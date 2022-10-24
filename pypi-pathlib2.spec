#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pathlib2
Version  : 2.3.7.post1
Release  : 33
URL      : https://files.pythonhosted.org/packages/31/51/99caf463dc7c18eb18dad1fffe465a3cf3ee50ac3d1dccbd1781336fe9c7/pathlib2-2.3.7.post1.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/51/99caf463dc7c18eb18dad1fffe465a3cf3ee50ac3d1dccbd1781336fe9c7/pathlib2-2.3.7.post1.tar.gz
Summary  : Object-oriented filesystem paths
Group    : Development/Tools
License  : MIT
Requires: pypi-pathlib2-license = %{version}-%{release}
Requires: pypi-pathlib2-python = %{version}-%{release}
Requires: pypi-pathlib2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(six)

%description
module on bitbucket is no longer maintained.
        The goal of pathlib2 is to provide a backport of

%package license
Summary: license components for the pypi-pathlib2 package.
Group: Default

%description license
license components for the pypi-pathlib2 package.


%package python
Summary: python components for the pypi-pathlib2 package.
Group: Default
Requires: pypi-pathlib2-python3 = %{version}-%{release}

%description python
python components for the pypi-pathlib2 package.


%package python3
Summary: python3 components for the pypi-pathlib2 package.
Group: Default
Requires: python3-core
Provides: pypi(pathlib2)
Requires: pypi(six)

%description python3
python3 components for the pypi-pathlib2 package.


%prep
%setup -q -n pathlib2-2.3.7.post1
cd %{_builddir}/pathlib2-2.3.7.post1
pushd ..
cp -a pathlib2-2.3.7.post1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664316997
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pathlib2
cp %{_builddir}/pathlib2-%{version}/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-pathlib2/10af98b35d719ffba3910fc127caeb2ef386cb9a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pathlib2/10af98b35d719ffba3910fc127caeb2ef386cb9a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
