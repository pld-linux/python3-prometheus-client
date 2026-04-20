#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Python client for the Prometheus monitoring system
Summary(pl.UTF-8):	Pythonowy klient systemu monitorowania Prometheus
Name:		python3-prometheus-client
Version:	0.25.0
Release:	1
License:	Apache v2.0, BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/prometheus-client/
Source0:	https://files.pythonhosted.org/packages/source/p/prometheus-client/prometheus_client-%{version}.tar.gz
# Source0-md5:	a62e0923bbe5b194492acf2e26004e6b
URL:		https://pypi.org/project/prometheus-client/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:77.0.0
%if %{with tests}
BuildRequires:	python3-aiohttp
BuildRequires:	python3-asgiref
BuildRequires:	python3-django
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-benchmark
BuildRequires:	python3-twisted
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The official Python client for Prometheus <https://prometheus.io/>.

%description -l pl.UTF-8
Oficjalny klient Prometheusa <https://prometheus.io/> dla Pythona.

%prep
%setup -q -n prometheus_client-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_benchmark.plugin \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE README.md
%{py3_sitescriptdir}/prometheus_client
%{py3_sitescriptdir}/prometheus_client-%{version}.dist-info
