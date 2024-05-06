Summary:	Very fast and light web browser
Name:		dillo
Version:	3.1.0
Release:	1
# The OpenSSL exception is in dpi/https.c - AdamW 2008/12
License:	GPLv3+ with exceptions
Group:		Networking/WWW
URL:		http://www.dillo.org/
#Source0:	http://www.dillo.org/download/%{name}-%{version}.tar.bz2
Source0:	https://github.com/dillo-browser/dillo/releases/download/v%{version}/dillo-%{version}.tar.bz2
BuildRequires:	fltk-devel
BuildRequires:	jpeg-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(openssl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:	pkgconfig(xft)

%description
Dillo is a Web browser that's completely written in C, very fast, and small in
code base and binary. It is a graphical browser built upon FLTK2 and currently
renders a subset of HTML (no frames, no JavaScript, and no JVM).

%prep
%autosetup -p1

%build
%configure \
	--enable-ipv6 \
	--enable-tls
  
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 dillorc %{buildroot}%{_sysconfdir}/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Dillo
Comment=A simple web browser
Exec=%{name}
Icon=networking_www_section
Terminal=false
Type=Application
Categories=Network;WebBrowser;
EOF

%files
%doc AUTHORS ChangeLog* INSTALL NEWS README user_help.html
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/applications/dillo.desktop
%{_libdir}/%{name}/
%config(noreplace) %{_sysconfdir}/dillorc
%config(noreplace) %{_sysconfdir}/dillo/dillorc
%config(noreplace) %{_sysconfdir}/dillo/dpidrc
%config(noreplace) %{_sysconfdir}/dillo/keysrc
%config(noreplace) %{_sysconfdir}/dillo/domainrc
%config(noreplace) %{_sysconfdir}/dillo/hsts_preload
%{_iconsdir}/hicolor/*x*/apps/dillo.png
%{_mandir}/man1/dillo.1*

