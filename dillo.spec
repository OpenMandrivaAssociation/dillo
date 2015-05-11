Summary:	Very fast and light web browser
Name:		dillo
Version:	3.0.4.1
Release:	1
# The OpenSSL exception is in dpi/https.c - AdamW 2008/12
License:	GPLv3+ with exceptions
Group:		Networking/WWW
URL:		http://www.dillo.org/
Source0:	http://www.dillo.org/download/%{name}-%{version}.tar.bz2
Source1:	http://www.dillo.org/download/%{name}-%{version}.tar.bz2.asc
BuildRequires:	fltk-devel
BuildRequires:	jpeg-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)

%description
Dillo is a Web browser that's completely written in C, very fast, and small in
code base and binary. It is a graphical browser built upon FLTK2 and currently
renders a subset of HTML (no frames, no JavaScript, and no JVM).

%prep
%setup -q

%build
%configure2_5x --enable-ipv6
%make

%install
%makeinstall_std

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
%doc AUTHORS ChangeLog* INSTALL NEWS README
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_libdir}/%{name}/
%config(noreplace) %{_sysconfdir}/dillorc
%config(noreplace) %{_sysconfdir}/dillo/dillorc
%config(noreplace) %{_sysconfdir}/dillo/dpidrc
%config(noreplace) %{_sysconfdir}/dillo/keysrc
%config(noreplace) %{_sysconfdir}/dillo/domainrc
%{_mandir}/man1/dillo.1*

