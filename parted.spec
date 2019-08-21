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
Version:	3.2
Release:	5
License:	GPL v3+
Group:		Applications/System
Source0:	http://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.xz
# Source0-md5:	0247b6a7b314f8edeb618159fa95f9cb
# restored from git repository
Source1:	%{name}.m4

Patch01:	0001-tests-Try-several-UTF8-locales.patch
Patch02:	0002-maint-post-release-administrivia.patch
Patch03:	0003-lib%{name}-also-link-to-UUID_LIBS.patch
Patch04:	0004-lib-fs-resize-Prevent-crash-resizing-FAT16-file-syst.patch
Patch05:	0005-tests-t3000-resize-fs.sh-Add-FAT16-resizing-test.patch
Patch06:	0006-tests-t3000-resize-fs.sh-Add-requirement-on-mkfs.vfa.patch
Patch07:	0007-tests-Change-minimum-size-to-256MiB.patch
Patch08:	0008-%{name}-don-t-crash-in-disk_set-when-disk-label-not-f.patch
Patch09:	0009-tests-Add-a-test-for-device-mapper-partition-sizes.patch
Patch10:	0010-lib%{name}-device-mapper-uses-512b-sectors.patch
Patch11:	0011-Update-manpage-NAME-so-whatis-will-work.patch
Patch12:	0012-tests-Make-sure-the-extended-partition-length-is-cor.patch
Patch13:	0013-lib%{name}-BLKPG_RESIZE_PARTITION-uses-bytes-not-sect.patch
Patch14:	0014-%{name}-Fix-crash-with-name-command-and-no-disklabel-.patch
Patch15:	0015-UI-Avoid-memory-leaks.patch
Patch16:	0016-lib%{name}-Fix-memory-leaks.patch
Patch17:	0017-lib%{name}-Fix-possible-memory-leaks.patch
Patch18:	0018-lib%{name}-Stop-converting-.-in-sys-path-to.patch
Patch19:	0019-lib%{name}-Use-read-only-when-probing-devices-on-linu.patch
Patch20:	0020-tests-Use-wait_for_dev_to_-functions.patch
Patch21:	0021-fdasd-geometry-handling-updated-from-upstream-s390-t.patch
Patch22:	0022-dasd-enhance-device-probing.patch
Patch23:	0023-%{name}-fix-build-error-on-s390.patch
Patch24:	0024-fdasd.c-Safeguard-against-geometry-misprobing.patch
Patch25:	0025-Add-lib%{name}-fs-resize.pc.patch
Patch26:	0026-tests-Add-udevadm-settle-to-wait_for_-loop-1260664.patch
Patch27:	0027-tests-Add-wait-to-t9042-1257415.patch
Patch28:	0028-tests-Fix-t1700-failing-on-a-host-with-a-4k-xfs-file.patch
Patch29:	0029-lib-fs-resize-Prevent-crash-resizing-FAT-with-very-d.patch
Patch30:	0030-tests-t3000-resize-fs.sh-Add-very-deep-directory.patch
Patch31:	0031-Use-BLKSSZGET-to-get-device-sector-size-in-_device_p.patch
Patch32:	0032-%{name}-fix-the-rescue-command.patch
Patch33:	0033-Use-disk-geometry-as-basis-for-ext2-sector-sizes.patch
Patch34:	0034-docs-Add-list-of-filesystems-for-fs-type-1311596.patch
Patch35:	0035-%{name}-Display-details-of-partition-alignment-failur.patch
Patch36:	0036-lib%{name}-Remove-fdasd-geometry-code-from-alloc_meta.patch
Patch37:	0037-lib%{name}-Fix-probing-AIX-disks-on-other-arches.patch
Patch38:	0038-partprobe-Open-the-device-once-for-probing.patch
Patch39:	0039-Cleanup-mkpart-manpage-entry-1183077.patch
Patch40:	0040-doc-Add-information-about-quoting.patch
Patch41:	0041-lib%{name}-dasd-correct-the-offset-where-the-first-pa.patch
Patch42:	0042-Add-support-for-NVMe-devices.patch
Patch43:	0043-docs-Improve-partition-description-in-%{name}.texi.patch
Patch44:	0044-lib%{name}-only-IEC-units-are-treated-as-exact.patch
Patch45:	0045-tests-t3310-flags.sh-Query-lib%{name}-for-all-flags-t.patch
Patch46:	0046-tests-t3310-flags.sh-Stop-excluding-certain-flags-fr.patch
Patch47:	0047-tests-t3310-flags.sh-Add-test-for-bsd-table-flags.patch
Patch48:	0048-lib%{name}-Fix-to-report-success-when-setting-lvm-fla.patch
Patch49:	0049-lib%{name}-Remove-commented-local-variable-from-bsd_p.patch
Patch50:	0050-tests-t3310-flags.sh-Add-test-for-mac-table-flags.patch
Patch51:	0051-tests-t3310-flags.sh-Add-test-for-dvh-table-flags.patch
Patch52:	0052-tests-t3310-flags.sh-Add-tests-for-remaining-table-t.patch
Patch53:	0053-tests-Set-optimal-blocks-to-64-for-scsi_debug-device.patch
Patch54:	0054-tests-t3310-flags.sh-skip-pc98-when-sector-size-512.patch
Patch55:	0055-tests-Stop-timing-t9040-1172675.patch
Patch56:	0056-lib%{name}-Fix-starting-CHS-in-protective-MBR.patch
Patch57:	0057-lib%{name}-Don-t-warn-if-no-HDIO_GET_IDENTITY-ioctl.patch
Patch58:	0058-lib%{name}-dasd-unify-vtoc-handling-for-cdl-ldl.patch
Patch59:	0059-lib%{name}-dasd-update-and-improve-fdasd-functions.patch
Patch60:	0060-lib%{name}-dasd-add-new-fdasd-functions.patch
Patch61:	0061-lib%{name}-dasd-add-test-cases-for-the-new-fdasd-func.patch
Patch62:	0062-lib%{name}-set-swap-flag-on-GPT-partitions.patch
Patch63:	0063-tests-Update-t0220-and-t0280-for-the-swap-flag.patch
Patch64:	0064-lib%{name}-tests-Move-get_sector_size-to-common.c.patch
Patch65:	0065-lib%{name}-Add-support-for-atari-partition-tables.patch
Patch66:	0066-mac-copy-partition-type-and-name-correctly.patch
Patch67:	0067-lib%{name}-Fix-MacOS-boot-support.patch
Patch68:	0068-lib%{name}-Fix-typo-in-hfs-error-message.patch
Patch69:	0069-Fix-crash-when-localized.patch
Patch70:	0070-Add-support-for-RAM-drives.patch
Patch71:	0071-%{name}-check-the-name-of-partition-first-when-to-nam.patch
Patch72:	0072-%{name}-ui-remove-unneccesary-information-of-command-.patch
Patch73:	0073-libpartd-dasd-improve-flag-processing-for-DASD-LDL.patch
Patch74:	0074-lib%{name}-dasd-add-an-exception-for-changing-DASD-LD.patch
Patch75:	0075-lib%{name}-dasd-add-test-cases-for-the-new-fdasd-func.patch
Patch76:	0076-Increase-timeout-for-rmmod-scsi_debug-and-make-it-a-.patch
Patch77:	0077-tests-t1701-rescue-fs-wait-for-the-device-to-appear.patch
Patch78:	0078-lib%{name}-Fix-udev-cookie-leak-in-_dm_resize_partiti.patch
Patch79:	0079-atari.c-Drop-xlocale.h-1476934.patch
Patch80:	0080-libparted-labels-link-with-libiconv-if-needed.patch
Patch81:	0081-Add-support-for-NVDIMM-devices.patch
Patch82:	0082-linux-Include-sys-sysmacros.h-for-major-macro.patch
Patch83:	0083-Fix-make-check.patch
Patch84:	0084-tests-fix-t6100-mdraid-partitions.patch
Patch85:	0085-Fix-set-and-disk_set-to-not-crash-when-no-flags-are-.patch
Patch86:	0086-mkpart-Allow-negative-start-value-when-FS-TYPE-is-no.patch
Patch87:	0087-Fix-resizepart-iec-unit-end-sector.patch
Patch88:	0088-build-Remove-unused-traces-of-dynamic-loading.patch
Patch89:	0089-Lift-512-byte-restriction-on-fat-resize.patch
Patch90:	0090-Fix-atari-label-false-positives.patch
Patch91:	0091-Modify-gpt-header-move-and-msdos-overlap-to-work-wit.patch
Patch92:	0092-Switch-gpt-header-move-and-msdos-overlap-to-python3.patch
Patch93:	0093-libparted-Fix-ending-CHS-address-in-PMBR.patch
Patch94:	0094-Fix-the-length-of-several-strncpy-calls.patch
Patch95:	0095-parted.c-Always-free-peek_word.patch
Patch96:	0096-parted.c-Make-sure-dev_name-is-freed.patch
Patch97:	0097-t6100-mdraid-partitions-Use-v0.90-metadata-for-the-t.patch
Patch98:	0098-Fix-potential-command-line-buffer-overflow.patch
Patch99:	0099-libparted-Add-support-for-MBR-id-GPT-GUID-and-detect.patch
Patch100:	0100-Add-udf-to-t1700-probe-fs-and-to-the-manpage.patch
Patch101:	0101-ped_unit_get_name-Resolve-conflicting-attributes-con.patch
Patch102:	0102-Fix-warnings-from-GCC-7-s-Wimplicit-fallthrough.patch
Patch103:	0103-Read-NVMe-model-names-from-sysfs.patch
Patch104:	0104-parted-fix-crash-due-to-improper-partition-number-in.patch
Patch105:	0105-parted-fix-wrong-error-label-jump-in-mkpart.patch
Patch106:	0106-clean-the-disk-information-when-commands-fail-in-int.patch
Patch107:	0107-parted-Remove-PED_ASSERT-from-ped_partition_set_name.patch
Patch108:	0108-Added-support-for-Windows-recovery-partition-WINRE-o.patch
Patch109:	0109-t6000-dm-Stop-using-private-lvm-root.patch
Patch110:	0110-Avoid-sigsegv-in-case-2nd-nilfs2-superblock-magic-ac.patch
Patch111:	0111-Tests-case-for-sigsegv-when-false-nilfs2-superblock-.patch

Patch1001:	%{name}-no_wrap.patch
Patch1002:	%{name}-BIG_FAT_WARNING.patch
Patch1003:	%{name}-uClibc.patch
Patch1004:	%{name}-info.patch
Patch1005:	%{name}-man-pt.patch
Patch1006:	%{name}-link.patch
Patch1007:	static.patch
URL:		http://www.gnu.org/software/parted/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11.6
BuildRequires:	check >= 0.9.3
BuildRequires:	device-mapper-devel >= 1.02.02
BuildRequires:	gettext-tools >= 0.18
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
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1

%patch1001 -p1
%patch1002 -p1
%{?with_uClibc:%patch1003 -p1}
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1

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
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libparted*.la

# missing in sources
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_aclocaldir}/parted.m4

%{?with_nls:%find_lang %{name}}

%{__rm} -f $RPM_BUILD_ROOT%{_infodir}/dir

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
# too little is translated as of 3.2
#%lang(pt_BR) %{_mandir}/pt_BR/man8/parted.8*
#%lang(pt_BR) %{_mandir}/pt_BR/man8/partprobe.8*
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
%{_pkgconfigdir}/libparted-fs-resize.pc
%{_aclocaldir}/parted.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libparted.a
%{_libdir}/libparted-fs-resize.a
