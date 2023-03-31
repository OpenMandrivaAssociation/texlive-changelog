Name:		texlive-changelog
Version:	56338
Release:	2
Summary:	Provides a changelog environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changelog
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changelog.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changelog.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a changelog environment (which itself
provides a version environment) to represent a changelog. The
package supports multiple authors, unreleased changes, and
yanked (revoked) releases. Inspired by keepachangelog.com.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/changelog
%doc %{_texmfdistdir}/doc/latex/changelog

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
