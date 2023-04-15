# NOTE: currently we are packaging individual parts as gstreamer-*-apidocs
Summary:	GStreamer design documents collection
Summary(pl.UTF-8):	Zbiór dokumentów projektowych GStreamera
Name:		gstreamer-docs
Version:	1.22.2
Release:	0.1
License:	OPL v1.0, LGPL v2.1+, BSD, MIT, CC-BY-SA 4.0
Group:		Documentation
Source0:	https://gstreamer.freedesktop.org/src/gstreamer-docs/gstreamer-docs-%{version}.tar.xz
# Source0-md5:	b8dc03a89c5af97ef4645b2382b733ff
URL:		https://gstreamer.freedesktop.org/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of GStreamer design documents, formerly
maintained in various different locations and formats, now grouped
together and converted to commonmark.

%description -l pl.UTF-8
Ten pakiet to zbiór dokumentów projektowych GStreamera, uprzednio
utrzymywanych w różnych miejscach i formatach, a teraz pogrupowanych i
przekonwertowanych do formatu commonmark.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/devhelp/books

cp -pr devhelp/books/GStreamer $RPM_BUILD_ROOT%{_datadir}/devhelp/books

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING LICENSE.BSD LICENSE.CC-BY-SA-4.0 LICENSE.MIT LICENSE.OPL README.md
%{_datadir}/devhelp/books/GStreamer
