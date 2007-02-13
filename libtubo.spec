Summary:	Interprocess communication library
Summary(pl.UTF-8):	Biblioteka komunikacji międzyprocesowej
Name:		libtubo
Version:	4.5.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/xffm/%{name}-%{version}.tar.gz
# Source0-md5:	b860deed622fd9484ac640ec7ebf7234
URL:		http://xffm.sourceforge.net/libtubo.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libtubo library is small and simple function set to enable a
process to run any other process in the background and communicate via
the stdout, stderr and stdin.

%description -l pl.UTF-8
Biblioteka libtubo jest małym i prostym zbiorem funkcji, które
pozwalają procesom uruchomić w tle inny proces i komunikować się
poprzez stdout, stderr i stdin.

%package devel
Summary:	Header files for libtubo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtubo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.6.0

%description devel
Header files for libtubo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtubo.

%package static
Summary:	Static libtubo library
Summary(pl.UTF-8):	Statyczna biblioteka libtubo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtubo library.

%description static -l pl.UTF-8
Statyczna biblioteka libtubo.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libtubo.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtubo.so
%{_libdir}/libtubo.la
%dir %{_includedir}/xffm
%{_includedir}/xffm/*.h
%{_pkgconfigdir}/libtubo.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtubo.a
