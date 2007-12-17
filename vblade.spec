%define name vblade
%define version 14
%define release %mkrel 1

# (Nanar) TODO: An initscript !!

Summary: Programs to export AoE block device
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL 
Group: System/Kernel and hardware
Url: http://sourceforge.net/projects/aoetools/

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


