%define		subver		2014-07-16
%define		ver			%(echo %{subver} | tr -d -)
%define		plugin		diffpreview
%define		php_min_version 5.3.0
Summary:	DokuWiki diff preview plugin
Summary(pl.UTF-8):	Wtyczka diffpreview dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/issmirnov/dokuwiki-diffpreview/archive/c6fd2c86/%{plugin}-%{version}.tar.gz
# Source0-md5:	a270cd74b41e9a8002635ac1245968cf
URL:		https://www.dokuwiki.org/plugin:diffpreview
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20131208
Requires:	php(core) >= %{php_min_version}
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
%setup -qc
mv dokuwiki-diffpreview-*/* .

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/README.md

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
%doc README.md
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.js
%{plugindir}/*.txt
