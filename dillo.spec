Summary:	Very fast and light web browser
Name:		dillo
Version:	2.0
Release:	%{mkrel 1}
Source0:	http://www.dillo.org/download/%{name}-%{version}.tar.bz2
Source1:	http://www.dillo.org/download/%{name}-%{version}.tar.bz2.asc 
# (cjw) aclocal complains about a line in configure.in that doesn't make sense, so remove the line
#Patch1:		dillo-0.8.6-configure-fix.patch
URL:		http://www.dillo.org/
# The OpenSSL exception is in dpi/https.c - AdamW 2008/12
License:	GPLv3+ with exceptions
Group:		Networking/WWW
BuildRoot:	%{_tmppath}/%{name}-buildroot
Buildrequires:	libjpeg-devel
Buildrequires:	libpng-devel
Buildrequires:	zlib-devel
Buildrequires:	openssl-devel
BuildRequires:	fltk2-devel

%description
Dillo is a Web browser that's completely written in C, very fast, and small in
code base and binary. It is a graphical browser built upon FLTK2 and currently
renders a subset of HTML (no frames, no JavaScript, and no JVM).

%prep
%setup -q

%build
%configure2_5x --disable-dlgui --enable-ipv6

%make
%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 dillorc %{buildroot}%{_sysconfdir}/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Dillo
Comment=A simple web browser
Exec=%{_bindir}/dillo
Icon=networking_www_section
Terminal=false
Type=Application
Categories=Network;WebBrowser;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog* INSTALL NEWS README
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_libdir}/%{name}/
%config(noreplace) %{_sysconfdir}/dillorc
%config(noreplace) %{_sysconfdir}/dpidrc

