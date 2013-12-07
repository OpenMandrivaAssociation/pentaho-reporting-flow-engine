Summary:	Pentaho Flow Reporting Engine
Name:		pentaho-reporting-flow-engine
Version:	0.9.4
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://reporting.pentaho.org/
Source0:	http://downloads.sourceforge.net/jfreereport/flow-engine-%{version}.zip
BuildRequires:	ant
BuildRequires:	flute
BuildRequires:	java-devel
BuildRequires:	jpackage-utils
BuildRequires:	libbase
BuildRequires:	libfonts
BuildRequires:	libformula
BuildRequires:	liblayout
BuildRequires:	libloader
BuildRequires:	librepository
BuildRequires:	libserializer
BuildRequires:	pentaho-libxml
BuildRequires:	sac
BuildRequires:	xml-commons-apis
Requires:	java
Requires:	jpackage-utils
Requires:	libbase >= 1.1.3
Requires:	libfonts >= 1.1.3
Requires:	pentaho-libxml
Requires:	libformula >= 1.1.3
Requires:	librepository >= 1.1.3
Requires:	sac
Requires:	flute
Requires:	liblayout >= 0.2.10
Requires:	libserializer
BuildArch:	noarch

%description
Pentaho Reporting Flow Engine is a free Java report library, formerly
known as 'JFreeReport'

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

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
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}

