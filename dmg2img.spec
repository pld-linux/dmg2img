Summary:	Tool to convert Apple's compressed DMG to standard (hfsplus) disk image file
Summary(pl.UTF-8):	Narzędzie konwertujące skomplesowane pliki Apple DMG na obrazy dysków (hfsplus)
Name:		dmg2img
Version:	0.3a
Release:	1
License:	GPL v2
Group:		Applications/File
Source0:	http://vu1tur.eu.org/tools/download.pl?dmg2img.tar.gz
# Source0-md5:	e3fa1bc5f38e961230100c1c2274bd28
URL:		http://vu1tur.eu.org/tools/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dmg2img is an Apple's compressed DMG to standard (hfsplus) image disk file
convert tool.

%description -l pl.UTF-8
dwg2img to konwerter skompresowanych plików Apple DMG na standardowe
pliki obrazów dysków (hfsplus).

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D dmg2img $RPM_BUILD_ROOT%{_bindir}/dmg2img

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dmg2img
