#
# Conditional build:
# _without_tests - do not perform "make test"
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
Summary(no):	Perlmodul libnet
Summary(pl):	Ró¿ne modu³y perlowe do obs³ugi sieci
Summary(pt):	Módulo de Perl libnet
Summary(pt_BR):	Módulo Perl libnet
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl libnet
Summary(sv):	libnet Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl libnet
Summary(zh_CN):	libnet Perl Ä£¿é
Name:		perl-libnet
Version:	1.12
Release:	3
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		%{name}-Configure.patch
URL:		http://www.perl.com/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.readme
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
libnet jest zestawem modu³ów do perla, które udostêpniaj± prosty i
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
perl Makefile.PL </dev/null

%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
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
