# Created by pyp2rpm-3.3.5
%global pypi_name pyroute2
%define debug_package %{nil}

Name:		python-%{pypi_name}
Version:	0.9.5
Release:	2
Summary:	Python Netlink library
Group:		Development/Python
License:	Apache-2.0 OR GPL-2.0-or-later
URL:		https://github.com/svinota/pyroute2
Source0:	https://files.pythonhosted.org/packages/source/p/pyroute2/pyroute2-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(psutil)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

# from v0.7.0 pyroute2 moved to a single source tarball
# obsolete the old modules
Provides:       python-pyroute2.core = %{version}
Obsoletes:      python-pyroute2.core < %{version}
Provides:       python-pyroute2.ethtool = %{version}
Obsoletes:      python-pyroute2.ethtool < %{version}
Provides:       python-pyroute2.ipdb = %{version}
Obsoletes:      python-pyroute2.ipdb < %{version}
Provides:       python-pyroute2.ipset = %{version}
Obsoletes:      python-pyroute2.ipset < %{version}
Provides:       python-pyroute2.ndb = %{version}
Obsoletes:      python-pyroute2.ndb < %{version}
Provides:       python-pyroute2.nftables = %{version}
Obsoletes:      python-pyroute2.nftables < %{version}
Provides:       python-pyroute2.nslink = %{version}
Obsoletes:      python-pyroute2.nslink < %{version}


%description
Pyroute2 is a pure Python **netlink** library. The core requires only Python
stdlib, no 3rd party libraries. The library was started as an RTNL protocol
implementation, so the name is **pyroute2**, but now it supports many netlink
protocols. Some supported netlink families and protocols:* **rtnl**, network
settings addresses, routes, traffic controls * **nfnetlink** netfilter API *
**ipq**...

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files -n python-%{pypi_name}
%doc README.rst
%license README.license.rst LICENSE.Apache-2.0 LICENSE.GPL-2.0-or-later
%{_bindir}/dhcp-server-detector
%{_bindir}/pyroute2-decoder
%{_bindir}/pyroute2-dhcp-client
%{_bindir}/pyroute2-test-platform
%{_bindir}/ss2
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}.dist-info
