Summary:	Library to help mapping id's, mainly for NFSv
Name:		libnfsidmap
Version:	0.25
Release:	3
License:	BSD
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/libnfsidmap/%{name}-%{version}.tar.gz
# Source0-md5:	2ac4893c92716add1a1447ae01df77ab
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	openldap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to help mapping id's, mainly for NFSv4.

%package devel
Summary:	Header files for libnfsidmap library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnfsidmap library.

%package mappings
Summary:	Mapping functions
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mappings
Dynamically loaded mapping functions.

%prep
%setup -q

%build
%configure \
	--disable-static    \
	--with-pluginpath=%{_libdir}/libnfsidmap
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{*.la,libnfsidmap/*.la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libnfsidmap.so.0
%attr(755,root,root) %{_libdir}/libnfsidmap.so.*.*.*
%{_mandir}/man5/idmapd.conf.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnfsidmap.so
%{_includedir}/nfsidmap.h
%{_pkgconfigdir}/libnfsidmap.pc
%{_mandir}/man3/nfs4_uid_to_name.3*

%files mappings
%defattr(644,root,root,755)
%dir %{_libdir}/libnfsidmap
%attr(755,root,root) %{_libdir}/libnfsidmap/nsswitch.so
%attr(755,root,root) %{_libdir}/libnfsidmap/static.so
%attr(755,root,root) %{_libdir}/libnfsidmap/umich_ldap.so

