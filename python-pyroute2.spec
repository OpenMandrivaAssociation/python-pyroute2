# Created by pyp2rpm-3.3.5
%global pypi_name pyroute2
%define debug_package %{nil}

Name:           python-%{pypi_name}
Version:        0.5.14
Release:        2
Summary:        Python Netlink library
Group:          Development/Python
License:        dual license GPLv2+ and Apache v2
URL:            https://github.com/svinota/pyroute2
Source0:        %{version}.tar.gz
Patch0:         fix-provides.patch
BuildRequires:  python3-devel
BuildRequires:  (python3dist(psutil) >= 5 with python3dist(psutil) < 6)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(win-inet-pton)

%description
Pyroute2 is a pure Python **netlink** library. The core requires only Python
stdlib, no 3rd party libraries. The library was started as an RTNL protocol
implementation, so the name is **pyroute2**, but now it supports many netlink
protocols. Some supported netlink families and protocols:* **rtnl**, network
settings addresses, routes, traffic controls * **nfnetlink** netfilter API *
**ipq**...

%prep
%setup -n %{pypi_name}-%{version}
#mv README.rst README.md
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%autopatch


%build
%py3_build

%install
%py3_install

#%check
#%{__python3} setup.py test

%files -n python-%{pypi_name}
%license README.license.md LICENSE.Apache.v2 LICENSE.GPL.v2 
%doc README.make.md README.md README.report.md README.rst examples/README.md
%{_bindir}/pyroute2-cli
%{_bindir}/ss2
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/pyroute2-0.5.14-py%{python3_version}.egg-info
