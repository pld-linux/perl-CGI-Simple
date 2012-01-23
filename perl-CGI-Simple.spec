#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Simple
Summary:	CGI::Simple - a Simple totally OO CGI interface that is CGI.pm compliant
Summary(pl.UTF-8):	CGI::Simple - prosty, zorientowany obiektowo interfejs CGI zgodny z CGI.pm
Name:		perl-CGI-Simple
Version:	1.113
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	50c50dbec87b822e3f2285e41cb23519
URL:		http://search.cpan.org/dist/Cgi-Simple/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IO-stringy
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Simple provides a relatively lightweight drop in replacement for
CGI.pm. It shares an identical OO interface to CGI.pm for parameter
parsing, file upload, cookie handling and header generation. This
module is entirely object oriented, however a complete functional
interface is available by using the CGI::Simple::Standard module.

%description -l pl.UTF-8
CGI::Simple udostępnia w miarę lekki zamiennik CGI.pm. Współdzieli z
CGI.pm identyczny zorientowany obiektowo interfejs do analizy
parametrów, przesyłania plików, obsługi ciasteczek i generowania
nagłówków. Ten moduł jest w pełni zorientowany obiektowo, ale z
pełnym interfejsem funkcyjnym dostępnym poprzez moduł
CGI::Simple::Standard.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#setup -q -n Cgi-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/*.pm
%{perl_vendorlib}/CGI/Simple
%{_mandir}/man3/*
