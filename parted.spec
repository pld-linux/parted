Summary:	Flexible partitioning tool
Summary(pl):	GNU Parted - narzêdzie do zarz±dzania partycjami na dyskach
Name:		parted
Version:	1.1.0
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Vendor:		Andrew Clausen <clausen@alphalink.com.au>
Source:		ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/parted/
BuildPrereq:	e2fsprogs-devel
BuildPrereq:	readline-devel
BuildPrereq:	ncurses-devel >= 5.0
Buildroot:	/tmp/%{name}-%{version}-root

%description
GNU Parted is a program that allows you to create, destroy, resize, move
and copy hard disk partitions. This is useful for creating space for new
operating systems, reorganising disk usage, and copying data to new hard
disks.

%description -l pl
GNU Parted jest programem który umo¿liwia teorzenie, usuwanie, zmianê
rozmiaru, przesuwanie i kopiowanie partycji na dyskach. Mo¿e byæ u¿yteczny 
przy tworzeniu partycji pod nowy system jak i przy reorganizacji sposobu
wykorzystywania dysków, a tak¿e ich kopiowaniu.

%package devel
Summary:	Files required to compile software that uses libparted
Summary(pl):	Pliki wymagane przy kompilacji programów u¿ywaj±cych libparted
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	e2fsprogs-devel

%description devel
This package includes the header files and libraries needed to statically
link software with libparted.

%description -l pl devel
Pakiet zawiera pliki nag³ówkowe i bibliotekê statyczn± libparted.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
gettextize --copy --force
%configure \
	--with-readline \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf API AUTHORS BUGS ChangeLog HACKING NEWS README THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/parted

%files devel
%defattr(644,root,root,755)
%{_includedir}/parted
%{_libdir}/libparted.a
