#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	libnet
Summary:	Miscellaneous perl networking modules
Summary(cs.UTF-8):	Modul libnet pro Perl
Summary(da.UTF-8):	Perl-modulet libnet
Summary(de.UTF-8):	libnet Perl Modul
Summary(es.UTF-8):	Módulo de Perl libnet
Summary(fr.UTF-8):	Module Perl libnet
Summary(it.UTF-8):	Modulo di Perl libnet
Summary(ja.UTF-8):	libnet Perl モジュール
Summary(ko.UTF-8):	libnet 펄 모줄
Summary(nb.UTF-8):	Perlmodul libnet
Summary(pl.UTF-8):	Różne moduły perlowe do obsługi sieci
Summary(pt.UTF-8):	Módulo de Perl libnet
Summary(pt_BR.UTF-8):	Módulo Perl libnet
Summary(ru.UTF-8):	Модуль для Perl libnet
Summary(sv.UTF-8):	libnet Perlmodul
Summary(uk.UTF-8):	Модуль для Perl libnet
Summary(zh_CN.UTF-8):	libnet Perl 模块
Name:		perl-libnet
Version:	1.22
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pnam}-%{version}.tar.gz
# Source0-md5:	ac82f4ea57113dabcce4b65d540a7a3a
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

%description -l pl.UTF-8
libnet jest zestawem modułów do Perla, które udostępniają prosty i
spójny interfejs programisty (API) do obsługi po stronie klienta
różnych protokołów używanych w sieci Internet. Spis dokumentów RFC,
które są zaimplementowane w libnet:

- Net::FTP - RFC959 File Transfer Protocol
- Net::SMTP - RFC821 Simple Mail Transfer Protocol
- Net::Time - RFC867 Daytime Protocol
- Net::Time - RFC868 Time Protocol
- Net::NNTP - RFC977 Network News Transfer Protocol
- Net::POP3 - RFC1939 Post Office Protocol 3
- Net::SNPP - RFC1861 Simple Network Pager Protocol

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

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
