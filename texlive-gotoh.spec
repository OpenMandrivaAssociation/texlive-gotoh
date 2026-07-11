%global tl_name gotoh
%global tl_revision 44764

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	An implementation of the Gotoh sequence alignment algorithm
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gotoh
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gotoh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gotoh.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gotoh.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package calculates biological sequence alignment with the Gotoh
algorithm. The package also provides an interface to control various
settings including algorithm parameters.

