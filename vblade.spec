%define name vblade
%define version 20
%define release %mkrel 2

# (Nanar) TODO: An initscript !!

Summary: Programs to export AoE block device
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tgz
License: GPLv2
Group: System/Kernel and hardware
Url: http://sourceforge.net/projects/aoetools/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
The vblade program (storage target) exports a block device using AoE.

%prep
%setup -q

%build
%make CFLAGS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot{%_sbindir,%_mandir/man8}

install vblade  %buildroot%_sbindir/vblade
install vblade.8 %buildroot%_mandir/man8/vblade.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc HACKING NEWS README
%_sbindir/*
%_mandir/*/*


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 20-2mdv2011.0
+ Revision: 615385
- the mass rebuild of 2010.1 packages

* Mon Nov 16 2009 Olivier Thauvin <nanardon@mandriva.org> 20-1mdv2010.1
+ Revision: 466689
- 20

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 18-2mdv2010.0
+ Revision: 434641
- rebuild

* Mon Aug 04 2008 Funda Wang <fwang@mandriva.org> 18-1mdv2009.0
+ Revision: 262837
- New version 18

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 14-1mdv2008.1
+ Revision: 128872
- kill re-definition of %%buildroot on Pixel's request


* Tue Jan 16 2007 Olivier Thauvin <nanardon@mandriva.org> 14-1mdv2007.0
+ Revision: 109646
- version 14
- Import vblade

* Tue Dec 20 2005 Olivier Thauvin <nanardon@mandriva.org> 10-1mdk
- 10 (the version)

* Wed Nov 30 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 9-1mdk
- Initial mandriva spec

