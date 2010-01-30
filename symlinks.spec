Summary:	A utility which maintains a system's symbolic links
Name:		symlinks
Version:	1.4
Release:	%mkrel 1
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
%patch0 -p1 -b .noroot
%patch2 -p1 -b .short

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
