Name: beebank-test
Version: 1.0.0
Release: 1
Summary: phpor's hello world

Group:	Development/Languages
License: BSD
URL: http://phpor.net
Source0: beebank-test-1.0.0.tar.gz

%description
test

%prep
%setup -q


%build
%configure
make 


%install
%makeinstall


%files
/usr/bin/hello
%config /etc/hello.conf

%doc


%changelog

