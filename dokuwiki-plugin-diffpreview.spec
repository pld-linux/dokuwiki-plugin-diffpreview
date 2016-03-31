# http://bugs.splitbrain.org/index.php?do=details&task_id=1673
%define		plugin		diffpreview
Summary:	DokuWiki diff preview plugin
Summary(pl.UTF-8):	Wtyczka diffpreview dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20110120
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/adrianheine/dokuwiki-diffpreview/archive/0f215700/%{name}.tar.gz
# Source0-md5:	e6190c6a2ee9895d8a57967ff6f53869
URL:		https://www.dokuwiki.org/plugin:diffpreview
BuildRequires:	rpmbuild(macros) >= 1.520
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
%{plugindir}/*.txt
