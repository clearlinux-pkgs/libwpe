#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x91C559DBE4C9123B (aperez@igalia.com)
#
Name     : libwpe
Version  : 1.14.1
Release  : 1
URL      : https://github.com/WebPlatformForEmbedded/libwpe/releases/download/1.14.1/libwpe-1.14.1.tar.xz
Source0  : https://github.com/WebPlatformForEmbedded/libwpe/releases/download/1.14.1/libwpe-1.14.1.tar.xz
Source1  : https://github.com/WebPlatformForEmbedded/libwpe/releases/download/1.14.1/libwpe-1.14.1.tar.xz.asc
Summary  : The wpe library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: libwpe-lib = %{version}-%{release}
Requires: libwpe-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : pkg-config
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(xkbcommon)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the libwpe package.
Group: Development
Requires: libwpe-lib = %{version}-%{release}
Provides: libwpe-devel = %{version}-%{release}
Requires: libwpe = %{version}-%{release}

%description dev
dev components for the libwpe package.


%package lib
Summary: lib components for the libwpe package.
Group: Libraries
Requires: libwpe-license = %{version}-%{release}

%description lib
lib components for the libwpe package.


%package license
Summary: license components for the libwpe package.
Group: Default

%description license
license components for the libwpe package.


%prep
%setup -q -n libwpe-1.14.1
cd %{_builddir}/libwpe-1.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679075395
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1679075395
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libwpe
cp %{_builddir}/libwpe-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libwpe/36aa4395241156d28aa853670fc7f94b206474b0 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/wpe-1.0/wpe/export.h
/usr/include/wpe-1.0/wpe/gamepad.h
/usr/include/wpe-1.0/wpe/input-xkb.h
/usr/include/wpe-1.0/wpe/input.h
/usr/include/wpe-1.0/wpe/keysyms.h
/usr/include/wpe-1.0/wpe/libwpe-version.h
/usr/include/wpe-1.0/wpe/loader.h
/usr/include/wpe-1.0/wpe/pasteboard.h
/usr/include/wpe-1.0/wpe/process.h
/usr/include/wpe-1.0/wpe/renderer-backend-egl.h
/usr/include/wpe-1.0/wpe/renderer-host.h
/usr/include/wpe-1.0/wpe/version-deprecated.h
/usr/include/wpe-1.0/wpe/version.h
/usr/include/wpe-1.0/wpe/view-backend.h
/usr/include/wpe-1.0/wpe/wpe-egl.h
/usr/include/wpe-1.0/wpe/wpe.h
/usr/lib64/libwpe-1.0.so
/usr/lib64/pkgconfig/wpe-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwpe-1.0.so.1
/usr/lib64/libwpe-1.0.so.1.8.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libwpe/36aa4395241156d28aa853670fc7f94b206474b0
