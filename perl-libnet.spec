#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	libnet
Summary:	Miscellaneous perl networking modules
Summary(cs):	Modul libnet pro Perl
Summary(da):	Perl-modulet libnet
Summary(de):	libnet Perl Modul
Summary(es):	Módulo de Perl libnet
Summary(fr):	Module Perl libnet
Summary(it):	Modulo di Perl libnet
Summary(ja):	libnet Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	libnet ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul libnet
Summary(pl):	Ró¿ne modu³y perlowe do obs³ugi sieci
Summary(pt):	Módulo de Perl libnet
Summary(pt_BR):	Módulo Perl libnet
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl libnet
Summary(sv):	libnet Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl libnet
Summary(zh_CN):	libnet Perl Ä£¿é
Name:		perl-libnet
Version:	1.19
Release:	2
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	e6533ef83a2497562418a2239bb44602
Patch0:		%{name}-Configure.patch
URL:		http://www.perl.com/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.readme
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Convert::EBCDIC required only on os390
# Authen::SASL and MIME::Base64 required only for SMTP AUTH
%define		_noautoreq	'perl(Convert::EBCDIC)' 'perl(Authen::SASL)' 'perl(MIME::Base64)'

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

%description -l pl
libnet jest zestawem modu³ów do Perla, które udostêpniaj± prosty i
spójny interfejs programisty (API) do obs³ugi po stronie klienta
ró¿nych protoko³ów u¿ywanych w sieci Internet. Spis dokumentów RFC,
które s± zaimplementowane w libnet:

- Net::FTP - RFC959 File Transfer Protocol
- Net::SMTP - RFC821 Simple Mail Transfer Protocol
- Net::Time - RFC867 Daytime Protocol
- Net::Time - RFC868 Time Protocol
- Net::NNTP - RFC977 Network News Transfer Protocol
- Net::POP3 - RFC1939 Post Office Protocol 3
- Net::SNPP - RFC1861 Simple Network Pager Protocol

%prep
%setup -q -n %{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%config(noreplace) %{perl_vendorlib}/Net/Config.pm
%{perl_vendorlib}/Net/Cmd.pm
%{perl_vendorlib}/Net/Domain.pm
%dir %{perl_vendorlib}/Net/FTP
%{perl_vendorlib}/Net/FTP/A.pm
%{perl_vendorlib}/Net/FTP/dataconn.pm
%{perl_vendorlib}/Net/FTP/E.pm
%{perl_vendorlib}/Net/FTP/I.pm
%{perl_vendorlib}/Net/FTP/L.pm
%{perl_vendorlib}/Net/FTP.pm
%{perl_vendorlib}/Net/libnet.cfg
%{perl_vendorlib}/Net/NNTP.pm
%{perl_vendorlib}/Net/POP3.pm
%{perl_vendorlib}/Net/Netrc.pm
%{perl_vendorlib}/Net/SMTP.pm
%{perl_vendorlib}/Net/Time.pm
%{_mandir}/man3/*
