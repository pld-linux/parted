#
# Conditional build:
%bcond_with	static		# link statically
%bcond_without	nls		# build without NLS
%bcond_without	readline	# build without readline support
%bcond_with	selinux		# SELinux support
%bcond_with	uClibc		# add somewhat nasty uClibc patch, that
#				# shouldn't cause problems, but who knows...
%bcond_without	po4a		# do not use po4a (for pt_BR manual)
#
Summary:	Flexible partitioning tool
Summary(es.UTF-8):	Herramienta de particionamiento flexible
Summary(pl.UTF-8):	GNU Parted - narzędzie do zarządzania partycjami na dyskach
Summary(pt_BR.UTF-8):	Ferramenta flexível de particionamento
Summary(ru.UTF-8):	Программа GNU манипуляции дисковыми разделами
Summary(uk.UTF-8):	Програма GNU маніпуляції дисковими розділами
Name:		parted
Version:	3.1
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	http://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.xz
# Source0-md5:	5d89d64d94bcfefa9ce8f59f4b81bdcb
# restored from git repository
Source1:	%{name}.m4
Patch1:		%{name}-no_wrap.patch
Patch2:		%{name}-BIG_FAT_WARNING.patch
Patch3:		%{name}-uClibc.patch
Patch4:		%{name}-info.patch
Patch5:		%{name}-man-pt.patch
Patch6:		%{name}-link.patch
Patch7:		static.patch
URL:		http://www.gnu.org/software/parted/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	check >= 0.9.3
BuildRequires:	device-mapper-devel >= 1.02.02
BuildRequires:	gettext-devel >= 0.18
BuildRequires:	libblkid-devel >= 2.17
%if %{with selinux}
BuildRequires:	libselinux-devel
BuildRequires:	libsepol-devel
%endif
BuildRequires:	libtool
BuildRequires:	libuuid-devel
%{?with_static:BuildRequires:	libuuid-static}
%{?with_readline:BuildRequires:	ncurses-devel >= 5.2}
BuildRequires:	pkgconfig
%{?with_po4a:BuildRequires:	po4a}
%{?with_readline:BuildRequires:	readline-devel >= 5.2}
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.2
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Parted is a program that allows you to create, destroy, resize,
move and copy hard disk partitions. This is useful for creating space
for new operating systems, reorganising disk usage, and copying data
to new hard disks.

%description -l es.UTF-8
GNU Parted es un programa que permite crear, destruir, redimensionar,
mover y copiar particiones de discos duros. Es útil para crear espacio
para nuevos sistemas operacionales, reorganizar el uso del disco, y
copiar datos para nuevos discos duros.

%description -l pl.UTF-8
GNU Parted jest programem który umożliwia tworzenie, usuwanie, zmianę
rozmiaru, przesuwanie i kopiowanie partycji na dyskach. Może być
użyteczny przy tworzeniu partycji pod nowy system jak i przy
reorganizacji sposobu wykorzystywania dysków, a także ich kopiowaniu.

%description -l pt_BR.UTF-8
O GNU Parted é um programa que permite criar, destruir, redimensionar,
mover e copiar partições de discos rígidos. É útil para criar espaço
para novos sistemas operacionais, reorganizar o uso do disco, e copiar
dados para novos discos rígidos.

%description -l ru.UTF-8
GNU Parted - это программа, позволяющая вам создавать, удалять, менять
размер, перемещать и копировать разделы на жестких дисках. Это полезно
для создания места для размещения новых операционных систем,
реорганизации использования диска и копирования данных на новые диски.

%description -l uk.UTF-8
GNU Parted - це програма, яка дозволяє вам створювати, видаляти,
змінювати розмір, переміщувати та копіювати розділи на жорстких
дисках. Це корисно для створення місця для розміщення нових
операційних систем, реорганізації використання диску та копіювання
даних на нові диски.

%package libs
Summary:	Parted shared library
Summary(pl.UTF-8):	Biblioteka współdzielona Parteda
Group:		Libraries
Requires:	device-mapper >= 1.02.02
Requires:	libblkid >= 2.17
Suggests:	progsreiserfs >= 0.3.1
Conflicts:	parted < 2.3

%description libs
Parted shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona Parteda.

%package devel
Summary:	Files required to compile software that uses libparted
Summary(es.UTF-8):	Archivos de desarrollo para libparted
Summary(pl.UTF-8):	Pliki wymagane przy kompilacji programów używających libparted
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento para a libparted
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	device-mapper-devel >= 1.02.02
Requires:	libblkid-devel >= 2.17
Requires:	libuuid-devel

%description devel
Files required to compile software that uses libparted.

%description devel -l es.UTF-8
Este paquete incluye los archivos de encabezamiento y bibliotecas
necesarios para ligar estáticamente programas con libparted.

%description devel -l pl.UTF-8
Pliki wymagane przy kompilacji programów używających libparted.

%description devel -l pt_BR.UTF-8
O GNU Parted é um programa que permite criar, destruir, redimensionar,
mover e copiar partições de discos rígidos. É útil para criar espaço
para novos sistemas operacionais, reorganizar o uso do disco, e copiar
dados para novos discos rígidos. Este pacote inclui os arquivos de
cabeçalho e bibliotecas necessários para ligar estaticamente programas
com a libparted.

%package static
Summary:	Static libparted library
Summary(pl.UTF-8):	Biblioteka statyczna libparted
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libparted library.

%description static -l pl.UTF-8
Biblioteka statyczna libparted.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%{?with_uClibc:%patch3 -p1}
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%{__rm} po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_nls:--disable-nls} \
	--disable-silent-rules \
	%{?with_selinux:--enable-selinux} \
	%{?with_static:--without-pic} \
	--with-readline%{!?with_readline:=no}

%{!?with_nls:touch include/libintl.h}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

%if %{with po4a}
# not supported yet by am
install -d $RPM_BUILD_ROOT%{_mandir}/pt_BR/man8
install doc/pt_BR/*.8 $RPM_BUILD_ROOT%{_mandir}/pt_BR/man8
%endif

# missing in sources
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_aclocaldir}/parted.m4

%{?with_nls:%find_lang %{name}}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files %{?with_nls:-f %{name}.lang}
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%lang(ja) %doc doc/USER.jp
%attr(755,root,root) %{_sbindir}/parted
%attr(755,root,root) %{_sbindir}/partprobe
%{_mandir}/man8/parted.8*
%{_mandir}/man8/partprobe.8*
%if %{with po4a}
%lang(pt) %{_mandir}/pt_BR/man8/*
%endif
%{_infodir}/parted.info*

%if %{without static}
%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libparted.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libparted.so.2
%attr(755,root,root) %{_libdir}/libparted-fs-resize.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libparted-fs-resize.so.0
%endif

%files devel
%defattr(644,root,root,755)
%doc doc/{API,FAT}
%if %{without static}
%attr(755,root,root) %{_libdir}/libparted.so
%attr(755,root,root) %{_libdir}/libparted-fs-resize.so
%endif
%{_includedir}/parted
%{_pkgconfigdir}/libparted.pc
%{_aclocaldir}/parted.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libparted.a
%{_libdir}/libparted-fs-resize.a
