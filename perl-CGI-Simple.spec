#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	CGI
%define	pnam	Simple
Summary:	CGI::Simple - a Simple totally OO CGI interface that is CGI.pm compliant
Summary(pl.UTF-8):	CGI::Simple - prosty, zorientowany obiektowo interfejs CGI zgodny z CGI.pm
Name:		perl-CGI-Simple
Version:	1.282
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	870af26de58ec2053dece6e09a9e0c47
URL:		http://search.cpan.org/dist/Cgi-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-NoWarnings
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/*.pm
%{perl_vendorlib}/CGI/Simple
%{_mandir}/man3/*
