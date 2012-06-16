Summary:	Tool to convert Apple's compressed DMG to standard (hfsplus) disk image file
Summary(pl.UTF-8):	Narzędzie konwertujące skomplesowane pliki Apple DMG na obrazy dysków (hfsplus)
Name:		dmg2img
Version:	1.6.4
Release:	1
License:	GPL v2
Group:		Applications/File
Source0:	http://vu1tur.eu.org/tools/dmg2img-1.6.4.tar.gz
# Source0-md5:	3861da66bf0d2f7407aeeec93f9cfc5e
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
install -p dmg2img $RPM_BUILD_ROOT%{_bindir}
install -p vfdecrypt $RPM_BUILD_ROOT%{_bindir}
cp -p vfdecrypt.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dmg2img
%attr(755,root,root) %{_bindir}/vfdecrypt
%{_mandir}/man1/vfdecrypt.1*
