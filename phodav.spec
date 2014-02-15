Summary:	Phodav - WebDAV server implementation using libsoup
Summary(en.UTF-8):	Phởdav - WebDAV server implementation using libsoup
Summary(pl.UTF-8):	Phởdav - implementacja serwera WebDAV wykorzystująca libsoup
Name:		phodav
Version:	0.1.17
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/phodav/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	0a5843ba6a3984fb57a0257b1e8975f1
URL:		https://wiki.gnome.org/phodav
BuildRequires:	asciidoc
BuildRequires:	avahi-devel
BuildRequires:	avahi-gobject-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto
BuildRequires:	xz
Requires:	systemd-units
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phodav is a WebDAV server implementation using libsoup (RFC 4918).

%description -l en.UTF-8
phởdav is a WebDAV server implementation using libsoup (RFC 4918).

%description -l pl.UTF-8
phởdav to implementacja serwera WebDAV wykorzystująca libsoup
(RFC 4918).

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--with-systemdsystemunitdir=%{systemdunitdir} \
	--with-udevdir=/lib/udev
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/chezdav
%attr(755,root,root) %{_sbindir}/spice-webdavd
%{systemdunitdir}/spice-webdavd.service
%{systemdunitdir}/spice-webdavd.target
/lib/udev/rules.d/70-spice-webdavd.rules
%{_mandir}/man1/chezdav.1*
