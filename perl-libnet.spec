Summary:	Miscellaneous perl networking modules
Summary(pl):	Ró¿ne modu³y perlowe do obs³ugi sieci
Name:		libnet
Version:	1.0605
Release:	2
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Copyright:	GPL
URL:		http://www.perl.com/CPAN//modules/by-module/Net/libnet-1.0502.readme
Source:		ftp://ftp.digital.com/pub/plan/perl/CPAN/modules/by-module/Net/%{name}-%{version}.tar.gz
Requires:	perl >= 5.002
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
%setup -q

%build
yes "" | perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
# install -d $RPM_BUILD_ROOT/usr/{lib/perl5/site_perl/Net,man/man3}
make install \
	MKPATH="install -d" \
	PREFIX=$RPM_BUILD_ROOT/usr \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT/usr/man/man3

gzip -9nf $RPM_BUILD_ROOT/usr/man/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir /usr/lib/perl5/site_perl/*/*/Net
%config(noreplace) /usr/lib/perl5/site_perl/*/*/Net/Config.pm

/usr/lib/perl5/site_perl/*/*/Net/Cmd.pm
/usr/lib/perl5/site_perl/*/*/Net/Domain.pm
/usr/lib/perl5/site_perl/*/*/Net/DummyInetd.pm
/usr/lib/perl5/site_perl/*/*/Net/FTP
/usr/lib/perl5/site_perl/*/*/Net/FTP.pm
/usr/lib/perl5/site_perl/*/*/Net/NNTP.pm
/usr/lib/perl5/site_perl/*/*/Net/Netrc.pm
/usr/lib/perl5/site_perl/*/*/Net/PH.pm
/usr/lib/perl5/site_perl/*/*/Net/POP3.pm
/usr/lib/perl5/site_perl/*/*/Net/SMTP.pm
/usr/lib/perl5/site_perl/*/*/Net/SNPP.pm
/usr/lib/perl5/site_perl/*/*/Net/Time.pm
/usr/lib/perl5/site_perl/*/*/auto/Net
/usr/man/man3/*

%changelog 
* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.0605-2]
- changed Group to Development/Languages/Perl
- added Group(pl)
- removed man group from man pages
- added gzipping man pages

* Wed Nov 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0605-1]
- rewrited for using Buildroot,
- added -q %setup parameter,
- added pl translation,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- removed %post,
- removed Packager field (this must be placed in private ~/.rpmrc),
- man pages moved to /usr/mam/man3,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Thu Mar 08 1998 Kirk Bauer <kirk@kaybee.org>
For some reason, Config.pm ended up in a different place on my system.
So, I made a new release.  I will probably be killed for this next one,
but I took out the dependencies for IO and Data-Dumper... because
it seems that LibNet works without them...

* Thu Jul 17 1997 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
This distribution of libnet is the same as libnet rel1.  Someone created
a libnet release 2 that did not have all the proper files.... If that
person would care to talk to me about why they thought their subtractions
from the package were necessary, I would be most pleased.
