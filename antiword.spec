Summary:	MSWord Document to TXT/Postscript converter
Summary(pl):	Konwerter dokumentów MSWord do TXT/Postscript
Name:		antiword
Version:	0.36.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.winfield.demon.nl/linux/%{name}-%{version}.tar.gz
# Source0-md5:	d46107219f4afaee658647a49dc45ed9
Patch0:		%{name}-etc_dir.patch
URL:		http://www.winfield.demon.nl/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Antiword is a free MS-Word reader for Linux, BeOS and RISC OS. It
converts the documents from Word 6, 7, 97 and 2000 to text and
Postscript. Antiword tries to keep the layout of the document intact.

%description -l pl
Antiword to darmowy czytnik dokumentów MS-Word dla Linuksa, BeOS i RISC
OS. Konwertuje on dokumenty z Worda 6, 7, 97 oraz 2000 do tekstu oraz
Postscriptu. Antiword próbuje utrzymaæ formê dokumentu nietkniêt±.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/antiword}

install %{name} k%{name} $RPM_BUILD_ROOT%{_bindir}
install Docs/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install Resources/*	$RPM_BUILD_ROOT%{_datadir}/antiword

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Docs/{ChangeLog,Exmh,FAQ,History,Mutt,Netscape,QandA,ReadMe}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/antiword
%{_mandir}/man*/*
