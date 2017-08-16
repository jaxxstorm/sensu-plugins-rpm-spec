%define name sensu-plugins


# hack to disable path checks. We probably should not do this..
#%define __arch_install_post /bin/true
# Disable debug find
%define debug_package %{nil}

Name:		%{name}
Version:	0.1
Release:	1%{?dist}
Summary:  A collection of ruby based sensu plugins

License: GPL
Group: Application/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: x86_64
Source: %{name}-%{version}.tar.gz

AutoReqProv: no
BuildRequires:	gcc gcc-c++ sensu >= 1.0.1
Requires: nagios-plugins-all sensu >= 1.0.1


%description
A collection of ruby sensu plugins


%prep

%setup -q -n %{name}-%{version}

%build
/opt/sensu/embedded/bin/gem install -i %{_builddir}/ruby/2.4.0 bundler  --no-rdoc --no-ri
GEM_HOME=%{_builddir}/ruby/2.4.0 %{_builddir}/ruby/2.4.0/bin/bundle install --path %{_builddir}

%install

rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/sensu/embedded/lib/ruby/gems
mv %{_builddir}/ruby/2.4.0 %{buildroot}/opt/sensu/embedded/lib/ruby/gems

mkdir -p %{buildroot}/etc/sensu/plugins
mkdir -p %{buildroot}/etc/sensu/handlers
cp -a sensu-plugins/* %{buildroot}/etc/sensu/plugins
cp -a sensu-handlers/* %{buildroot}/etc/sensu/plugins
chmod -R 0755 %{buildroot}/etc/sensu/plugins
chmod -R 0755 %{buildroot}/etc/sensu/handlers


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,755)
%dir /opt/sensu
%dir /etc/sensu
%dir /etc/sensu/plugins
/etc/sensu/*
/opt/sensu/*

%post

%changelog

* Wed Aug 16 2017 Lee Briggs <lee@leebriggs.co.uk>
- Initial commit


