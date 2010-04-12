Summary:	Tool to convert Apple's compressed DMG to standard (hfsplus) disk image file
Summary(pl.UTF-8):	Narzędzie konwertujące skomplesowane pliki Apple DMG na obrazy dysków (hfsplus)
Name:		dmg2img
Version:	1.6
Release:	2
License:	GPL v2
Group:		Applications/File
# http://vu1tur.eu.org/tools/download.pl?dmg2img-1.6.tar.gz
Source0:	dmg2img-1.6.tar.gz
# Source0-md5:	532f5096f0a38349afc5738f1fa0a9d3
URL:		http://vu1tur.eu.org/tools/
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dmg2img is an Apple's compressed DMG to standard (hfsplus) image disk file
convert tool.

%description -l pl.UTF-8
dwg2img to konwerter skompresowanych plików Apple DMG na standardowe
pliki obrazów dysków (hfsplus).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dmg2img $RPM_BUILD_ROOT%{_bindir}
install vfdecrypt $RPM_BUILD_ROOT%{_bindir}
install vfdecrypt.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dmg2img
%attr(755,root,root) %{_bindir}/vfdecrypt
%{_mandir}/man1/vfdecrypt.1*
