Name:		texlive-gotoh
Version:	44764
Release:	2
Summary:	An implementation of the Gotoh sequence alignment algorithm
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gotoh
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gotoh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gotoh.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gotoh.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package calculates biological sequence alignment with the
Gotoh algorithm. The package also provides an interface to
control various settings including algorithm parameters.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gotoh
%{_texmfdistdir}/tex/latex/gotoh
%doc %{_texmfdistdir}/doc/latex/gotoh

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
