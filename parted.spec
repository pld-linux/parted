Summary:	Flexible partitioning tool
Summary(pl):	GNU Parted - narzêdzie do zarz±dzania partycjami na dyskach
Name:		parted
Version:	1.4.11
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Vendor:		Andrew Clausen <clausen@gnu.org>
Source0:	ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/parted/
BuildRequires:	e2fsprogs-devel
%if %{?BOOT:1}%{!?BOOT:0}
BuildRequires:	e2fsprogs-static
%endif
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Parted is a program that allows you to create, destroy, resize,
move and copy hard disk partitions. This is useful for creating space
for new operating systems, reorganising disk usage, and copying data
to new hard disks.

%description -l pl
GNU Parted jest programem który umo¿liwia teorzenie, usuwanie, zmianê
rozmiaru, przesuwanie i kopiowanie partycji na dyskach. Mo¿e byæ
u¿yteczny przy tworzeniu partycji pod nowy system jak i przy
reorganizacji sposobu wykorzystywania dysków, a tak¿e ich kopiowaniu.

%package devel
Summary:	Files required to compile software that uses libparted
Summary(pl):	Pliki wymagane przy kompilacji programów u¿ywaj±cych libparted
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	e2fsprogs-devel

%description devel
Files required to compile software that uses libparted.

%description -l pl devel
Pliki wymagane przy kompilacji programów u¿ywaj±cych libparted.

%package static
Summary:	Satic libparted
Summary(pl):	Biblioteka statyczna libparted
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Satic libparted.

%description -l pl static
Biblioteka statyczna libparted.

%if %{?BOOT:1}%{!?BOOT:0}
%package BOOT
Summary:	parted for bootdisk
Group:		Applications/System

%description BOOT
%endif

%prep
%setup -q

%build
#rm missing
#libtoolize --copy --force
#gettextize --copy --force
#aclocal
#autoconf
#automake -a -c
%if %{?BOOT:1}%{!?BOOT:0}
%configure --disable-nls --enable-all-static --without-readline
%{__make}
mv -f %{name}/%{name} %{name}-BOOT
%{__make} clean
%endif

%configure \
	--with-readline \
	--without-included-gettext \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT/usr/lib/bootdisk/sbin
install -s %{name}-BOOT $RPM_BUILD_ROOT/usr/lib/bootdisk/sbin/%{name}
%endif

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

gzip -9nf doc/{API,FAT,USER} AUTHORS BUGS ChangeLog NEWS README THANKS TODO

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_sbindir}/parted
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/parted
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/bootdisk/sbin/*
%endif
