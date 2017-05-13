Summary:	GStreamer design documents collection
Summary(pl.UTF-8):	Zbiór dokumentów projektowych GStreamera
Name:		gstreamer-docs
Version:	1.10
%define	gitref	4c04cfda9f8c70b11eabce6b3ba2b187267a30c5
%define	snap	20170429
Release:	0.%{snap}.1
License:	unknown
Group:		Documentation
# git://anongit.freedesktop.org/gstreamer/gst-docs
Source0:	https://github.com/GStreamer/gst-docs/archive/%{gitref}/gst-docs-%{snap}.tar.gz
# Source0-md5:	13223c01c50c1f929f00962e71e4883e
# submodule for HTML:
#   path = theme/hotdoc_bootstrap_theme
#   url = git@github.com:hotdoc/hotdoc_bootstrap_theme.git
URL:		https://gstreamer.freedesktop.org/
# for HTML
#BuildRequires:	hotdoc
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
%setup -q -n gst-docs-%{gitref}

%build
# for HTML
#%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO.md examples images markdown plugins-introspection
