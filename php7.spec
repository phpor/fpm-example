%define version 7.0.9
%define so_version 5
%define release 1
%define _user www
%define _group www

Name: beebank-php
Summary: PHP: Hypertext Preprocessor
Group: Development/Languages
Vendor: Beebank
Version: %{version}
Release: %{release}
License: The PHP license (see "LICENSE" file included in distribution)
#Source file in SOURCES
Source: beebank-php-7.0.9.tar.gz
URL: http://www.php.net/
Packager: phpor <junjie.li@beebank.com>

BuildRequires: libxml2-devel, gd-devel, libcurl-devel, openssl-devel, zlib-devel, libxslt-devel
#Requires multiple items separated by commas
Requires: gd, libpng, libxml2, libcurl, openssl, zlib, libxslt

%description
PHP is an HTML-embedded scripting language. Much of its syntax is
borrowed from C, Java and Perl with a couple of unique PHP-specific
features thrown in. The goal of the language is to allow web
developers to write dynamically generated pages quickly.

%prep

%setup
%build
./configure --localstatedir=/var --with-config-file-path=/etc/php.ini --with-config-file-scan-dir=/etc/php.d --bindir=/usr/bin --sbindir=/usr/sbin  --mandir=/usr/share/man --enable-fpm  --enable-mbstring=shared --enable-opcache=shared --enable-soap=shared --enable-mysqlnd=shared --with-gd=shared --enable-json=shared --enable-posix=shared --with-iconv=shared --enable-phpdbg --enable-pcntl=shared --enable-bcmath=shared --enable-zip=shared --enable-shmop=shared --enable-ftp=shared --enable-calendar=shared --enable-sockets=shared --with-xml=shared --with-xsl=shared
make %{?_smp_mflags}

%install
rm -fr %{buildroot}
make INSTALL_ROOT=%{buildroot} install
#%{__install} -p -D -m 0755 sapi/fpm/init.d.php-fpm %{buildroot}%{_sysconfdir}/init.d/php-fpm
%{__install} -p -D -m 0644 php.ini-production %{buildroot}/%{_sysconfdir}/php.ini


%pre
if [ $1 == 1 -a -z "`grep ^%{_user} /etc/passwd`" ]; then    # $1有3个值，代表动作，安装类型，处理类型
    groupadd %{_group} -g 10000                              # 1：表示安装
    useradd -u 10000 -g 10000 -m %{_user}                    # 2：表示升级
fi

%post
#/sbin/chkconfig --add php-fpm
#/sbin/chkconfig php-fpm on


%clean
rm -rf %{buildroot}

%files
/
#%attr(0755,root,root) %{_sysconfdir}/init.d/php-fpm
