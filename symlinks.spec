Summary:	A utility which maintains a system's symbolic links
Name:		symlinks
Version:	1.2
Release:	%mkrel 18
Group:		File tools
License:	BSD-style
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/file/%{name}-%{version}.tar.bz2
URL:		http://www.ibiblio.org/pub/Linux/utils/file/
Patch0:		%{name}-1.2-noroot.patch
Patch1:		%{name}-1.2-static.patch
Buildrequires:	glibc-static-devel
Buildroot:	%{_tmppath}/%{name}-%{version}--buildroot

%description
The symlinks utility performs maintenance on symbolic links.  Symlinks
checks for symlink problems, including dangling symlinks which point to
nonexistent files.  Symlinks can also automatically convert absolute
symlinks to relative symlinks.

Install the symlinks package if you need a program for maintaining
symlinks on your system.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .static

%build
%make CFLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -D %{name} %{buildroot}%{_bindir}/%{name}
install -D %{name}.8  %{buildroot}%{_mandir}/man8/%{name}.8

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


