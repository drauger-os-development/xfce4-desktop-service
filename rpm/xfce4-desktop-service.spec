Name:           xfce4-desktop-service
Version:        0.2.6
Release:        1%{?dist}
Summary:        File Manager Service stand-in for Xfce

License:        GPL-2.0-or-later
URL:            https://github.com/drauger-os-development/xfce4-desktop-service
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Python dependencies
## Cf. https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/
Requires:       python%{python3_version}dist(dbus-python)
Requires:       python%{python3_version}dist(python-magic)
Requires:       python%{python3_version}dist(urllib3)
%if 0%{?suse_version}
# SUSE distributions split out gobject-introspection files
Requires:       typelib(Gtk) = 3.0
%endif
Requires:       gtk3 >= 3.24.5
Requires:       xfdesktop
# We use gio for things, so require it
Requires:       /usr/bin/gio
Requires:       xdg-utils
# We can't have Thunar on the system at the same time
Conflicts:      thunar

BuildArch:      noarch

%description
This package provides a file manager service for Xfce, in a way that
does not require Thunar to be installed. This way, users can use whatever
file manager they prefer with Xfce.

This package is a third-party package and is not maintained by the Xfce developers.


%prep
%autosetup


%build
# Nothing to build


%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}
cp -a etc %{buildroot}


%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_sysconfdir}/xdg/autostart/xfce4-desktop-service.desktop


%changelog
* Sun Jan 30 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.2.6-1
- Initial packaging
