Summary:	Flexible partitioning tool
Summary(es):	Herramienta de particionamiento flexible
Summary(pl):	GNU Parted - narzÍdzie do zarz±dzania partycjami na dyskach
Summary(pt_BR):	Ferramenta flexÌvel de particionamento
Name:		parted
Version:	1.4.23
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Vendor:		Andrew Clausen <clausen@gnu.org>
Source0:	ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.gz
Patch0:		%{name}-BOOT.patch
Patch1:		%{name}-llseek.patch
Patch2:		%{name}-no_wrap.patch
Patch3:		%{name}-BIG_FAT_WARNING.patch
URL:		http://www.gnu.org/software/parted/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
%if %{?BOOT:1}%{!?BOOT:0}
BuildRequires:	e2fsprogs-static
%endif
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Parted is a program that allows you to create, destroy, resize,
move and copy hard disk partitions. This is useful for creating space
for new operating systems, reorganising disk usage, and copying data
to new hard disks.

%description -l es
GNU Parted es un programa que permite crear, destruir, redimensionar,
mover y copiar particiones de discos duros. Es ˙til para crear espacio
para nuevos sistemas operacionales, reorganizar el uso del disco, y
copiar datos para nuevos discos duros.

%description -l pl
GNU Parted jest programem ktÛry umoøliwia teorzenie, usuwanie, zmianÍ
rozmiaru, przesuwanie i kopiowanie partycji na dyskach. Moøe byÊ
uøyteczny przy tworzeniu partycji pod nowy system jak i przy
reorganizacji sposobu wykorzystywania dyskÛw, a takøe ich kopiowaniu.

%description -l pt_BR
O GNU Parted È um programa que permite criar, destruir, redimensionar,
mover e copiar partiÁıes de discos rÌgidos. … ˙til para criar espaÁo
para novos sistemas operacionais, reorganizar o uso do disco, e copiar
dados para novos discos rÌgidos.

%package devel
Summary:	Files required to compile software that uses libparted
Summary(es):	Archivos de desarrollo para libparted
Summary(pl):	Pliki wymagane przy kompilacji programÛw uøywaj±cych libparted
Summary(pt_BR):	Arquivos de desenvolvimento para a libparted
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	e2fsprogs-devel

%description devel
Files required to compile software that uses libparted.

%description -l es devel
Este paquete incluye los archivos de encabezamiento y bibliotecas
necesarios para ligar est·ticamente programas con libparted.

%description -l pl devel
Pliki wymagane przy kompilacji programÛw uøywaj±cych libparted.

%description -l pt_BR devel
O GNU Parted È um programa que permite criar, destruir, redimensionar,
mover e copiar partiÁıes de discos rÌgidos. … ˙til para criar espaÁo
para novos sistemas operacionais, reorganizar o uso do disco, e copiar
dados para novos discos rÌgidos. Este pacote inclui os arquivos de
cabeÁalho e bibliotecas necess·rios para ligar estaticamente programas
com a libparted.

%package static
Summary:	Satic libparted
Summary(pl):	Biblioteka statyczna libparted
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Satic libparted.

%description -l pl static
Biblioteka statyczna libparted.

%if %{?BOOT:1}%{!?BOOT:0}
%package BOOT
Summary:	parted for bootdisk
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description BOOT
%endif

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal
automake -a -c
autoheader
autoconf
%if %{?BOOT:1}%{!?BOOT:0}
%configure \
	--disable-nls \
	--enable-all-static \
	--without-readline \
	--without-pic
%{__make} CFLAGS="-DUSE_OWN_LLSEEK -DNO_BIOS_GEOMETRY_WARNING %{rpmcflags}"
mv -f %{name}/%{name} %{name}-BOOT
%{__make} distclean
%endif

%configure \
	--with-readline \
	--without-included-gettext \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin
install %{name}-BOOT $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin/%{name}
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
%attr(755,root,root) %{_libdir}/bootdisk/sbin/*
%endif
