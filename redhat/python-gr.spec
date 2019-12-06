%define debug_package %{nil}

%if 0%{?centos_version} >= 800
%bcond_without py3
%else
%bcond_with py3
%endif

%if 0%{?centos_version} >= 800
%define py2 python2
%else
%define py2 python
%endif

%if 0%{?__jcns}
%define fixedversion %{version}
Name:          python-gr-local
%else
# use fixedversion for builds on build.opensuse.org - needed for deb builds.
%define fixedversion fixed
%define compression gz
Name:          python-gr
%endif

Summary:       GR, a universal framework for visualization applications
Version:       1.12.0
Release:       2%{?dist}
License:       MIT
Group:         Development/Libraries
Source:        python-gr-%{fixedversion}.tar%{?compression:.%{compression}}
# for vcversioner
BuildRequires: git
BuildRequires: gr
Requires:      gr

# wxWidgets BuildRequires / Requires
%if 0%{?suse_version}
BuildRequires: libwx_baseu-2_8-0-stl
BuildRequires: libwx_gtk2u_core-2_8-0-stl
BuildRequires: libwx_baseu-2_8-0-compat-lib-stl
BuildRequires: libwx_gtk2u_core-2_8-0-compat-lib-stl
BuildRequires: wxWidgets-devel
%endif

%if 0%{?__jcns}
BuildRequires: python-local
BuildRequires: python-setuptools-local
Requires:      python-local
Requires:      numpy-local
%else
BuildRequires: %{py2}-devel
BuildRequires: %{py2}-setuptools
Requires:      python
Requires:      numpy
%endif

%if %{with py3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif

%description
GR, a universal framework for visualization applications

%prep
%setup -n python-gr-%{fixedversion}

%build
%py2_build
%if %{with py3}
%py3_build
%endif

%install
%py2_install
%if %{with py3}
%py3_install
%endif

%files
%defattr(-,root,root)
%{python2_sitelib}/gr-*.egg-info
%{python2_sitelib}/gr
%{python2_sitelib}/gr3
%{python2_sitelib}/qtgr

# Python 3 version...

%if %{with py3}

%package -n python3-gr
Summary:       GR, a universal framework for visualization applications (Python 3 bindings)
Requires:      python3
Requires:      python3-numpy

%description -n python3-gr
%{summary}

%files -n python3-gr
%{python3_sitelib}/gr-*.egg-info
%{python3_sitelib}/gr
%{python3_sitelib}/gr3
%{python3_sitelib}/qtgr

%endif
