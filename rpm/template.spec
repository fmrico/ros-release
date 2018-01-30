Name:           ros-melodic-mk
Version:        1.14.3
Release:        0%{?dist}
Summary:        ROS mk package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ROS
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-rosbuild
BuildRequires:  ros-melodic-catkin >= 0.5.69

%description
A collection of .mk include files for building ROS architectural elements. Most
package authors should use cmake .mk, which calls CMake for the build of the
package. The other files in this package are intended for use in exotic
situations that mostly arise when importing 3rdparty code.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Jan 30 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.3-0
- Autogenerated by Bloom

