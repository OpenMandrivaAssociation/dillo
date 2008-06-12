%define name    dillo
%define version 0.8.6
%define release %mkrel 3

Summary: 	GTK+ based web browser
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	http://www.dillo.org/download/%{name}-%{version}.tar.bz2
Source1:        http://www.dillo.org/download/%{name}-%{version}.tar.bz2.asc 
# (cjw) aclocal complains about a line in configure.in that doesn't make sense, so remove the line
Patch1:		dillo-0.8.6-configure-fix.patch
URL: 		http://www.dillo.org/
License: 	GPL
Group: 		Networking/WWW
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Buildrequires:  libgtk+-devel libjpeg-devel libpng-devel zlib-devel openssl-devel


%description
Dillo is a Web browser that's completely written in C, very fast, and small in
code base and binary (less than 300 kb). It is a graphical browser built upon
GTK+ and currently renders a subset of HTML (no frames, no JavaScript, and 
no JVM).

%prep

%setup -q
%patch1 -p1 -b .subst

%build

aclocal
autoheader
autoconf
automake -a
 
%configure2_5x --disable-dlgui --enable-ipv6

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%_sysconfdir
install -m 644 dillorc $RPM_BUILD_ROOT%_sysconfdir/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Dillo
Comment=A simple web browser
Exec=%{_bindir}/dillo
Icon=networking_www_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Internet-WebBrowsers;Network;WebBrowser;
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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog* INSTALL NEWS README
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_libdir}/%{name}/
%config(noreplace) %_sysconfdir/dillorc
%config(noreplace) %_sysconfdir/dpidrc

