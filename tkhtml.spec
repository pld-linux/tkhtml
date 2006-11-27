%define		_rel	0.2
Summary:	tkhtml
Name:		tkhtml
Version:	3.0
Release:	0.alpha13.%{_rel}
License:	BSD-like
Group:		Applications/WWW
Source0:	http://tkhtml.tcl.tk/%{name}3-alpha-13.tar.gz
# Source0-md5:	64218a74ad2f4dafaa57597ba2d4e9b7
Patch0:		%{name}-paths.patch
URL:		http://tkhtml.tcl.tk/
BuildRequires:	autoconf
BuildRequires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Tkhtml" is a Tcl/Tk widget that displays HTML. Tkhtml is implemented
in C. It is a true widget, not a metawidget implemented using the Text
or Canvas widgets of the Tcl/Tk core.

%package -n hv3
Summary:	Html Viewer 3 - Tkhtml3 Web Browser
Group:		Applications/WWW
URL:		http://tkhtml.tcl.tk/hv3.html
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/wish

%description -n hv3
Html Viewer 3 (hv3) is a minimalist web browser that uses Tkhtml.

Hv3 is not yet as sophisticated as some popular web browsers. Most
notably, it does not support either javascript or plugins (although it
can run most "tclets" created for the tcl plugin). It does support the
following:

- Formatting of regular HTML/CSS documents,
- HTML Frameset documents,
- HTML forms,
- HTTP cookies,
- HTTP "Location" and "Refresh" headers.

%prep
%setup -q -n htmlwidget
%patch0 -p1

%build
%{__aclocal} -I tclconfig
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/hv3,%{_bindir}}
cp -a hv/*.tcl $RPM_BUILD_ROOT%{_datadir}/hv3
cp -a hv/index.html $RPM_BUILD_ROOT%{_datadir}/hv3
cat <<'EOF' > $RPM_BUILD_ROOT%{_bindir}/hv3
#!/bin/sh
exec %{_bindir}/wish %{_datadir}/hv3/hv3_main.tcl
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYRIGHT
%dir %{_libdir}/Tkhtml3.0
%{_libdir}/Tkhtml3.0/libTkhtml3.0.so
%{_libdir}/Tkhtml3.0/pkgIndex.tcl
%{_mandir}/mann/tkhtml.n*

%files -n hv3
%defattr(644,root,root,755)
%doc hv/README hv/license.txt
%attr(755,root,root) %{_bindir}/hv3
%{_datadir}/hv3