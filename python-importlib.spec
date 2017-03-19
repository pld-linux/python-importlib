# NOTE: now it's part of python 2.7 / 3.1
Summary:	Backport of importlib.import_module() from Python 2.7
Summary(pl.UTF-8):	Backport importlib.import_module() z Pythona 2.7
Name:		python-importlib
Version:	1.0.4
Release:	0.1
License:	PSF
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/importlib/
Source0:	https://files.pythonhosted.org/packages/source/i/importlib/importlib-%{version}.zip
# Source0-md5:	5f9a0803bca7ba95f670d1464984296f
URL:		https://github.com/brettcannon/importlib
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the code from importlib as found in Python 2.7.
It is provided so that people who wish to use
importlib.import_module() with a version of Python prior to 2.7 or in 3.0
have the function readily available. The code in no way deviates from
what can be found in the Python 2.7 standard library.

For documentation, see the importlib docs for Python 2.7:
<http://docs.python.org/2.7/library/importlib.html>.

%description -l pl.UTF-8
Ten pakiet zawiera kod biblioteki importlib dołączonej do Pythona 2.7.
Pakiet jest przeznaczony dla chcących używać funkcji
importlib.import_module() w Pythonie starszym niż 2.7 lub w wersji
3.0. Kod nie różny się niczym od tego w bibliotece standardowej
Pythona 2.7.

Dokumentację można znaleźć w dokumentacji biblioteki Pythona 2.7:
<http://docs.python.org/2.7/library/importlib.html>.

%prep
%setup -q -n importlib-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%if "%{py_ver}" < "2.7"
%{py_sitescriptdir}/importlib
%endif
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/importlib-%{version}-py*.egg-info
%endif
