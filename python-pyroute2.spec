%define module	pyroute2
  
Summary:	Python netlink library — Linux network setup and monitoring
Name:		python-pyroute2
Version:	0.5.9
Release:	1
Group:		Development/Python
License:	Python
Url:		https://pypi.python.org/pypi/pyroute2
Source0:	https://github.com/svinota/pyroute2/archive/%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
 
%description 
Pyroute2 is a pure Python netlink library. It requires only Python stdlib,
no 3rd party libraries. The library was started as an RTNL protocol
implementation, so the name is pyroute2, but now it supports many netlink
protocols.

%prep
%setup -qn %{module}-%{version}
%autopatch -p1

%build
%__python setup.py build
  
%install 
%__python setup.py install --root=%{buildroot}

%files
%{_bindir}/pyroute2-cli
%{_bindir}/ss2
%{py_sitedir}/pyroute2*.egg-info
%{py_sitedir}/pyroute2
