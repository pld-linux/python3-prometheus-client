#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-prometheus-client.spec)

Summary:	Python client for the Prometheus monitoring system
Summary(pl.UTF-8):	Pythonowy klient systemu monitorowania Prometheus
Name:		python-prometheus-client
# keep 0.12.x here for python2 support
Version:	0.12.0
Release:	1
License:	Apache v2.0, BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/prometheus-client/
Source0:	https://files.pythonhosted.org/packages/source/p/prometheus-client/prometheus_client-%{version}.tar.gz
# Source0-md5:	4439c954aa7bc68b15915c6360967851
URL:		https://pypi.org/project/prometheus-client/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-twisted
BuildRequires:	python-unittest2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-asgiref
BuildRequires:	python3-pytest
BuildRequires:	python3-twisted
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The official Python 2 and 3 client for Prometheus
<http://prometheus.io/>.

%description -l pl.UTF-8
Oficjalny klient Prometheusa <http://prometheus.io/> dla Pythona 2 i
3.

%package -n python3-prometheus-client
Summary:	Python client for the Prometheus monitoring system
Summary(pl.UTF-8):	Pythonowy klient systemu monitorowania Prometheus
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-prometheus-client
The official Python 2 and 3 client for Prometheus
<http://prometheus.io/>.

%description -n python3-prometheus-client -l pl.UTF-8
Oficjalny klient Prometheusa <http://prometheus.io/> dla Pythona 2 i
3.

%prep
%setup -q -n prometheus_client-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/prometheus_client
%{py_sitescriptdir}/prometheus_client-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-prometheus-client
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/prometheus_client
%{py3_sitescriptdir}/prometheus_client-%{version}-py*.egg-info
%endif
