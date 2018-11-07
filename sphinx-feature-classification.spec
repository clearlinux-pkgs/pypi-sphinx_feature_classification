#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinx-feature-classification
Version  : 0.3.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/d9/8f/62b2c783bb6647b08085c546c86280a663601d3b87ac1bb67c5ee8642d2e/sphinx-feature-classification-0.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d9/8f/62b2c783bb6647b08085c546c86280a663601d3b87ac1bb67c5ee8642d2e/sphinx-feature-classification-0.3.1.tar.gz
Summary  : Generate a matrix of pluggable drivers and their support to an API in Sphinx.
Group    : Development/Tools
License  : Apache-2.0
Requires: sphinx-feature-classification-license = %{version}-%{release}
Requires: sphinx-feature-classification-python = %{version}-%{release}
Requires: sphinx-feature-classification-python3 = %{version}-%{release}
Requires: docutils
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : ddt
BuildRequires : oslotest
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : testrepository
BuildRequires : testtools
BuildRequires : tox
BuildRequires : virtualenv

%description
Team and repository tags
        ========================

%package license
Summary: license components for the sphinx-feature-classification package.
Group: Default

%description license
license components for the sphinx-feature-classification package.


%package python
Summary: python components for the sphinx-feature-classification package.
Group: Default
Requires: sphinx-feature-classification-python3 = %{version}-%{release}

%description python
python components for the sphinx-feature-classification package.


%package python3
Summary: python3 components for the sphinx-feature-classification package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sphinx-feature-classification package.


%prep
%setup -q -n sphinx-feature-classification-0.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541606064
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinx-feature-classification
cp LICENSE %{buildroot}/usr/share/package-licenses/sphinx-feature-classification/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinx-feature-classification/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
