# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-simplejson
Epoch: 100
Version: 4.1.1
Release: 1%{?dist}
Summary: Simple, fast, extensible JSON encoder/decoder for Python
License: BSD-3-Clause
URL: https://github.com/simplejson/simplejson/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org> encoder and decoder for Python 3.3+ with legacy
support for Python 2.5+. It is pure Python code with no dependencies,
but includes an optional C extension for a serious speed boost.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-simplejson
Summary: Simple, fast, extensible JSON encoder/decoder for Python
Requires: python3
Provides: python3-simplejson = %{epoch}:%{version}-%{release}
Provides: python3dist(simplejson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-simplejson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(simplejson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-simplejson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(simplejson) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-simplejson
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org> encoder and decoder for Python 3.3+ with legacy
support for Python 2.5+. It is pure Python code with no dependencies,
but includes an optional C extension for a serious speed boost.

%files -n python%{python3_version_nodots}-simplejson
%license LICENSE.txt
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n python3-simplejson
Summary: Simple, fast, extensible JSON encoder/decoder for Python
Requires: python3
Provides: python3-simplejson = %{epoch}:%{version}-%{release}
Provides: python3dist(simplejson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-simplejson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(simplejson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-simplejson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(simplejson) = %{epoch}:%{version}-%{release}

%description -n python3-simplejson
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org> encoder and decoder for Python 3.3+ with legacy
support for Python 2.5+. It is pure Python code with no dependencies,
but includes an optional C extension for a serious speed boost.

%files -n python3-simplejson
%license LICENSE.txt
%{python3_sitearch}/*
%endif

%changelog
