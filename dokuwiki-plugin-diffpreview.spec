# http://bugs.splitbrain.org/index.php?do=details&task_id=1673
%define		plugin		diffpreview
Summary:	DokuWiki diff preview plugin
Summary(pl.UTF-8):	Wtyczka diffpreview dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20100110
Release:	1
License:	GPL v2
Group:		Applications/WWW
# Source0Download: http://bugs.splitbrain.org/index.php?getfile=282
Source0:	diffpreview.zip
# Source0-md5:	ff537be6d8863ea64e8e1952495aab21
URL:		http://www.dokuwiki.org/plugin:diffpreview
BuildRequires:	rpmbuild(macros) >= 1.520
BuildRequires:	unzip
Requires:	dokuwiki >= 20090214
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir	/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Adds a new button to show a diff-like preview of all changes while
editing a page.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.js
