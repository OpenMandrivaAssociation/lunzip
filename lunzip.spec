Name:		lunzip
Summary:	Decompressor for lzip files
Version:	1.1
Release:	1
License:	GPLv3+
Group:		Archiving/Compression
URL:		http://www.nongnu.org/lzip/lunzip.html
Source0:	http://download.savannah.gnu.org/releases/lzip/%{name}-%{version}.tar.lz
BuildRequires:	lzip

%description
Lunzip is a decompressor for lzip files. It is written in C and its small size
makes it well suited for embedded devices or software installers that need
to decompress files but do not need compression capabilities.

Lunzip replaces every file given in the command line with a decompressed
version of itself. Each decompressed file has the same modification date,
permissions, and, when possible, ownership as the corresponding compressed
file. Lunzip is able to read from some types of non regular files
if the "--stdout" option is specified.

If no file names are specified, lunzip decompresses from standard input
to standard output. In this case, lunzip will decline to read compressed input
from a terminal.

Lunzip will correctly decompress a file which is the concatenation of two
or more compressed files. The result is the concatenation of the corresponding
uncompressed files. Integrity testing of concatenated compressed files is also
supported.

The amount of memory required by lunzip to decompress a file is only a few tens
of KiB larger than the dictionary size used to compress that file. 

%prep
%setup -q

%build
%configure
%make

%check
make check

%install
%makeinstall_std

%files
%{_bindir}/lunzip
%{_mandir}/man1/lunzip.1*
%doc AUTHORS ChangeLog NEWS README


%changelog
* Wed Apr 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1-1
+ Revision: 789134
- update to 1.1
- run make check after build

* Tue Mar 13 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0-1
+ Revision: 784552
- imported package lunzip

