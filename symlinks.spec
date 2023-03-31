Summary:	A utility which maintains a system's symbolic links
Name:		symlinks
Version:	1.4
Release:	14
Group:		File tools
License:	BSD-style
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/file/%{name}-%{version}.tar.gz
URL:		http://www.ibiblio.org/pub/Linux/utils/file/
Patch0:		symlinks-1.4-noroot.patch
Patch2:		symlinks-1.4-short.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The symlinks utility performs maintenance on symbolic links.  Symlinks
checks for symlink problems, including dangling symlinks which point to
nonexistent files.  Symlinks can also automatically convert absolute
symlinks to relative symlinks.

Install the symlinks package if you need a program for maintaining
symlinks on your system.

%prep
%setup -q
%patch0 -p1 -b .noroot~
%patch2 -p1 -b .short~

%build
%make CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" 

%install
rm -rf %{buildroot}

install -D %{name} %{buildroot}%{_bindir}/%{name}
install -D %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-4mdv2011.0
+ Revision: 670255
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-3mdv2011.0
+ Revision: 607761
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-2mdv2010.1
+ Revision: 520244
- rebuilt for 2010.1

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - drop buildrequires on glibc-static-devel as we no longer do static linking
    - regenerate short patch (P2)
    - drop static patch (P1) as it's no longer needed
    - regenerate noroot patch (P0)
    - new release: 1.5

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2-23mdv2010.0
+ Revision: 427220
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1.2-22mdv2009.1
+ Revision: 366310
- rediff noroot patch

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - fix issue with >2GB files (fixes #41900)
    - fix issue with symlinks converted from absolute to relative aren't shortened
      (P2, RHBZ #89655)
    - compile with correct flags to enable large files support (#41900)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2-20mdv2009.0
+ Revision: 225548
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2-19mdv2008.1
+ Revision: 179567
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2-18mdv2007.0
+ Revision: 119974
- Import symlinks

* Sat Apr 29 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2-17mdk
- rebuild
- %%mkrel
- pass $RPM_OPT_FLAGS to CFLAGS variable in stead of changing it with perl
- fix summary-ended-with-dot

* Tue Oct 05 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2-16mdk
- fix static build

