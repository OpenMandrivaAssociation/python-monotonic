%global pypi_name monotonic

Name:           python-%{pypi_name}
Version:        1.6
Release:        1
Group:          Development/Python
Summary:        An implementation of time.monotonic() for Python 2 & < 3.3
License:        ASLv2
URL:            https://github.com/atdt/monotonic
Source0:        https://pypi.io/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)

%description
This module provides a monotonic() function which returns the value (in
fractional seconds) of a clock which never goes backwards.

%files
%license LICENSE
%doc README.md
%{python_sitelib}/*
