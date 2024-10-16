%global  kf_version 6.6.0

Name:		kf6-kitemviews
Version: 6.6.0
Release:	0%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with item views
License:	CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:		https://invent.kde.org/frameworks/kitemviews
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:	fdupes
BuildRequires:	cmake
BuildRequires:	clang
BuildRequires:	kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	pkgconfig(xkbcommon)

%description
KDE Frameworks 6 Tier 1 addon with item views.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kitemviews6_qt
%fdupes LICENSES

%files -f kitemviews6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6ItemViews.so.*

%files devel
%{_kf6_includedir}/KItemViews/
%{_kf6_libdir}/libKF6ItemViews.so
%{_kf6_libdir}/cmake/KF6ItemViews/
%{_kf6_qtplugindir}/designer/kitemviews6widgets.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
