Summary:	Flexible partitioning tool
Summary(pl):	GNU Parted - narzêdzie do zarz±dzania partycjami na dyskach
Name:		parted
Version:	1.2.3
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Vendor:		Andrew Clausen <clausen@alphalink.com.au>
Source0:	ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/parted/
BuildPrereq:	e2fsprogs-devel
BuildPrereq:	readline-devel >= 4.1
BuildPrereq:	ncurses-devel >= 5.0
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
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Satic libparted.

%description -l pl static
Biblioteka statyczna libparted.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
gettextize --copy --force
%configure \
	--with-readline \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf doc/{API,FAT,USER} AUTHORS BUGS ChangeLog NEWS README THANKS TODO \
	$RPM_BUILD_ROOT%{_mandir}/man*/*

%find_lang %{name}

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
