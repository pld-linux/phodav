Summary:	Phodav - WebDAV server implementation using libsoup
Summary(en.UTF-8):	Phởdav - WebDAV server implementation using libsoup
Summary(pl.UTF-8):	Phởdav - implementacja serwera WebDAV wykorzystująca libsoup
Name:		phodav
Version:	0.4
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/phodav/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	02036f62c7094a11123924c6d5605c9f
URL:		https://wiki.gnome.org/phodav
BuildRequires:	asciidoc
BuildRequires:	attr-devel
BuildRequires:	avahi-devel
BuildRequires:	avahi-gobject-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
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
phởdav to implementacja serwera WebDAV wykorzystująca libsoup
(RFC 4918).

%package libs
Summary:	PhoDAV - WebDAV library based on libsoup
Summary(pl.UTF-8):	PhoDAV - biblioteka WebDAV oparta na libsoup
Group:		Libraries
Requires:	libsoup >= 2.4

%description libs
PhoDAV - WebDAV library based on libsoup.

%description libs -l pl.UTF-8
PhoDAV - biblioteka WebDAV oparta na libsoup.

%package devel
Summary:	Header files for PhoDAV library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki PhoDAV
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libsoup-devel >= 2.4

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

%description apidocs
API documentation for PhoDAV library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki PhoDAV.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir} \
	--with-systemdsystemunitdir=%{systemdunitdir} \
	--with-udevdir=/lib/udev
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/chezdav
%attr(755,root,root) %{_sbindir}/spice-webdavd
%{systemdunitdir}/spice-webdavd.service
%{systemdunitdir}/spice-webdavd.target
/lib/udev/rules.d/70-spice-webdavd.rules
%{_mandir}/man1/chezdav.1*

%files libs
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_libdir}/libphodav-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libphodav-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libphodav-1.0.so
%{_includedir}/libphodav-1.0
%{_pkgconfigdir}/libphodav-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libphodav-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/phodav
