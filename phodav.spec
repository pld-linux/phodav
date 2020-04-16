Summary:	Phodav - WebDAV server implementation using libsoup
Summary(en.UTF-8):	Phởdav - WebDAV server implementation using libsoup
Summary(pl.UTF-8):	Phởdav - implementacja serwera WebDAV wykorzystująca libsoup
Name:		phodav
Version:	2.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/phodav/2.4/%{name}-%{version}.tar.xz
# Source0-md5:	7034f99ad6a510ddaa82bda12641b077
URL:		https://wiki.gnome.org/phodav
BuildRequires:	asciidoc
BuildRequires:	attr-devel
BuildRequires:	avahi-devel
BuildRequires:	avahi-gobject-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.51.2
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libsoup-devel >= 2.48.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.50
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-units
BuildRequires:	tar >= 1:1.22
# for udevdir
BuildRequires:	udev-devel
BuildRequires:	xmlto
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	systemd-units
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phodav is a WebDAV server implementation using libsoup (RFC 4918).

%description -l en.UTF-8
phởdav is a WebDAV server implementation using libsoup (RFC 4918).

%description -l pl.UTF-8
phởdav to implementacja serwera WebDAV wykorzystująca libsoup (RFC
4918).

%package libs
Summary:	PhoDAV - WebDAV library based on libsoup
Summary(pl.UTF-8):	PhoDAV - biblioteka WebDAV oparta na libsoup
Group:		Libraries
Requires:	glib2 >= 1:2.51.2
Requires:	libsoup >= 2.48.0

%description libs
PhoDAV - WebDAV library based on libsoup.

%description libs -l pl.UTF-8
PhoDAV - biblioteka WebDAV oparta na libsoup.

%package devel
Summary:	Header files for PhoDAV library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki PhoDAV
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libsoup-devel >= 2.48.0

%description devel
Header files for PhoDAV library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki PhoDAV.

%package static
Summary:	Static PhoDAV library
Summary(pl.UTF-8):	Statyczna biblioteka PhoDAV
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static PhoDAV library.

%description static -l pl.UTF-8
Statyczna biblioteka PhoDAV.

%package apidocs
Summary:	API documentation for PhoDAV library
Summary(pl.UTF-8):	Dokumentacja API biblioteki PhoDAV
Group:		Documentation
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
API documentation for PhoDAV library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki PhoDAV.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/chezdav
%attr(755,root,root) %{_sbindir}/spice-webdavd
%{systemdunitdir}/spice-webdavd.service
/lib/udev/rules.d/70-spice-webdavd.rules
%{_mandir}/man1/chezdav.1*

%files libs
%defattr(644,root,root,755)
%doc NEWS README.md TODO
%attr(755,root,root) %{_libdir}/libphodav-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libphodav-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libphodav-2.0.so
%{_includedir}/libphodav-2.0
%{_pkgconfigdir}/libphodav-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libphodav-2.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/phodav-2.0
