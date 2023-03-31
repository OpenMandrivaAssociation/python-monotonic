%global pypi_name monotonic

Name:           python-%{pypi_name}
Version:        1.5
Release:        2
Group:          Development/Python
Summary:        An implementation of time.monotonic() for Python 2 & < 3.3
License:        ASLv2
URL:            https://github.com/atdt/monotonic
Source0:        http://pypi.io/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python-%{pypi_name}}

%description
This module provides a monotonic() function which returns the value (in
fractional seconds) of a clock which never goes backwards.

%prep
%setup -q -n %{pypi_name}-%{version}
%autopatch -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.md
%{python_sitelib}/*
