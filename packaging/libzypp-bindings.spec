# 
# spec file for package libzypp-bindings
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
# 
Name:           libzypp-bindings
Version:        0.6.1
Release:        0
License:        GPL-2.0+
Summary:        Bindings for libzypp
Group:          Development/Sources
Source:         %{name}-%{version}.tar.gz
Source1001: 	libzypp-bindings.manifest

BuildRequires:  cmake gcc-c++ python-devel
BuildRequires:  swig

BuildRequires:  libzypp-devel

%description
This package provides bindings for libzypp, the library for package management.

%prep
%setup -q
cp %{SOURCE1001} .

%build
mkdir build
cd build
%cmake -DCMAKE_INSTALL_PREFIX=%{prefix} \
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

%clean

%package -n python-zypp
Summary:        Python bindings for libzypp
Group:          Development/Languages/Python
Requires:  libzypp

%description -n python-zypp
Python bindings of libzypp


%files -n python-zypp
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{python_sitearch}/_zypp.so
%{python_sitearch}/zypp.py*
