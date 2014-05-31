# 
# spec file for package libzypp-bindings
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
# 
# nodebuginfo
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           libzypp-bindings
Version:        0.5.10
Release:        1.3
License:        GPLv2+
Summary:        Bindings for libzypp
Group:          Development/Sources
%if 0%{?suse_version}  
Vendor:    openSUSE  
%endif 
Source:         %{name}-%{version}.tar.gz
Patch1:         remove-perl-binding.patch
Patch2:         support-armv7-architectures.patch
Patch3:         meego-add-more-class.patch

BuildRequires:  cmake gcc-c++ python-devel
BuildRequires:  swig == 1.3.40

BuildRequires:  libzypp-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides bindings for libzypp, the library for package management.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} \
      -DPYTHON_SITEDIR=%{python_sitearch} \
      -DLIB=%{_lib} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      ..
make -j1

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{name}-%{version}/LICENSE %{buildroot}/usr/share/license/%{name}

%clean

%package -n python-zypp
Summary:        Python bindings for libzypp
Group:          Development/Languages/Python

Requires:  libzypp

%description -n python-zypp
Python bindings of libzypp

%files -n python-zypp
%defattr(-,root,root,-)
%{python_sitearch}/_zypp.so
%{python_sitearch}/zypp.py*
/usr/share/license/%{name}
