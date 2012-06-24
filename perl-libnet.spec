%include	/usr/lib/rpm/macros.perl
Summary:	Miscellaneous perl networking modules
Summary(pl):	R�ne modu�y perlowe do obs�ugi sieci
Name:		perl-libnet
Version:	1.0901
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/libnet-%{version}.tar.gz
Patch0:		%{name}-Configure.patch
URL:		http://www.perl.com/CPAN/modules/by-module/Net/libnet-%{version}.readme
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# required only on os390
%define		_noautoreq	'perl(Convert::EBCDIC)'

%description
libnet is a collection of Perl modules which provides a simple and
consistent programming interface (API) to the client side of various
protocols used in the internet community. The RFCs implemented in this
distribution are:

- Net::FTP - RFC959 File Transfer Protocol
- Net::SMTP - RFC821 Simple Mail Transfer Protocol
- Net::Time - RFC867 Daytime Protocol
- Net::Time - RFC868 Time Protocol
- Net::NNTP - RFC977 Network News Transfer Protocol
- Net::POP3 - RFC1939 Post Office Protocol 3
- Net::SNPP - RFC1861 Simple Network Pager Protocol

The distribution also contains a module (Net::PH) which facilitates
comunicate with with servers using the CCSO Nameserver Server-Client
Protocol

%description -l pl
libnet jest zestawem modu��w do perla, kt�re udost�pniaj� prosty i
sp�jny interfejs programisty (API) do obs�ugi po stronie klienta
r�nych protoko��w u�uwanych w sieci Internet. Spis dokument�w RFS,
kt�re s� zaimplementowane w libnet:

- Net::FTP - RFC959 File Transfer Protocol
- Net::SMTP - RFC821 Simple Mail Transfer Protocol
- Net::Time - RFC867 Daytime Protocol
- Net::Time - RFC868 Time Protocol
- Net::NNTP - RFC977 Network News Transfer Protocol
- Net::POP3 - RFC1939 Post Office Protocol 3
- Net::SNPP - RFC1861 Simple Network Pager Protocol

Dystrybucja libnet zawiera tak�e modu� (Net::PH), kt�ry umo�liwia
komunikacj� z serwerami CCSO Nameserver Server-Client Protocol.

%prep
%setup -q -n libnet-%{version}
%patch -p1

%build
yes "" | perl Makefile.PL 

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %{perl_sitelib}/Net/Config.pm
%{perl_sitelib}/Net/Cmd.pm
%{perl_sitelib}/Net/Domain.pm
%dir %{perl_sitelib}/Net/FTP
%{perl_sitelib}/Net/FTP/A.pm
%{perl_sitelib}/Net/FTP/dataconn.pm
%{perl_sitelib}/Net/FTP/E.pm
%{perl_sitelib}/Net/FTP/I.pm
%{perl_sitelib}/Net/FTP/L.pm
%{perl_sitelib}/Net/FTP.pm
%{perl_sitelib}/Net/libnet.cfg
%{perl_sitelib}/Net/libnetFAQ.pod
%{perl_sitelib}/Net/NNTP.pm
%{perl_sitelib}/Net/POP3.pm
%{perl_sitelib}/Net/Netrc.pm
%{perl_sitelib}/Net/SMTP.pm
%{perl_sitelib}/Net/Time.pm
%{_mandir}/man3/*
