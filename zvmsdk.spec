%define name python-zvm-sdk

Summary: IBM z/VM cloud connector
Name: %{name}
Version: 0.3.0
Release: 1
Source: python-zvm-sdk.tar.gz
Vendor: IBM
License: ASL 2.0
BuildArch: noarch
Group: System/tools
Requires: python-netaddr, python-PyJWT, python-requests, python-routes, python-webob, python-jsonschema, python-six, zthin
BuildRoot: %{_tmppath}/python-zvm-sdk
Prefix: /opt/python-zvm-sdk

%description
The System z/VM cloud connector is a set of APIs to be used
by external
%define builddate %(date)

%prep
tar -zxvf ../SOURCES/python-zvm-sdk.tar.gz -C ../BUILD/ --strip 1

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --prefix= --record=INSTALLED_FILES


%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

%dir(644, zvmsdk, zvmsdk) /etc/zvmsdk
%dir(644, zvmsdk, zvmsdk) /var/log/zvmsdk
%dir(755, zvmsdk, zvmsdk) /var/lib/zvmsdk

%pre
/usr/bin/getent passwd zvmsdk || /usr/sbin/useradd -r -d /var/lib/zvmsdk -m -U zvmsdk

%postun

