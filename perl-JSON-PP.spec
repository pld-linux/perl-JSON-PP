#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	JSON
%define		pnam	PP
Summary:	JSON::PP - JSON::XS compatible pure-Perl module
Summary(pl.UTF-8):	JSON::PP - czysto perlowy moduł kompatybilny z JSON::XS
Name:		perl-JSON-PP
Version:	4.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/JSON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4ec8d53913f529d3fe172559cb5a131e
URL:		https://metacpan.org/dist/JSON-PP
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Scalar-List-Utils >= 1.08
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Conflicts:	perl-JSON < 2.51
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is JSON::XS compatible pure Perl module. (Perl 5.8 or
later is recommended)

JSON::XS is the fastest and most proper JSON module on CPAN. It is
written by Marc Lehmann in C, so must be compiled and installed in the
used environment.

JSON::PP is a pure-Perl module and has compatibility to JSON::XS.

%description -l pl.UTF-8
JSON::PP jest modułem kompatybilnym z JSON::XS, napisanym w czystym
Perlu (zalecany jest Perl 5.8 lub nowszy).

JSON::XS jest najszybszym i najsensowniejszym modułem JSON na CPAN-ie.
Jest napisany przez Marca Lehmanna w C, więc mu być skompilowany i
zainstalowany przed użyciem.

JSON::PP jest modułem czysto perlowym, kompatybilnym z JSON::XS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%attr(755,root,root) %{_bindir}/json_pp
%dir %{perl_vendorlib}/JSON
%{perl_vendorlib}/JSON/PP.pm
%dir %{perl_vendorlib}/JSON/PP
%{perl_vendorlib}/JSON/PP/Boolean.pm
%{_mandir}/man1/json_pp.1p*
%{_mandir}/man3/JSON::PP*.3pm*
