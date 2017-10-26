Name:           ros-lunar-roslang
Version:        1.14.2
Release:        0%{?dist}
Summary:        ROS roslang package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roslang
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-catkin
Requires:       ros-lunar-genmsg
BuildRequires:  ros-lunar-catkin

%description
roslang is a common package that all ROS client libraries depend on. This is
mainly used to find client libraries (via 'rospack depends-on1 roslang').

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Oct 26 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.2-0
- Autogenerated by Bloom

* Thu Jul 27 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.1-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.0-0
- Autogenerated by Bloom

