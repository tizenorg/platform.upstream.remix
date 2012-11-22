Name:           remix
Version:        0.2.4
Release:        1
License:        LGPL-2.1
Summary:        An audio sequencing and mixing library
Url:            http://www.metadecks.org/software/remix/
Group:          Libraries/Sound
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  libsndfile-devel
BuildRequires:  autoconf, automake, libtool

%description
Remix is an audio sequencing and mixing library that provides a multichannel,
sparse audio data container (streams), a structured mixing abstraction (decks),
and widely useful means of generating control data (via envelopes) and of
caching audio data.

%package -n libremix
Summary:        An audio sequencing and mixing library
Group:          Libraries

%description -n libremix
Remix is an audio sequencing and mixing library that provides a multichannel,
sparse audio data container (streams), a structured mixing abstraction (decks),
and widely useful means of generating control data (via envelopes) and of
caching audio data.

%package -n libremix-devel
Summary:        Libraries, includes, etc to develop remix applications
Group:          Libraries
Requires:       lib%{name} = %{version}

%description -n libremix-devel
Libraries, include files, etc you can use to develop remix applications.

%prep
%setup -q

%build
%reconfigure
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/usr/share/license/%{name}

%remove_docs

%post -n libremix -p /sbin/ldconfig

%postun -n libremix -p /sbin/ldconfig

%files  -n libremix
%manifest %{name}.manifest
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libremix.so.*
%{_libdir}/libctxdata.so.*
/usr/lib/remix/libremix_ladspa*
/usr/lib/remix/libremix_noise*
/usr/share/license/%{name}

%files -n libremix-devel
%defattr(-,root,root,-)
%{_libdir}/libremix.so
%{_libdir}/libctxdata.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ctxdata.h
%{_includedir}/remix/*.h
