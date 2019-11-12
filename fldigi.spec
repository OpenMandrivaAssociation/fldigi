Name:		fldigi
Version:	4.1.08
Release:	1
Summary:	A software modem for Amateur Radio use
License:	GPLv3+
Group:		Communications/Radio
URL:		http://www.w1hkj.com
Source0:	https://sourceforge.net/projects/fldigi/files/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(hamlib) >= 1.2.4
BuildRequires:	pkgconfig(libpng) >= 1.2.8
BuildRequires:	pkgconfig(libpulse-simple) >= 0.9.7
BuildRequires:	pkgconfig(portaudio-2.0) >= 19
BuildRequires:	pkgconfig(samplerate) >= 0.1.1
BuildRequires:	pkgconfig(sndfile) >= 1.0.10
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(alsa)
BuildRequires:	fltk-devel
BuildRequires:	asciidoc
BuildRequires:	desktop-file-utils

Requires:	flrig

%description
Fldigi is a software modem for Amateur Radio use. It is a sound card based
program that is used for both transmitting and receiving data in any of the
following modes:

BPSK and QPSK        31, 63, 125, 250 (both), and 63F and 500 (BPSK only)
PSKR                 125, 250, and 500
CW                   speeds from 5 to 200 wpm
DominoEX             4, 5, 8, 11, 16 and 22; also with FEC
Hellschreiber        Feld Hell, Slow Hell, Hell x5/x9, FSKHell(-105)
                     and Hell 80
MFSK                 4, 8, 11, 16, 22, 31, 32 and 64; most with image support
MT63                 500, 1000 and 2000
OLIVIA               various tones and bandwidths
RTTY                 various baud rates, shifts, nbr. of data bits, etc.
THOR                 4, 5, 8, 11, 16 and 22
Throb and ThrobX     1, 2, and 4
WWV                  receive only - calibrate your sound card to WWV
Frequency Analysis   receive only - measure the frequency of a carrier

Fldigi can also control a transceiver using Hamlib or RigCAT I/O, perform
online or cdrom QRZ queries, log QSOs with the built-in logbook or Xlog,
and send reception reports to the PSK Automatic Propagation Reporter.

%prep
%setup -q

%build
%configure --disable-rpath
%make_build ASCIIDOC_ICONS_DIR=%{_sysconfdir}/asciidoc/images/icons V=1

%install
%make_install

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications \
--remove-category='Network' \
--add-category='AudioVideo' \
--add-category='Audio' \
--add-category='X-Mageia-CrossDesktop' \
%{buildroot}%{_datadir}/applications/fldigi.desktop

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications \
--remove-category='Network' \
--add-category='AudioVideo' \
--add-category='Audio' \
--add-category='X-Mageia-CrossDesktop' \
%{buildroot}%{_datadir}/applications/flarq.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc README NEWS AUTHORS doc/guide*
%{_bindir}/flarq
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*.xpm
%{_mandir}/man1/flarq.1*
%{_mandir}/man1/%{name}.1*
