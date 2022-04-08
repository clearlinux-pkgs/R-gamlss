#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gamlss
Version  : 5.4.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/gamlss_5.4-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gamlss_5.4-1.tar.gz
Summary  : Generalised Additive Models for Location Scale and Shape
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-gamlss-lib = %{version}-%{release}
Requires: R-gamlss.data
Requires: R-gamlss.dist
BuildRequires : R-gamlss.data
BuildRequires : R-gamlss.dist
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-gamlss package.
Group: Libraries

%description lib
lib components for the R-gamlss package.


%prep
%setup -q -c -n gamlss
cd %{_builddir}/gamlss

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649433709

%install
export SOURCE_DATE_EPOCH=1649433709
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamlss
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamlss
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamlss
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gamlss || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gamlss/CITATION
/usr/lib64/R/library/gamlss/DESCRIPTION
/usr/lib64/R/library/gamlss/INDEX
/usr/lib64/R/library/gamlss/Meta/Rd.rds
/usr/lib64/R/library/gamlss/Meta/features.rds
/usr/lib64/R/library/gamlss/Meta/hsearch.rds
/usr/lib64/R/library/gamlss/Meta/links.rds
/usr/lib64/R/library/gamlss/Meta/nsInfo.rds
/usr/lib64/R/library/gamlss/Meta/package.rds
/usr/lib64/R/library/gamlss/NAMESPACE
/usr/lib64/R/library/gamlss/R/gamlss
/usr/lib64/R/library/gamlss/R/gamlss.rdb
/usr/lib64/R/library/gamlss/R/gamlss.rdx
/usr/lib64/R/library/gamlss/doc/NEWS.txt
/usr/lib64/R/library/gamlss/help/AnIndex
/usr/lib64/R/library/gamlss/help/aliases.rds
/usr/lib64/R/library/gamlss/help/gamlss.rdb
/usr/lib64/R/library/gamlss/help/gamlss.rdx
/usr/lib64/R/library/gamlss/help/paths.rds
/usr/lib64/R/library/gamlss/html/00Index.html
/usr/lib64/R/library/gamlss/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gamlss/libs/gamlss.so
/usr/lib64/R/library/gamlss/libs/gamlss.so.avx2
/usr/lib64/R/library/gamlss/libs/gamlss.so.avx512
