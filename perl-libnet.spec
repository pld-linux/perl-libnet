Summary:	Miscellaneous perl networking modules
Summary(pl):	Ró¿ne modu³y perlowe do obs³ugi sieci
Name:		perl-libnet
Version:	1.0606
Release:	3
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Copyright:	GPL
URL:		http://www.perl.com/CPAN//modules/by-module/Net/libnet-%{version}.readme
Source:		ftp://ftp.digital.com/pub/plan/perl/CPAN/modules/by-module/Net/libnet-%{version}.tar.gz
Patch:		perl-libnet-Configure.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
Obsoletes:	libnet
Buildroot:	/tmp/%{name}-%{version}-root

%description
libnet is a collection of Perl modules which provides a simple
and consistent programming interface (API) to the client side
of various protocols used in the internet community.
The RFCs implemented in this distribution are

Net::FTP        RFC959          File Transfer Protocol
Net::SMTP       RFC821          Simple Mail Transfer Protocol
Net::Time       RFC867          Daytime Protocol
Net::Time       RFC868          Time Protocol
Net::NNTP       RFC977          Network News Transfer Protocol
Net::POP3       RFC1939         Post Office Protocol 3
Net::SNPP       RFC1861         Simple Network Pager Protocol

The distribution also contains a module (Net::PH) which facilitates
comunicate with with servers using the CCSO Nameserver Server-Client
Protocol

%description -l pl
libnet jest zestawem modu³ów do perla, które udostêpniaj± prosty i spójny 
interfejs programisty (API) do obs³ugi po stronie klienta ró¿nych protoko³ów
u¿uwanych w sieci Internet.
Spis dokumentów RFS, które s± zaimplementowane w libnet:

Net::FTP        RFC959          File Transfer Protocol
Net::SMTP       RFC821          Simple Mail Transfer Protocol
Net::Time       RFC867          Daytime Protocol
Net::Time       RFC868          Time Protocol
Net::NNTP       RFC977          Network News Transfer Protocol
Net::POP3       RFC1939         Post Office Protocol 3
Net::SNPP       RFC1861         Simple Network Pager Protocol

Dystrybucja libnet zawiera tak¿e modu³ (Net::PH), który umo¿liwia
komunikacjê z serwerami CCSO Nameserver Server-Client Protocol.

%prep
%setup -q -n libnet-%{version}
%patch -p1

%build
yes "" | perl Makefile.PL 

make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}
make install \
	DESTDIR=$RPM_BUILD_ROOT

sed -e "s#$RPM_BUILD_ROOT##g" $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/.packlist \
	>$RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/.packlist.wrk
mv $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/.packlist.wrk \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/.packlist

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_sitearch}/Net
%config(noreplace) %{perl_sitearch}/Net/Config.pm

%{perl_sitearch}/Net/Cmd.pm
%{perl_sitearch}/Net/Domain.pm
%{perl_sitearch}/Net/DummyInetd.pm
%{perl_sitearch}/Net/FTP
%{perl_sitearch}/Net/FTP.pm
%{perl_sitearch}/Net/NNTP.pm
%{perl_sitearch}/Net/Netrc.pm
%{perl_sitearch}/Net/PH.pm
%{perl_sitearch}/Net/POP3.pm
%{perl_sitearch}/Net/SMTP.pm
%{perl_sitearch}/Net/SNPP.pm
%{perl_sitearch}/Net/Time.pm
%{perl_sitearch}/auto/Net
%{_mandir}/man3/*
