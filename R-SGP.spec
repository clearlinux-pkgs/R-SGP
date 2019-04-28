#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-SGP
Version  : 1.9.0.0
Release  : 15
URL      : https://cran.r-project.org/src/contrib/SGP_1.9-0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/SGP_1.9-0.0.tar.gz
Summary  : Student Growth Percentiles & Percentile Growth Trajectories
Group    : Development/Tools
License  : GPL-3.0
Requires: R-tidyselect
BuildRequires : R-Cairo
BuildRequires : R-DBI
BuildRequires : R-MatrixModels
BuildRequires : R-RSQLite
BuildRequires : R-Rcpp
BuildRequires : R-SGPdata
BuildRequires : R-SparseM
BuildRequires : R-bibtex
BuildRequires : R-bit64
BuildRequires : R-blob
BuildRequires : R-colorspace
BuildRequires : R-data.table
BuildRequires : R-doParallel
BuildRequires : R-doRNG
BuildRequires : R-dplyr
BuildRequires : R-equate
BuildRequires : R-foreach
BuildRequires : R-ggplot2
BuildRequires : R-gridBase
BuildRequires : R-gtable
BuildRequires : R-gtools
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-iterators
BuildRequires : R-jsonlite
BuildRequires : R-lazyeval
BuildRequires : R-matrixStats
BuildRequires : R-memoise
BuildRequires : R-mnormt
BuildRequires : R-munsell
BuildRequires : R-numDeriv
BuildRequires : R-pillar
BuildRequires : R-pkgconfig
BuildRequires : R-pkgmaker
BuildRequires : R-plotly
BuildRequires : R-plyr
BuildRequires : R-quantreg
BuildRequires : R-randomNames
BuildRequires : R-registry
BuildRequires : R-rngtools
BuildRequires : R-scales
BuildRequires : R-sn
BuildRequires : R-stringi
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : R-toOrdinal
BuildRequires : R-viridisLite
BuildRequires : R-xtable
BuildRequires : buildreq-R

%description
longitudinal assessment data.  Functions use quantile regression to estimate the conditional density associated
        with each student's achievement history.  Percentile growth projections/trajectories are calculated using the coefficient matrices derived from
	the quantile regression analyses and specify what percentile growth is required for students to reach future achievement targets.

%prep
%setup -q -c -n SGP

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556482703

%install
export SOURCE_DATE_EPOCH=1556482703
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SGP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SGP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SGP
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc SGP || :


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
