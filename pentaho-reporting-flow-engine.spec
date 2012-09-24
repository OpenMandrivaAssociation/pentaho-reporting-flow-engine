Name:           pentaho-reporting-flow-engine
Epoch:          1
Version:        0.9.4
Release:        %mkrel 7
Summary:        Pentaho Flow Reporting Engine
License:        LGPLv2+
Group:          System/Libraries
Source0:        http://downloads.sourceforge.net/jfreereport/flow-engine-%{version}.zip
URL:            http://reporting.pentaho.org/
BuildRequires:  ant, java-devel, jpackage-utils, libbase, libserializer
BuildRequires:  libloader, libfonts, pentaho-libxml, xml-commons-apis
BuildRequires:  librepository, sac, flute, liblayout, libformula
Requires:       java, jpackage-utils, libbase >= 1.1.3, libfonts >= 1.1.3
Requires:       pentaho-libxml, libformula >= 1.1.3, librepository >= 1.1.3
Requires:       sac, flute, liblayout >= 0.2.10, libserializer
BuildArch:      noarch

%description
Pentaho Reporting Flow Engine is a free Java report library, formerly
known as 'JFreeReport'


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = 1:%{version}-%{release}
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -c
mkdir -p lib
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib commons-logging-api libbase libloader \
    libfonts libxml jaxp libformula librepository sac flute liblayout \
    libserializer

%build
ant jar javadoc

%install
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/flow-engine.jar %{buildroot}%{_javadir}/flow-engine.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/api %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}


%changelog

* Sat Jan 21 2012 kamil <kamil> 1:0.9.4-7.mga2
+ Revision: 198996
- rebuild against new libloader, libfonts, pentaho-libxml, libbase, libserializer, librepository, liblayout, libformula (everything 1.1.6)
- rebuild against new libbase-1.1.6 and new librepository-1.1.6

* Sat Jan 21 2012 kamil <kamil> 1:0.9.4-5.mga2
+ Revision: 198919
- drop gcj support
- fix group for the javadoc subpackage
- rebuild against new libserializer-1.1.6

* Sun Apr 17 2011 stormi <stormi> 1:0.9.4-4.mga1
+ Revision: 87443
- fix RPM group

* Fri Mar 18 2011 dmorgan <dmorgan> 1:0.9.4-3.mga1
+ Revision: 74264
- Fix with_gcj macro
- Rebuild withtou gcj support

* Sun Jan 23 2011 dmorgan <dmorgan> 1:0.9.4-2.mga1
+ Revision: 35547
- Adapt for mageia
- imported package pentaho-reporting-flow-engine


* Fri Jul 02 2010 Caolán McNamara <caolanm@redhat.com> 0.9.4-2
- rebuild against libserializer

* Thu Dec 03 2009 Caolán McNamara <caolanm@redhat.com> 0.9.4-1
- latest version

* Fri Jul 24 2009 Caolán McNamara <caolanm@redhat.com> 0.9.2-5.OOo31
- make javadoc no-arch when building as arch-dependant aot

* Sun Mar 29 2009 Caolán McNamara <caolanm@redhat.com> 0.9.2-4.OOo31
- wrong num

* Sat Mar 28 2009 Caolán McNamara <caolanm@redhat.com> 0.9.2-3.OOo31
- tweak version

* Mon Mar 16 2009 Caolán McNamara <caolanm@redhat.com> 0.9.2-1
- OOo tuned version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 05 2008 Caolán McNamara <caolanm@redhat.com> 0.9.3-2
- wrong liblayout version required

* Wed May 07 2008 Caolán McNamara <caolanm@redhat.com> 0.9.3-1
- initial fedora import
