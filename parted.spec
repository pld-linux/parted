# TODO:
# - put library to separate package
#
# Conditional build:
%bcond_with	static		# link statically
%bcond_without	nls		# build without NLS
%bcond_without	readline	# build without readline support
%bcond_with	uClibc		# add somewhat nasty uClibc patch, that
#				# shouldn't cause problems, but who knows...
#
Summary:	Flexible partitioning tool
Summary(es):	Herramienta de particionamiento flexible
Summary(pl):	GNU Parted - narzêdzie do zarz±dzania partycjami na dyskach
Summary(pt_BR):	Ferramenta flexível de particionamento
Summary(ru):	ðÒÏÇÒÁÍÍÁ GNU ÍÁÎÉÐÕÌÑÃÉÉ ÄÉÓËÏ×ÙÍÉ ÒÁÚÄÅÌÁÍÉ
Summary(uk):	ðÒÏÇÒÁÍÁ GNU ÍÁÎ¦ÐÕÌÑÃ¦§ ÄÉÓËÏ×ÉÍÉ ÒÏÚÄ¦ÌÁÍÉ
Name:		parted
Version:	1.8.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.gz
# Source0-md5:	52d3e565fc3369d3388a9e02d4b17410
Patch0:		%{name}-pl.po-update.patch
Patch1:		%{name}-no_wrap.patch
Patch2:		%{name}-BIG_FAT_WARNING.patch
Patch3:		%{name}-uClibc.patch
Patch4:		%{name}-info.patch
Patch5:		%{name}-link.patch
Patch6:		%{name}-etherd.patch
Patch7:		%{name}-segv.patch
Patch8:		%{name}-headers.patch
Patch9:		%{name}-man-pt.patch
URL:		http://www.gnu.org/software/parted/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	device-mapper-devel >= 1.02.02
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
%{?with_static:BuildRequires:	libuuid-static}
%{?with_readline:BuildRequires:	ncurses-devel >= 5.2}
BuildRequires:	po4a
%{?with_readline:BuildRequires:	readline-devel >= 5.0}
BuildRequires:	texinfo >= 4.2
Requires(post,postun):	/sbin/ldconfig
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
GNU Parted jest programem który umo¿liwia tworzenie, usuwanie, zmianê
rozmiaru, przesuwanie i kopiowanie partycji na dyskach. Mo¿e byæ
u¿yteczny przy tworzeniu partycji pod nowy system jak i przy
reorganizacji sposobu wykorzystywania dysków, a tak¿e ich kopiowaniu.

%description -l pt_BR
O GNU Parted é um programa que permite criar, destruir, redimensionar,
mover e copiar partições de discos rígidos. É útil para criar espaço
para novos sistemas operacionais, reorganizar o uso do disco, e copiar
dados para novos discos rígidos.

%description -l ru
GNU Parted - ÜÔÏ ÐÒÏÇÒÁÍÍÁ, ÐÏÚ×ÏÌÑÀÝÁÑ ×ÁÍ ÓÏÚÄÁ×ÁÔØ, ÕÄÁÌÑÔØ, ÍÅÎÑÔØ
ÒÁÚÍÅÒ, ÐÅÒÅÍÅÝÁÔØ É ËÏÐÉÒÏ×ÁÔØ ÒÁÚÄÅÌÙ ÎÁ ÖÅÓÔËÉÈ ÄÉÓËÁÈ. üÔÏ ÐÏÌÅÚÎÏ
ÄÌÑ ÓÏÚÄÁÎÉÑ ÍÅÓÔÁ ÄÌÑ ÒÁÚÍÅÝÅÎÉÑ ÎÏ×ÙÈ ÏÐÅÒÁÃÉÏÎÎÙÈ ÓÉÓÔÅÍ,
ÒÅÏÒÇÁÎÉÚÁÃÉÉ ÉÓÐÏÌØÚÏ×ÁÎÉÑ ÄÉÓËÁ É ËÏÐÉÒÏ×ÁÎÉÑ ÄÁÎÎÙÈ ÎÁ ÎÏ×ÙÅ ÄÉÓËÉ.

%description -l uk
GNU Parted - ÃÅ ÐÒÏÇÒÁÍÁ, ÑËÁ ÄÏÚ×ÏÌÑ¤ ×ÁÍ ÓÔ×ÏÒÀ×ÁÔÉ, ×ÉÄÁÌÑÔÉ,
ÚÍ¦ÎÀ×ÁÔÉ ÒÏÚÍ¦Ò, ÐÅÒÅÍ¦ÝÕ×ÁÔÉ ÔÁ ËÏÐ¦À×ÁÔÉ ÒÏÚÄ¦ÌÉ ÎÁ ÖÏÒÓÔËÉÈ
ÄÉÓËÁÈ. ãÅ ËÏÒÉÓÎÏ ÄÌÑ ÓÔ×ÏÒÅÎÎÑ Í¦ÓÃÑ ÄÌÑ ÒÏÚÍ¦ÝÅÎÎÑ ÎÏ×ÉÈ
ÏÐÅÒÁÃ¦ÊÎÉÈ ÓÉÓÔÅÍ, ÒÅÏÒÇÁÎ¦ÚÁÃ¦§ ×ÉËÏÒÉÓÔÁÎÎÑ ÄÉÓËÕ ÔÁ ËÏÐ¦À×ÁÎÎÑ
ÄÁÎÉÈ ÎÁ ÎÏ×¦ ÄÉÓËÉ.

%package devel
Summary:	Files required to compile software that uses libparted
Summary(es):	Archivos de desarrollo para libparted
Summary(pl):	Pliki wymagane przy kompilacji programów u¿ywaj±cych libparted
Summary(pt_BR):	Arquivos de desenvolvimento para a libparted
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	device-mapper-devel >= 1.02.02
Requires:	libuuid-devel

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
Summary:	Static libparted library
Summary(pl):	Biblioteka statyczna libparted
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libparted library.

%description static -l pl
Biblioteka statyczna libparted.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?with_uClibc:%patch3 -p1}
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

rm -f po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_readline:--without-readline} \
	%{?with_readline:--with-readline} \
	%{!?with_nls:--disable-nls} \
	%{?with_static:--without-pic}

%{!?with_nls:touch include/libintl.h}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

# not supported yet by am
install -d $RPM_BUILD_ROOT%{_mandir}/pt_BR/man8
install doc/pt_BR/*.8 $RPM_BUILD_ROOT%{_mandir}/pt_BR/man8

%{?with_nls:%find_lang %{name}}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files %{?with_nls:-f %{name}.lang}
%defattr(644,root,root,755)
%doc doc/{API,FAT} AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%lang(ja) %doc doc/USER.jp
%attr(755,root,root) %{_sbindir}/*
%{!?with_static:%attr(755,root,root) %{_libdir}/libparted-*.so.*.*}
%{_mandir}/man8/*
%lang(pt) %{_mandir}/pt_BR/man8/*
%{_infodir}/parted.info*

%files devel
%defattr(644,root,root,755)
%{!?with_static:%attr(755,root,root) %{_libdir}/libparted.so}
%{_libdir}/libparted.la
%{_includedir}/parted
%{_aclocaldir}/parted.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libparted.a
