
%define plugin	weather
%define name	vdr-plugin-%plugin
%define version	0.2.1e
%define rel	13

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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.2.1e-12mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.2.1e-11mdv2009.1
+ Revision: 359384
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.2.1e-10mdv2009.0
+ Revision: 197998
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.2.1e-9mdv2009.0
+ Revision: 197742
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.2.1e-8mdv2008.1
+ Revision: 145266
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.2.1e-7mdv2008.1
+ Revision: 103247
- rebuild for new vdr

* Fri Jul 20 2007 Anssi Hannula <anssi@mandriva.org> 0.2.1e-6mdv2008.0
+ Revision: 53739
- fix location of NOAA weather ftp server (patch2, from e-tobi)

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.2.1e-5mdv2008.0
+ Revision: 50062
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.2.1e-4mdv2008.0
+ Revision: 42145
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.2.1e-3mdv2008.0
+ Revision: 22722
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1e-2mdv2007.0
+ Revision: 90983
- rebuild for new vdr

* Sat Nov 04 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1e-1mdv2007.1
+ Revision: 76661
- Import vdr-plugin-weather

