%global plugin_name skypeweb

Name: purple-%{plugin_name}
Version: 1.7
Release: 1
Summary: Adds support for Skype to Pidgin
License: GPLv3
URL: https://github.com/EionRobb/skype4pidgin
Source0: https://github.com/EionRobb/skype4pidgin/archive/%{version}/skype4pidgin-%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(zlib)

Provides: skype4pidgin = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: skype4pidgin < %{?epoch:%{epoch}:}%{version}-%{release}

%description
Adds support for Skype to Pidgin, Adium, Finch and other libpurple 
based messengers.

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Skype protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Skype protocol implemented by libskypeweb.

%prep
%autosetup -n skype4pidgin-%{version}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," %{plugin_name}/README.md

%build
%set_build_flags
%make_build -C %{plugin_name}

%install
%make_install -C %{plugin_name}

%files
%{_libdir}/purple-2/lib%{plugin_name}.so

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/skype*.png
%{_datadir}/pixmaps/pidgin/emotes/skype
