%include	/usr/lib/rpm/macros.perl
Summary:	Miscellaneous perl networking modules
Summary(pl):	Ró¿ne modu³y perlowe do obs³ugi sieci
Name:		perl-libnet
Version:	1.0703
Release:	2
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
License:	GPL
URL:		http://www.perl.com/CPAN//modules/by-module/Net/libnet-%{version}.readme
Source0:	ftp://ftp.digital.com/pub/plan/perl/CPAN/modules/by-module/Net/libnet-%{version}.tar.gz
Patch0:		%{name}-Configure.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
libnet jest zestawem modu³ów do perla, które udostêpniaj± prosty i
spójny interfejs programisty (API) do obs³ugi po stronie klienta
ró¿nych protoko³ów u¿uwanych w sieci Internet. Spis dokumentów RFS,
które s± zaimplementowane w libnet:

- Net::FTP - RFC959 File Transfer Protocol
- Net::SMTP - RFC821 Simple Mail Transfer Protocol
- Net::Time - RFC867 Daytime Protocol
- Net::Time - RFC868 Time Protocol
- Net::NNTP - RFC977 Network News Transfer Protocol
- Net::POP3 - RFC1939 Post Office Protocol 3
- Net::SNPP - RFC1861 Simple Network Pager Protocol

Dystrybucja libnet zawiera tak¿e modu³ (Net::PH), który umo¿liwia
komunikacjê z serwerami CCSO Nameserver Server-Client Protocol.

%prep
%setup -q -n libnet-%{version}
%patch -p1

%build
yes "" | perl Makefile.PL 

%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

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
%{perl_sitelib}/Net/DummyInetd.pm
%{perl_sitelib}/Net/FTP
%{perl_sitelib}/Net/FTP.pm
%{perl_sitelib}/Net/NNTP.pm
%{perl_sitelib}/Net/Netrc.pm
%{perl_sitelib}/Net/PH.pm
%{perl_sitelib}/Net/POP3.pm
%{perl_sitelib}/Net/SMTP.pm
%{perl_sitelib}/Net/SNPP.pm
%{perl_sitelib}/Net/Time.pm
%{_mandir}/man3/*
