#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinx-feature-classification
Version  : 1.0.1
Release  : 18
URL      : https://files.pythonhosted.org/packages/ad/7f/1aa3846c501a1cfc307b26a29720aa184ceee17788696f3181091b69b994/sphinx-feature-classification-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/7f/1aa3846c501a1cfc307b26a29720aa184ceee17788696f3181091b69b994/sphinx-feature-classification-1.0.1.tar.gz
Summary  : Generate a matrix of pluggable drivers and their support to an API in Sphinx.
Group    : Development/Tools
License  : Apache-2.0
Requires: sphinx-feature-classification-license = %{version}-%{release}
Requires: sphinx-feature-classification-python = %{version}-%{release}
Requires: sphinx-feature-classification-python3 = %{version}-%{release}
Requires: docutils
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : pbr

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/sphinx-feature-classification.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

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
Provides: pypi(sphinx_feature_classification)
Requires: pypi(docutils)
Requires: pypi(pbr)

%description python3
python3 components for the sphinx-feature-classification package.


%prep
%setup -q -n sphinx-feature-classification-1.0.1
cd %{_builddir}/sphinx-feature-classification-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586278303
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinx-feature-classification
cp %{_builddir}/sphinx-feature-classification-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/sphinx-feature-classification/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinx-feature-classification/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
