%define name    dillo
%define version 0.8.6
%define release %mkrel 2

Summary: 	GTK+ based web browser
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	http://www.dillo.org/download/%{name}-%{version}.tar.bz2
Source1:        http://www.dillo.org/download/%{name}-%{version}.tar.bz2.asc 
URL: 		http://www.dillo.org/
License: 	GPL
Group: 		Networking/WWW
Buildrequires:  libgtk+-devel libjpeg-devel libpng-devel zlib-devel fltk-devel openssl-devel


%description
Dillo is a Web browser that's completely written in C, very fast, and small in
code base and binary (less than 300 kb). It is a graphical browser built upon
GTK+ and currently renders a subset of HTML (no frames, no JavaScript, and 
no JVM).

%prep

%setup -q
aclocal
autoheader
autoconf
automake -a
 
%configure2_5x --disable-dlgui

%build

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%_sysconfdir
install -m 644 dillorc $RPM_BUILD_ROOT%_sysconfdir/

(cd $RPM_BUILD_ROOT
mkdir -p ./%{_menudir}
cat > ./%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{_bindir}/dillo"\
title="Dillo"\
longtitle="A simple web browser"\
needs="x11"\
icon="networking_www_section.png"\
section="Internet/Web Browsers" \
xdg="true"
EOF

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
)

%post
%{update_menus}

%postun
%{clean_menus}
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog* INSTALL NEWS README
%{_bindir}/*
%{_menudir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_libdir}/%{name}/
%config(noreplace) %_sysconfdir/dillorc
%config(noreplace) %_sysconfdir/dpidrc

