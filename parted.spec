# conditional build:
#  --with static
#  --without nls
#  --without readline
#  --with uClibc -- add somewhat nasty uClibc patch, that shouldn't cause
#                   problems, but who knows...
#
Summary:	Flexible partitioning tool
Summary(es):	Herramienta de particionamiento flexible
Summary(pl):	GNU Parted - narzЙdzie do zarz╠dzania partycjami na dyskach
Summary(pt_BR):	Ferramenta flexМvel de particionamento
Summary(ru):	Программа GNU манипуляции дисковыми разделами
Summary(uk):	Програма GNU ман╕пуляц╕╖ дисковими розд╕лами
Name:		parted
Version:	1.6.5
Release:	1
License:	GPL
Group:		Applications/System
Vendor:		Andrew Clausen <clausen@gnu.org>
Source0:	ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.gz
Patch0:		%{name}-BOOT.patch
Patch1:		%{name}-no_wrap.patch
Patch2:		%{name}-BIG_FAT_WARNING.patch
Patch3:		%{name}-uClibc.patch
PAtch5:		%{name}-info.patch
Patch6:		%{name}-ah.patch
URL:		http://www.gnu.org/software/parted/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
%{?_with_static:BuildRequires:	e2fsprogs-static}
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	texinfo >= 4.2
%{!?_without_readline:BuildRequires:	ncurses-devel >= 5.2}
%{!?_without_readline:BuildRequires:	readline-devel >= 4.2}
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Parted is a program that allows you to create, destroy, resize,
move and copy hard disk partitions. This is useful for creating space
for new operating systems, reorganising disk usage, and copying data
to new hard disks.

%description -l es
GNU Parted es un programa que permite crear, destruir, redimensionar,
mover y copiar particiones de discos duros. Es Зtil para crear espacio
para nuevos sistemas operacionales, reorganizar el uso del disco, y
copiar datos para nuevos discos duros.

%description -l pl
GNU Parted jest programem ktСry umo©liwia tworzenie, usuwanie, zmianЙ
rozmiaru, przesuwanie i kopiowanie partycji na dyskach. Mo©e byФ
u©yteczny przy tworzeniu partycji pod nowy system jak i przy
reorganizacji sposobu wykorzystywania dyskСw, a tak©e ich kopiowaniu.

%description -l pt_BR
O GNU Parted И um programa que permite criar, destruir, redimensionar,
mover e copiar partiГУes de discos rМgidos. и Зtil para criar espaГo
para novos sistemas operacionais, reorganizar o uso do disco, e copiar
dados para novos discos rМgidos.

%description -l ru
GNU Parted - это программа, позволяющая вам создавать, удалять, менять
размер, перемещать и копировать разделы на жестких дисках. Это полезно
для создания места для размещения новых операционных систем,
реорганизации использования диска и копирования данных на новые диски.

%description -l uk
GNU Parted - це програма, яка дозволя╓ вам створювати, видаляти,
зм╕нювати розм╕р, перем╕щувати та коп╕ювати розд╕ли на жорстких
дисках. Це корисно для створення м╕сця для розм╕щення нових
операц╕йних систем, реорган╕зац╕╖ використання диску та коп╕ювання
даних на нов╕ диски.

%package devel
Summary:	Files required to compile software that uses libparted
Summary(es):	Archivos de desarrollo para libparted
Summary(pl):	Pliki wymagane przy kompilacji programСw u©ywaj╠cych libparted
Summary(pt_BR):	Arquivos de desenvolvimento para a libparted
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	e2fsprogs-devel

%description devel
Files required to compile software that uses libparted.

%description devel -l es
Este paquete incluye los archivos de encabezamiento y bibliotecas
necesarios para ligar estАticamente programas con libparted.

%description devel -l pl
Pliki wymagane przy kompilacji programСw u©ywaj╠cych libparted.

%description devel -l pt_BR
O GNU Parted И um programa que permite criar, destruir, redimensionar,
mover e copiar partiГУes de discos rМgidos. и Зtil para criar espaГo
para novos sistemas operacionais, reorganizar o uso do disco, e copiar
dados para novos discos rМgidos. Este pacote inclui os arquivos de
cabeГalho e bibliotecas necessАrios para ligar estaticamente programas
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
%{?_with_uClibc:%patch3 -p1}
%patch5 -p1
%patch6	-p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
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

%{!?_without_nls:%find_lang %{name}}

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files %{!?_without_nls:-f %{name}.lang}
%defattr(644,root,root,755)
%doc doc/{API,FAT,FAQ} AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_sbindir}/*
%{!?_with_static:%attr(755,root,root) %{_libdir}/lib*.so.*.*}
%{_mandir}/man*/*
%lang(pt) %{_mandir}/pt_BR/man*/*
%{_infodir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/parted
%{!?_with_static:%attr(755,root,root) %{_libdir}/lib*.so}
%{_libdir}/lib*.la
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
