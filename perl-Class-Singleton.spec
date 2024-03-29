Name:           perl-Class-Singleton
Version:        1.4
Release:        6%{?dist}
Summary:        Implementation of a "Singleton" class
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Class-Singleton/
Source0:        http://www.cpan.org/authors/id/A/AB/ABW/Class-Singleton-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is the Class::Singleton module. A Singleton describes an object class
that can have only one instance in any system. An example of a Singleton
might be a print spooler or system registry. This module implements a
Singleton class from which other classes can be derived. By itself, the
Class::Singleton module does very little other than manage the
instantiation of a single object. In deriving a class from
Class::Singleton, your module will inherit the Singleton instantiation
method and can implement whatever specific functionality is required.

%prep
%setup -q -n Class-Singleton-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.4-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4-3
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.4-2
- rebuild for new perl

* Mon Oct 15 2007 Steven Pritchard <steve@kspei.com> 1.4-1
- Update to 1.4.
- Update License tag.
- Drop our copy of the license text.
- Improve Summary.
- Make description match cpanspec output.
- BR Test::More.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 1.03-4
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 1.03-3
- Canonicalize Source0 URL.
- Fix find option order.

* Thu Sep 08 2005 Steven Pritchard <steve@kspei.com> 1.03-2
- Fix permissions on Singleton.pm.

* Wed Aug 31 2005 Steven Pritchard <steve@kspei.com> 1.03-1
- Specfile autogenerated.
