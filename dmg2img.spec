Summary:	Tool to convert Apple's compressed DMG to standard (hfsplus) disk image file
Summary(pl.UTF-8):	Narzędzie konwertujące skompresowane pliki Apple DMG na obrazy dysków (hfsplus)
Name:		dmg2img
Version:	1.6.5
Release:	1
License:	GPL v2
Group:		Applications/File
Source0:	http://vu1tur.eu.org/tools/%{name}-%{version}.tar.gz
# Source0-md5:	d01b01151759dd25e16d0c37d4a57b3c
URL:		http://vu1tur.eu.org/tools/
BuildRequires:	bzip2-devel
BuildRequires:	openssl-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dmg2img is an Apple's compressed DMG to standard (hfsplus) image disk
file convert tool.

%description -l pl.UTF-8
dwg2img to konwerter skompresowanych plików Apple DMG na standardowe
pliki obrazów dysków (hfsplus).

%prep
%setup -q

%{__sed} -i -e '/CC/s/-s /$(LDFLAGS)/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

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
