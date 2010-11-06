Name:		fldigi
Version:	3.20.29
Release:	%mkrel 1
Summary:	Fldigi is a software modem for Amateur Radio use
License:        GPLv3
Group:          Communications
URL:            http://www.w1hkj.com
Source0:        http://www.w1hkj.com/download.html/%{name}-%{version}.tar.gz
BuildRequires:  libpulseaudio-devel
BuildRequires:  portaudio-devel
BuildRequires: 	fltk-devel
BuildRequires:  libxmlrpc-c-devel
BuildRequires:	hamlib-devel
BuildRequires:	sndfile-devel



%description
Fldigi is a software modem for Amateur Radio use. It is a sound card based
program that is used for both transmitting and receiving data in any of the
following modes:

BPSK and QPSK        31, 63, 125, 250 (both), and 63F and 500 (BPSK only)
PSKR                 125, 250, and 500
CW                   speeds from 5 to 200 wpm
DominoEX             4, 5, 8, 11, 16 and 22; also with FEC
Hellschreiber        Feld Hell, Slow Hell, Hell x5/x9, FSKHell(-105) and Hell 80
MFSK                 4, 8, 11, 16, 22, 31, 32 and 64; most with image support
MT63                 500, 1000 and 2000
OLIVIA               various tones and bandwidths
RTTY                 various baud rates, shifts, nbr. of data bits, etc.
THOR                 4, 5, 8, 11, 16 and 22
Throb and ThrobX     1, 2, and 4
WWV                  receive only - calibrate your sound card to WWV
Frequency Analysis   receive only - measure the frequency of a carrier

Fldigi can also control a transceiver using Hamlib or RigCAT I/O, perform online
or cdrom QRZ queries, log QSOs with the built-in logbook or Xlog, and send
reception reports to the PSK Automatic Propagation Reporter.



%prep 
%setup -q

%build 
%configure 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(0755,root,root) 
%doc README NEWS COPYING AUTHORS
%{_bindir}/flarq
%{_bindir}/fldigi
%{_bindir}/fldigi-shell
%{_datadir}/applications/flarq.desktop
%{_datadir}/applications/fldigi.desktop
%{_datadir}/locale/fr/LC_MESSAGES/fldigi.mo
%{_datadir}/pixmaps/flarq.xpm
%{_datadir}/pixmaps/fldigi.xpm
%{_mandir}/man1/flarq.1*
%{_mandir}/man1/fldigi.1*
%{_mandir}/man1/fldigi-shell.1*

 











