
%define plugin	weather
%define name	vdr-plugin-%plugin
%define version	0.2.1e
%define rel	12

Summary:	VDR plugin: Displays the current weather conditons
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.moldaner.de/vdr/
Source:		http://www.moldaner.de/vdr/download/vdr-%plugin-%version.tar.bz2
# dpatches from e-tobi repository
Patch0:		weather-02_vdr_1.3-fix.dpatch
Patch1:		weather-03_g++4.1-fix.dpatch
Patch2:		weather-04_ftp-location.dpatch
Patch3:		weather-0.2.1e-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	mdsplib-devel
BuildRequires:	ftp-devel
Requires:	vdr-abi = %vdr_abi

%description
Displays the current weather conditions for a selected location.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%vdr_plugin_prep
chmod 0644 HISTORY README

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


