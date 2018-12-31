%global snaprel %{nil}

%define base_name gcc
%global ver_major_minor 6.3
Name: %{base_name}%{ver_major_minor}
Version: %{ver_major_minor}.0
%define src_dir %{base_name}-%{version}
Release: 0%{?dist}
Summary: Various compilers (C, C++, Objective-C, ...)
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group: Development/Languages
URL: http://gcc.gnu.org
BuildRequires: git
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libgcc
BuildRequires: gdb elfutils-devel elfutils-libelf-devel glibc cpp
BuildRequires: glibc-static
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, sharutils
BuildRequires: texinfo, texinfo-tex, /usr/bin/pod2man
BuildRequires: systemtap-sdt-devel
BuildRequires: gmp-devel, mpfr-devel, libmpc-devel
BuildRequires: python2-devel, python3-devel
BuildRequires: gcc, gcc-c++
BuildRequires: hostname, procps
BuildRequires: glibc-devel  
BuildRequires: elfutils-devel  
BuildRequires: elfutils-libelf-devel    
BuildRequires: glibc
BuildRequires: /lib/libc.so.6 /usr/lib/libc.so /lib64/libc.so.6 /usr/lib64/libc.so
Patch0: gcc-%{version}.patch
%undefine _missing_build_ids_terminate_build
%undefine _disable_source_fetch
Source0: https://hephaistos.lpp.polytechnique.fr/data/mirrors/gcc/gcc-%{version}.tar.gz
%define  SHA256SUM0 f70eff74a6b4941121bc3ed1446e67e289cd4303be28edddae28f4c102f6ce7c
%description
The gcc package contains the GNU Compiler Collection version %{version}.

%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -
%setup -qn %{src_dir}
%patch0 -p1

%build
CFLAGS=-Ducontext=ucontext_t  CXXFLAGS=-Ducontext=ucontext_t \
    ./configure --prefix=%{_usr}/local/%{src_dir} --enable-multilib --with-tune=generic --with-arch_32=i686
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}


%files
%{_usr}/local/%{src_dir}/*

%changelog

* Mon Dec 31 2018 Alexis Jeandet <alexis.jeandet@member.fsf.org> - 6.3.0-0
- First setup

