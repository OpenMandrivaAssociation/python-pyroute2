# Created by pyp2rpm-3.3.5
%global pypi_name pyroute2
%define debug_package %{nil}

Name:           python-%{pypi_name}
Version:        0.6.7
Release:        1
Summary:        Python Netlink library
Group:          Development/Python
License:        dual license GPLv2+ and Apache v2
URL:            https://github.com/svinota/pyroute2
Source0:        https://files.pythonhosted.org/packages/source/p/pyroute2/pyroute2-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/p/pyroute2.core/pyroute2.core-%{version}.tar.gz
Source2:        https://files.pythonhosted.org/packages/source/p/pyroute2.nslink/pyroute2.nslink-%{version}.tar.gz
Source3:        https://files.pythonhosted.org/packages/source/p/pyroute2.nftables/pyroute2.nftables-%{version}.tar.gz
Source4:        https://files.pythonhosted.org/packages/source/p/pyroute2.ethtool/pyroute2.ethtool-%{version}.tar.gz
Source5:        https://files.pythonhosted.org/packages/source/p/pyroute2.ipset/pyroute2.ipset-%{version}.tar.gz
Source6:        https://files.pythonhosted.org/packages/source/p/pyroute2.ipdb/pyroute2.ipdb-%{version}.tar.gz
Source7:        https://files.pythonhosted.org/packages/source/p/pyroute2.ndb/pyroute2.ndb-%{version}.tar.gz
BuildRequires:  python-devel >= 3.0
BuildRequires:  (python3dist(psutil) >= 5 with python3dist(psutil) < 6)
BuildRequires:  python3dist(setuptools)
#BuildRequires:  python3dist(win-inet-pton)

%description
Pyroute2 is a pure Python **netlink** library. The core requires only Python
stdlib, no 3rd party libraries. The library was started as an RTNL protocol
implementation, so the name is **pyroute2**, but now it supports many netlink
protocols. Some supported netlink families and protocols:* **rtnl**, network
settings addresses, routes, traffic controls * **nfnetlink** netfilter API *
**ipq**...

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
tar xf %{S:1}
tar xf %{S:2}
tar xf %{S:3}
tar xf %{S:4}
tar xf %{S:5}
tar xf %{S:6}
tar xf %{S:7}

%build
for i in . pyroute2.core-%{version} pyroute2.nslink-%{version} pyroute2.nftables-%{version} pyroute2.ethtool-%{version} pyroute2.ipset-%{version} pyroute2.ipdb-%{version} pyroute2.ndb-%{version}; do
	cd $i
	%py3_build
	cd -
done

%install
for i in . pyroute2.core-%{version} pyroute2.nslink-%{version} pyroute2.nftables-%{version} pyroute2.ethtool-%{version} pyroute2.ipset-%{version} pyroute2.ipdb-%{version} pyroute2.ndb-%{version}; do
	cd $i
	%py3_install
	cd -
done

#%%check
#%%{__python3} setup.py test

%files -n python-%{pypi_name}
%license README.license.md LICENSE.Apache.v2 LICENSE.GPL.v2 
%{_bindir}/ss2
%{_bindir}/pyroute2-cli
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info
%{python3_sitelib}/pr2modules
%{python3_sitelib}/*.pth
