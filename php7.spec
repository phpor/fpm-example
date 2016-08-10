%define version 7.0.9
%define so_version 5
%define release 1

Name: php
Summary: PHP: Hypertext Preprocessor
Group: Development/Languages
Version: %{version}
Release: %{release}
License: The PHP license (see "LICENSE" file included in distribution)
Source: php-7.0.9.tar.gz
URL: http://www.php.net/
Packager: PHP Group <group@php.net>
Requires: libpng libxml2 libcurl openssl zlib

BuildRoot: /var/tmp/php-%{version}

%description
PHP is an HTML-embedded scripting language. Much of its syntax is
borrowed from C, Java and Perl with a couple of unique PHP-specific
features thrown in. The goal of the language is to allow web
developers to write dynamically generated pages quickly.

%prep

%setup -c

%install
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/sbin
install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT/usr/local/php
install -d $RPM_BUILD_ROOT/usr/local/lib
cd %{name}-%{version}
cp -a bin/* $RPM_BUILD_ROOT/usr/bin/
cp -a sbin/* $RPM_BUILD_ROOT/usr/sbin/
cp -a lib/* $RPM_BUILD_ROOT/usr/local/lib/
cp -a etc/* $RPM_BUILD_ROOT/etc/
cp -a man $RPM_BUILD_ROOT/usr/local/php/

%clean

%files
%defattr(-,root,root)
/*
