#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-SGP
Version  : 2.2.0.0
Release  : 51
URL      : https://cran.r-project.org/src/contrib/SGP_2.2-0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/SGP_2.2-0.0.tar.gz
Summary  : Student Growth Percentiles & Percentile Growth Trajectories
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Cairo
Requires: R-RSQLite
Requires: R-callr
Requires: R-collapse
Requires: R-colorspace
Requires: R-crayon
Requires: R-data.table
Requires: R-digest
Requires: R-doParallel
Requires: R-equate
Requires: R-foreach
Requires: R-gridBase
Requires: R-gtools
Requires: R-iterators
Requires: R-jsonlite
Requires: R-matrixStats
Requires: R-quantreg
Requires: R-randomNames
Requires: R-rngtools
Requires: R-sn
Requires: R-svglite
Requires: R-toOrdinal
BuildRequires : R-Cairo
BuildRequires : R-RSQLite
BuildRequires : R-callr
BuildRequires : R-collapse
BuildRequires : R-colorspace
BuildRequires : R-crayon
BuildRequires : R-data.table
BuildRequires : R-digest
BuildRequires : R-doParallel
BuildRequires : R-equate
BuildRequires : R-foreach
BuildRequires : R-gridBase
BuildRequires : R-gtools
BuildRequires : R-iterators
BuildRequires : R-jsonlite
BuildRequires : R-matrixStats
BuildRequires : R-quantreg
BuildRequires : R-randomNames
BuildRequires : R-rngtools
BuildRequires : R-sn
BuildRequires : R-svglite
BuildRequires : R-toOrdinal
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n SGP
pushd ..
cp -a SGP buildavx2
popd
pushd ..
cp -a SGP buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728427396

%install
export SOURCE_DATE_EPOCH=1728427396
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/SGP/CITATION
/usr/lib64/R/library/SGP/DESCRIPTION
/usr/lib64/R/library/SGP/INDEX
/usr/lib64/R/library/SGP/Meta/Rd.rds
/usr/lib64/R/library/SGP/Meta/data.rds
/usr/lib64/R/library/SGP/Meta/features.rds
/usr/lib64/R/library/SGP/Meta/hsearch.rds
/usr/lib64/R/library/SGP/Meta/links.rds
/usr/lib64/R/library/SGP/Meta/nsInfo.rds
/usr/lib64/R/library/SGP/Meta/package.rds
/usr/lib64/R/library/SGP/Meta/vignette.rds
/usr/lib64/R/library/SGP/NAMESPACE
/usr/lib64/R/library/SGP/NEWS
/usr/lib64/R/library/SGP/R/SGP
/usr/lib64/R/library/SGP/R/SGP.rdb
/usr/lib64/R/library/SGP/R/SGP.rdx
/usr/lib64/R/library/SGP/data/Rdata.rdb
/usr/lib64/R/library/SGP/data/Rdata.rds
/usr/lib64/R/library/SGP/data/Rdata.rdx
/usr/lib64/R/library/SGP/data/datalist
/usr/lib64/R/library/SGP/doc/SGP.R
/usr/lib64/R/library/SGP/doc/SGP.Rmd
/usr/lib64/R/library/SGP/doc/SGP.html
/usr/lib64/R/library/SGP/doc/SGP_Data_Analysis.R
/usr/lib64/R/library/SGP/doc/SGP_Data_Analysis.Rmd
/usr/lib64/R/library/SGP/doc/SGP_Data_Analysis.html
/usr/lib64/R/library/SGP/doc/SGP_Data_Preparation.R
/usr/lib64/R/library/SGP/doc/SGP_Data_Preparation.Rmd
/usr/lib64/R/library/SGP/doc/SGP_Data_Preparation.html
/usr/lib64/R/library/SGP/doc/index.html
/usr/lib64/R/library/SGP/help/AnIndex
/usr/lib64/R/library/SGP/help/SGP.rdb
/usr/lib64/R/library/SGP/help/SGP.rdx
/usr/lib64/R/library/SGP/help/aliases.rds
/usr/lib64/R/library/SGP/help/paths.rds
/usr/lib64/R/library/SGP/html/00Index.html
/usr/lib64/R/library/SGP/html/R.css
