%define plugin	weather

Summary:	VDR plugin: Displays the current weather conditons
Name:		vdr-plugin-%plugin
Version:	0.2.1e
Release:	14
Group:		Video
License:	GPL
URL:		http://www.moldaner.de/vdr/
Source:		http://www.moldaner.de/vdr/download/vdr-%plugin-%{version}.tar.bz2
# dpatches from e-tobi repository
Patch0:		weather-02_vdr_1.3-fix.dpatch
Patch1:		weather-03_g++4.1-fix.dpatch
Patch2:		weather-04_ftp-location.dpatch
Patch3:		weather-0.2.1e-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	mdsplib-devel
BuildRequires:	ftp-devel
Requires:	vdr-abi = %vdr_abi

%description
Displays the current weather conditions for a selected location.

%prep
%setup -q -n %plugin-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%vdr_plugin_prep
chmod 0644 HISTORY README

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY




