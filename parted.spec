# conditional build
#  --with static
#  --without nls
#  --without readline
#  --with uClibc -- add somewhat nasty uClibc patch, that shouldn't cause
#                   problems, but who knows...
Summary:	Flexible partitioning tool
Summary(es):	Herramienta de particionamiento flexible
Summary(pl):	GNU Parted - narzêdzie do zarz±dzania partycjami na dyskach
Summary(pt_BR):	Ferramenta flexível de particionamento
Name:		parted
Version:	1.4.24
Release:	1
License:	GPL
Group:		Applications/System
Vendor:		Andrew Clausen <clausen@gnu.org>
Source0:	ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.gz
Patch0:		%{name}-BOOT.patch
Patch1:		%{name}-llseek.patch
Patch2:		%{name}-no_wrap.patch
Patch3:		%{name}-BIG_FAT_WARNING.patch
Patch4:		%{name}-uClibc.patch
URL:		http://www.gnu.org/software/parted/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
%{?_with_static:BuildRequires:	e2fsprogs-static}
BuildRequires:	gettext-devel
BuildRequires:	libtool
%{!?_without_readline:BuildRequires:	ncurses-devel >= 5.2}
%{!?_without_readline:BuildRequires:	readline-devel >= 4.2}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Parted is a program that allows you to create, destroy, resize,
move and copy hard disk partitions. This is useful for creating space
for new operating systems, reorganising disk usage, and copying data
to new hard disks.

%description -l es
GNU Parted es un programa que permite crear, destruir, redimensionar,
mover y copiar particiones de discos duros. Es útil para crear espacio
para nuevos sistemas operacionales, reorganizar el uso del disco, y
copiar datos para nuevos discos duros.

%description -l pl
GNU Parted jest programem który umo¿liwia teorzenie, usuwanie, zmianê
rozmiaru, przesuwanie i kopiowanie partycji na dyskach. Mo¿e byæ
u¿yteczny przy tworzeniu partycji pod nowy system jak i przy
reorganizacji sposobu wykorzystywania dysków, a tak¿e ich kopiowaniu.

%description -l pt_BR
O GNU Parted é um programa que permite criar, destruir, redimensionar,
mover e copiar partições de discos rígidos. É útil para criar espaço
para novos sistemas operacionais, reorganizar o uso do disco, e copiar
dados para novos discos rígidos.

%package devel
Summary:	Files required to compile software that uses libparted
Summary(es):	Archivos de desarrollo para libparted
Summary(pl):	Pliki wymagane przy kompilacji programów u¿ywaj±cych libparted
Summary(pt_BR):	Arquivos de desenvolvimento para a libparted
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	e2fsprogs-devel

%description devel
Files required to compile software that uses libparted.

%description devel -l es
Este paquete incluye los archivos de encabezamiento y bibliotecas
necesarios para ligar estáticamente programas con libparted.

%description devel -l pl
Pliki wymagane przy kompilacji programów u¿ywaj±cych libparted.

%description devel -l pt_BR
O GNU Parted é um programa que permite criar, destruir, redimensionar,
mover e copiar partições de discos rígidos. É útil para criar espaço
para novos sistemas operacionais, reorganizar o uso do disco, e copiar
dados para novos discos rígidos. Este pacote inclui os arquivos de
cabeçalho e bibliotecas necessários para ligar estaticamente programas
com a libparted.

%package static
Summary:	Satic libparted
Summary(pl):	Biblioteka statyczna libparted
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Satic libparted.

%description static -l pl
Biblioteka statyczna libparted.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%{?_with_uClibc.spec:%patch4 -p1}

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal
automake -a -c
autoheader
autoconf

%configure \
	%{?_without_readline:--without-readline} \
	%{!?_without_readline:--with-readline} \
	--without-included-gettext \
	%{?_without_nls:--disable-nls} \
	%{?_with_static:--without-pic} \
	%{?_with_static:--enable-all-static} \
	%{!?_with_static:--enable-shared}

%{?_without_nls:touch include/libintl.h}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

gzip -9nf doc/{API,FAT,USER} AUTHORS BUGS ChangeLog NEWS README THANKS TODO

%{!?_without_nls:%find_lang %{name}}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files %{!?_without_nls:-f %{name}.lang}
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_sbindir}/parted
%{!?_with_static:%attr(755,root,root) %{_libdir}/lib*.so.*.*}
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/parted
%{!?_with_static:%attr(755,root,root) %{_libdir}/lib*.so}
%attr(755,root,root) %{_libdir}/lib*.la
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
