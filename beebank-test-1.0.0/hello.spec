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
read -p  "prep ok , press enter to continue..."
%setup -q
read -p  "setup ok , press enter to continue..."


%build
read -p  "build ok , press enter to continue..."
%configure
read -p  "configure ok , press enter to continue..."
make 
read -p  "make ok , press enter to continue..."


%install
read -p  "install ok , press enter to continue..."
%makeinstall
read -p  "makeinstall ok , press enter to continue..."

%files
/usr/bin/hello
%config /etc/hello.conf

%doc


%changelog

