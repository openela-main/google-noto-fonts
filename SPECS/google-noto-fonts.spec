%global fontname google-noto
%global fontconf %{fontname}
%global common_desc Noto fonts aims to remove tofu from web by providing fonts for all \
Unicode supported scripts. Its design goal is to achieve visual harmonization\
between multiple scripts. Noto family supports almost all scripts available\
in Unicode.\
%{nil}

%global commit 86b2e553c3e3e4d6614dadd1fa0a7a6dafd74552

Name:           %{fontname}-fonts
Version:        20161022
Release:        7%{?dist}.1
Summary:        Hinted and Non Hinted OpenType fonts for Unicode scripts
Group:          User Interface/X
License:        OFL
URL:            https://github.com/googlei18n/noto-fonts/
# downloaded from https://github.com/googlei18n/noto-fonts/tree/86b2e553c3e3e4d6614dadd1fa0a7a6dafd74552 -> download [zip]
# link https://codeload.github.com/googlei18n/noto-fonts/zip/86b2e553c3e3e4d6614dadd1fa0a7a6dafd74552
Source0:        noto-fonts-%{commit}.zip
Source2:        66-%{fontconf}-sans.conf
Source3:        66-%{fontconf}-sans-armenian.conf
Source4:        66-%{fontconf}-sans-avestan.conf
Source5:        66-%{fontconf}-sans-bengali.conf
Source6:        66-%{fontconf}-sans-bengali-ui.conf
Source7:        66-%{fontconf}-sans-brahmi.conf
Source8:        66-%{fontconf}-sans-carian.conf
Source9:        66-%{fontconf}-sans-cherokee.conf
Source10:       66-%{fontconf}-sans-coptic.conf
Source11:       66-%{fontconf}-sans-deseret.conf
Source12:       66-%{fontconf}-sans-devanagari.conf
Source13:       66-%{fontconf}-sans-devanagari-ui.conf
Source14:       66-%{fontconf}-sans-egyptian-hieroglyphs.conf
Source15:       66-%{fontconf}-sans-ethiopic.conf
Source16:       66-%{fontconf}-sans-georgian.conf
Source17:       66-%{fontconf}-sans-glagolitic.conf
Source18:       66-%{fontconf}-sans-hebrew.conf
Source19:       66-%{fontconf}-sans-imperial-aramaic.conf
Source20:       66-%{fontconf}-sans-kaithi.conf
Source21:       66-%{fontconf}-sans-kannada.conf
Source22:       66-%{fontconf}-sans-kayah-li.conf
Source23:       66-%{fontconf}-sans-kharoshthi.conf
Source24:       66-%{fontconf}-sans-khmer.conf
Source25:       66-%{fontconf}-sans-khmer-ui.conf
Source26:       66-%{fontconf}-sans-lao.conf
Source27:       66-%{fontconf}-sans-lao-ui.conf
Source28:       66-%{fontconf}-sans-lisu.conf
Source29:       66-%{fontconf}-sans-lycian.conf
Source30:       66-%{fontconf}-sans-lydian.conf
Source31:       66-%{fontconf}-sans-malayalam.conf
Source32:       66-%{fontconf}-sans-malayalam-ui.conf
Source33:       66-%{fontconf}-sans-mandaic.conf
Source34:       66-%{fontconf}-sans-meetei-mayek.conf
Source35:       66-%{fontconf}-sans-nko.conf
Source36:       66-%{fontconf}-sans-old-south-arabian.conf
Source37:       66-%{fontconf}-sans-old-turkic.conf
Source38:       66-%{fontconf}-sans-osmanya.conf
Source39:       66-%{fontconf}-sans-phoenician.conf
Source40:       66-%{fontconf}-sans-shavian.conf
Source41:       66-%{fontconf}-sans-symbols.conf
Source42:       66-%{fontconf}-sans-tagalog.conf
Source43:       66-%{fontconf}-sans-tai-tham.conf
Source44:       66-%{fontconf}-sans-tamil.conf
Source45:       66-%{fontconf}-sans-tamil-ui.conf
Source46:       66-%{fontconf}-sans-telugu.conf
Source47:       66-%{fontconf}-sans-thai.conf
Source48:       66-%{fontconf}-sans-thai-ui.conf
Source49:       66-%{fontconf}-sans-ugaritic.conf
Source50:       66-%{fontconf}-sans-ui.conf
Source51:       66-%{fontconf}-sans-vai.conf
Source52:       66-%{fontconf}-serif-armenian.conf
Source53:       66-%{fontconf}-serif.conf
Source54:       66-%{fontconf}-serif-georgian.conf
Source55:       66-%{fontconf}-serif-khmer.conf
Source56:       66-%{fontconf}-serif-lao.conf
Source57:       66-%{fontconf}-serif-thai.conf
Source58:       66-%{fontconf}-sans-kannada-ui.conf
Source59:       66-%{fontconf}-sans-telugu-ui.conf
Source60:       66-%{fontconf}-sans-gujarati.conf
Source61:       66-%{fontconf}-sans-gujarati-ui.conf
Source62:       66-%{fontconf}-sans-hanunoo.conf
Source63:       66-%{fontconf}-sans-tai-viet.conf
Source64:       66-%{fontconf}-kufi-arabic.conf
Source65:       66-%{fontconf}-naskh-arabic.conf
Source66:       66-%{fontconf}-naskh-arabic-ui.conf
Source67:       66-%{fontconf}-sans-balinese.conf
Source68:       66-%{fontconf}-sans-bamum.conf
Source69:       66-%{fontconf}-sans-batak.conf
Source70:       66-%{fontconf}-sans-buginese.conf
Source71:       66-%{fontconf}-sans-buhid.conf
Source72:       66-%{fontconf}-sans-canadian-aboriginal.conf
Source73:       66-%{fontconf}-sans-cham.conf
Source74:       66-%{fontconf}-sans-cuneiform.conf
Source75:       66-%{fontconf}-sans-cypriot.conf
Source76:       66-%{fontconf}-sans-gothic.conf
Source77:       66-%{fontconf}-sans-gurmukhi.conf
Source78:       66-%{fontconf}-sans-gurmukhi-ui.conf
Source79:       66-%{fontconf}-sans-inscriptional-pahlavi.conf
Source80:       66-%{fontconf}-sans-inscriptional-parthian.conf
Source81:       66-%{fontconf}-sans-javanese.conf
Source82:       66-%{fontconf}-sans-lepcha.conf
Source83:       66-%{fontconf}-sans-limbu.conf
Source84:       66-%{fontconf}-sans-linear-b.conf
Source85:       66-%{fontconf}-sans-mongolian.conf
Source86:       66-%{fontconf}-sans-myanmar.conf
Source87:       66-%{fontconf}-sans-myanmar-ui.conf
Source88:       66-%{fontconf}-sans-new-tai-lue.conf
Source89:       66-%{fontconf}-sans-ogham.conf
Source90:       66-%{fontconf}-sans-ol-chiki.conf
Source91:       66-%{fontconf}-sans-old-italic.conf
Source92:       66-%{fontconf}-sans-old-persian.conf
Source93:       66-%{fontconf}-sans-phags-pa.conf
Source94:       66-%{fontconf}-sans-rejang.conf
Source95:       66-%{fontconf}-sans-runic.conf
Source96:       66-%{fontconf}-sans-samaritan.conf
Source97:       66-%{fontconf}-sans-saurashtra.conf
Source98:       65-%{fontconf}-sans-sinhala.conf
Source99:       66-%{fontconf}-sans-sundanese.conf
Source100:      66-%{fontconf}-sans-syloti-nagri.conf
Source101:      66-%{fontconf}-sans-syriac-eastern.conf
Source102:      66-%{fontconf}-sans-syriac-estrangela.conf
Source103:      66-%{fontconf}-sans-syriac-western.conf
Source104:      66-%{fontconf}-sans-tai-le.conf
Source105:      66-%{fontconf}-sans-tifinagh.conf
Source106:      66-%{fontconf}-sans-yi.conf
Source107:      66-%{fontconf}-sans-tagbanwa.conf
Source108:      66-%{fontconf}-sans-thaana.conf

Source156:      66-%{fontconf}-sans-oriya.conf
Source157:      66-%{fontconf}-sans-oriya-ui.conf
Source158:      66-%{fontconf}-nastaliq-urdu.conf
Source159:      66-%{fontconf}-sans-tibetan.conf
Source160:      66-%{fontconf}-mono.conf
Source161:      66-%{fontconf}-serif-bengali.conf
Source162:      66-%{fontconf}-serif-devanagari.conf
Source163:      66-%{fontconf}-serif-gujarati.conf
Source164:      66-%{fontconf}-serif-kannada.conf
Source165:      66-%{fontconf}-serif-malayalam.conf
Source166:      66-%{fontconf}-serif-tamil.conf
Source167:      66-%{fontconf}-serif-telugu.conf

# Add appstream metadata files
Source200:      %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
%common_desc


%package common
Summary:        Common files for Noto fonts

%description common
Common files for Google Noto fonts.

# notopkg [-c] [-a AltFontName] [-o old-name] Font Name
# -c is for *.*tc fonts instead of *.*tf
# -a overrides the FontName
# -o adds an obsoletes for an older package name
# -p overrides fontconfig .conf priority (default 66)
%define notopkg(ca:o:p:)\
%define pname %(echo %{*} | tr "A-Z " "a-z-")\
%{!-a:%define fname %(echo %{*} | sed -e "s/ //g")}\
%define subpkg %{fontname}-%{pname}\
%define fconf %{-p*}%{!-p:66}-%{fontconf}-%{pname}.conf\
%package -n %{subpkg}-fonts\
Summary:        %{*} font\
Requires:       fontpackages-filesystem\
Requires:       %{name}-common = %{version}-%{release}\
%{?-o:Obsoletes:      %{fontname}-%{-o*}-fonts < %{version}-%{release}}\
\
%description -n %{subpkg}-fonts\
%common_desc\
Noto %1 font%{?2: for %(echo %* | sed -e "s/%1 //")}.\
\
%post -n %{subpkg}-fonts \
if [ -x %{_bindir}/fc-cache ]; then \
    %{_bindir}/fc-cache %{_fontdir} || : \
fi \
\
%postun -n %{subpkg}-fonts  \
if [ $1 -eq 0 -a -x %{_bindir}/fc-cache ] ; then \
    %{_bindir}/fc-cache %{_fontdir} || : \
fi\
\
%_font_pkg -n %{pname} -f %{fconf} Noto%{-a*}%{!-a:%{fname}}*.*t%{-c:c}%{!-c:f}\
%{_datadir}/appdata/%{subpkg}.metainfo.xml


%notopkg Kufi Arabic
%notopkg Naskh Arabic
%notopkg Naskh Arabic UI
%notopkg Sans
%notopkg Sans UI
%notopkg Sans Armenian
%notopkg Sans Avestan
%notopkg Sans Balinese
%notopkg Sans Bamum
%notopkg Sans Batak
%notopkg Sans Bengali
%notopkg Sans Bengali UI
%notopkg Sans Brahmi
%notopkg Sans Buginese
%notopkg Sans Buhid
%notopkg Sans Canadian Aboriginal
%notopkg Sans Carian
%notopkg Sans Cham
%notopkg Sans Cherokee
%notopkg Sans Coptic
%notopkg Sans Cuneiform
%notopkg Sans Cypriot
%notopkg Sans Deseret
%notopkg Sans Devanagari
%notopkg Sans Devanagari UI
%notopkg Sans Egyptian Hieroglyphs
%notopkg Sans Ethiopic
%notopkg Sans Georgian
%notopkg Sans Glagolitic
%notopkg Sans Gothic
%notopkg Sans Gujarati
%notopkg Sans Gujarati UI
%notopkg Sans Gurmukhi
%notopkg Sans Gurmukhi UI
%notopkg -o sans-hanunno Sans Hanunoo
%notopkg Sans Hebrew
%notopkg Sans Imperial Aramaic
%notopkg Sans Inscriptional Pahlavi
%notopkg Sans Inscriptional Parthian
%notopkg Sans Javanese
%notopkg Sans Kaithi
%notopkg Sans Kannada
%notopkg Sans Kannada UI
%notopkg Sans Kayah Li
%notopkg Sans Kharoshthi
%notopkg Sans Khmer
%notopkg Sans Khmer UI
%notopkg Sans Lao
%notopkg Sans Lao UI
%notopkg Sans Lepcha
%notopkg Sans Limbu
%notopkg -o sans-linearb Sans Linear B
%notopkg Sans Lisu
%notopkg Sans Lycian
%notopkg Sans Lydian
%notopkg Sans Malayalam
%notopkg Sans Malayalam UI
%notopkg Sans Mandaic
%notopkg -o sans-meeteimayek Sans Meetei Mayek
%notopkg Sans Mongolian
%notopkg Sans Myanmar
%notopkg Sans Myanmar UI
%notopkg Sans New Tai Lue
%notopkg Sans NKo
%notopkg Sans Ogham
%notopkg Sans Ol Chiki
%notopkg Sans Old Italic
%notopkg Sans Old Persian
%notopkg Sans Old South Arabian
%notopkg Sans Old Turkic
%notopkg Sans Osmanya
%notopkg Sans Phags Pa
%notopkg Sans Phoenician
%notopkg Sans Rejang
%notopkg Sans Runic
%notopkg Sans Shavian
%notopkg Sans Samaritan
%notopkg Sans Saurashtra
%notopkg -p 65 Sans Sinhala
%notopkg Sans Sundanese
%notopkg Sans Syloti Nagri
%notopkg Sans Symbols
%notopkg Sans Syriac Eastern
%notopkg Sans Syriac Estrangela
%notopkg Sans Syriac Western
%notopkg Sans Tagalog
%notopkg Sans Tagbanwa
%notopkg Sans Tai Le
%notopkg Sans Tai Tham
%notopkg Sans Tai Viet
%notopkg Sans Tamil
%notopkg Sans Tamil UI
%notopkg Sans Telugu
%notopkg Sans Telugu UI
%notopkg Sans Thaana
%notopkg Sans Thai
%notopkg Sans Thai UI
%notopkg Sans Tifinagh
%notopkg Sans Ugaritic
%notopkg Sans Vai
%notopkg Sans Yi
%notopkg Serif
%notopkg Serif Armenian
%notopkg Serif Georgian
%notopkg Serif Khmer
%notopkg Serif Lao
%notopkg Serif Thai
%notopkg Sans Oriya
%notopkg Sans Oriya UI
%notopkg Sans Tibetan
%notopkg Nastaliq Urdu
%notopkg Mono
%notopkg Serif Bengali
%notopkg Serif Devanagari
%notopkg Serif Gujarati
%notopkg Serif Kannada
%notopkg Serif Malayalam
%notopkg Serif Tamil
%notopkg Serif Telugu


%prep
%setup -q -n noto-fonts-86b2e553c3e3e4d6614dadd1fa0a7a6dafd74552


%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p unhinted/Noto*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p hinted/Noto*.ttf %{buildroot}%{_fontdir}



install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Add appstream metadata
install -Dm 0644 -p %{SOURCE200} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

for f in \
        kufi-arabic naskh-arabic naskh-arabic-ui \
        sans sans-armenian sans-avestan sans-balinese sans-bamum \
        sans-batak sans-bengali sans-bengali-ui sans-brahmi \
        sans-buginese sans-buhid sans-canadian-aboriginal sans-carian \
        sans-cham sans-cherokee sans-coptic sans-cuneiform \
        sans-cypriot sans-deseret sans-devanagari sans-devanagari-ui \
        sans-egyptian-hieroglyphs sans-ethiopic sans-georgian \
        sans-glagolitic sans-gothic sans-gujarati sans-gujarati-ui \
        sans-gurmukhi sans-gurmukhi-ui sans-hanunoo sans-hebrew \
        sans-imperial-aramaic sans-inscriptional-pahlavi \
        sans-inscriptional-parthian sans-javanese \
        sans-kaithi sans-kannada sans-kannada-ui sans-kayah-li \
        sans-kharoshthi sans-khmer sans-khmer-ui sans-lao \
        sans-lao-ui sans-lepcha sans-limbu sans-linear-b sans-lisu \
        sans-lycian sans-lydian sans-malayalam sans-malayalam-ui \
        sans-mandaic sans-meetei-mayek sans-mongolian sans-myanmar \
        sans-myanmar-ui sans-new-tai-lue sans-nko sans-ogham \
        sans-ol-chiki sans-old-italic sans-old-persian \
        sans-old-south-arabian sans-old-turkic sans-osmanya \
        sans-phags-pa sans-phoenician sans-rejang sans-runic \
        sans-samaritan sans-saurashtra sans-shavian sans-sinhala \
        sans-sundanese sans-syloti-nagri sans-symbols sans-syriac-eastern \
        sans-syriac-estrangela sans-syriac-western sans-tagalog \
        sans-tagbanwa sans-tai-le sans-tai-tham sans-tai-viet \
        sans-tamil sans-tamil-ui sans-telugu sans-telugu-ui \
        sans-thaana sans-thai sans-thai-ui sans-tifinagh \
        sans-ugaritic sans-ui sans-vai sans-yi \
        serif serif-armenian serif-georgian serif-khmer serif-lao serif-thai \
        sans-oriya sans-oriya-ui sans-tibetan nastaliq-urdu mono \
        serif-bengali serif-devanagari serif-gujarati serif-kannada \
        serif-malayalam serif-tamil serif-telugu \
        ; do
  fconf=$(basename -a %{_sourcedir}/*-%{fontconf}-$f.conf)
  if [ "$(echo $fconf | wc -w)" -ne 1 ]; then
     echo "Did not find unique \*-%{fontconf}-$f.conf file"
     exit 1
  fi
  install -m 0644 -p %{_sourcedir}/${fconf} \
        %{buildroot}%{_fontconfig_templatedir}/${fconf}
  ln -s %{_fontconfig_templatedir}/${fconf} \
        %{buildroot}%{_fontconfig_confdir}/${fconf}

  meta=%{fontname}-$f.metainfo.xml
  echo '<?xml version="1.0" encoding="UTF-8"?>' > $meta
  echo '<!-- Copyright 2014 Parag Nemade <pnemade AT redhat DOT com> -->' >> $meta
  echo '<component type="font">' >> $meta
  echo "  <id>google-noto-$f</id>" >> $meta
  echo '  <metadata_license>CC-BY-3.0</metadata_license>' >> $meta
  echo '  <extends>google-noto</extends>' >> $meta
  echo '</component>' >> $meta

  install -Dm 0644 -p %{fontname}-$f.metainfo.xml \
          %{buildroot}%{_datadir}/appdata/%{fontname}-$f.metainfo.xml
done


%files common
%license LICENSE
%doc README.md FAQ.md
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Mon Jun  8 2020 Akira TAGOH <tagoh@redhat.com> - 20161022-7.1
- Add CI tests
  Resolves: rhbz#1682152
- Fix typos in fontconfig config for Kannada
  Resolves: rhbz#1764502

* Thu Apr  5 2018 Jens Petersen <petersen@redhat.com> - 20161022-7
- change the Sinhala fontconfig priority to 65 (#1450802)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20161022-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Jens Petersen <petersen@redhat.com> - 20161022-5
- use _font_pkg

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul  5 2017 Jens Petersen <petersen@redhat.com> - 20161022-3
- add a fontconfig priority option to the notopkg macro,
  which allows overriding the default 66 priority

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Pravin Satpute <psatpute@redhat.com> - 20161022-1
- Resolves #1321685 - Added Noto Mono font.
- License changed from ASL 2.0 to OFL. 
- New package addition: Mono, Serif Bengali, Serif Devanagari
- Serif Gujarari, Serif Malayalam, Serif Tamil and Serif Telugu.

* Wed Aug 24 2016 Pravin Satpute <psatpute@redhat.com> - 20150929-2
- Resolves #1368772 - Fixes issue with LICENSE file.

* Thu Apr 28 2016 Pravin Satpute <psatpute@redhat.com> - 20150929-1
- Resolves #1269404 - Update to new git release 20150929
- Upstream divided google-noto-fonts package into noto-cjk-font and noto-emoji
- Removed packages: google-noto-color-emoji-fonts, google-noto-sans (cjk-fonts,
- japanese-fonts, simplified-chinese-fonts and traditional-chinese-fonts)
- Replaced by google-noto-cjk-fonts and google-noto-emoji-fonts
- New subpackages - google-noto-nastaliq-urdu-fonts and google-noto-sans-tibetan-fonts

* Thu Feb 04 2016 Parag Nemade <pnemade AT redhat DOT com> - 20150417-4
- Fix for python2 fonttools

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150417-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150417-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Pravin Satpute <psatpute@redhat.com> - 20150417-1
- Updating to git snapshot d47480343178.
- Remove Thaana and Oriya from under-development list.
- Add Syriac requirements from Unicode Core Specification. 

* Fri Mar 27 2015 Pravin Satpute <psatpute@redhat.com> - 20150325-1
- Updating to git snapshot 762640379a51.
- Added 2 new packages Oriya and Oriya-UI.
- Update Hebrew, Georgian, and Ethiopic fonts.
- Fix cmap of U+06F7 to Urdu form of digit 7.

* Tue Jan 13 2015 Pravin Satpute <psatpute@redhat.com> - 20141117-6
- Resolves #1162341: Packaged Noto Color Emoji

* Mon Dec 15 2014 Jens Petersen <petersen@redhat.com> - 20141117-5
- improve generated font subpackage descriptions
- it is Hanunoo not Hanuno!
- specify font filenames more precisely

* Mon Dec 15 2014 Jens Petersen <petersen@redhat.com> - 20141117-4
- add obsoletes to cover the change of package names for Hanuno, Linear B,
  and Meetei Mayek

* Tue Dec  2 2014 Jens Petersen <petersen@redhat.com> - 20141117-3
- create the fonts subpackages with a macro

* Fri Nov 21 2014 Jens Petersen <petersen@redhat.com> - 20141117-2
- move cjk fonts fontconfig priority from 65-0 to 66
- generate the appinfo metainfo for the subpackages
- use a single for-loop to install the font config and appdata files
- move parent appinfo metainfo to common (Parag Nemade)

* Thu Nov 20 2014 Jens Petersen <petersen@redhat.com> - 20141117-1
- update to latest git (aae16d0cd626)
- package Japanese, Korean, and CJK fonts
- add Thaana font
- add common subpackage for license and doc files
- order spec subpackages lexically

* Wed Nov 19 2014 Peng Wu <pwu@redhat.com> - 20141001-5
- Rename Chinese sub-packages

* Wed Nov 12 2014 Peng Wu <pwu@redhat.com> - 20141001-4
- Add Chinese fonts

* Tue Nov 11 2014 Parag Nemade <pnemade AT redhat DOT com> - 20141001-3
- Add metainfo file to show this font in gnome-software

* Mon Nov 03 2014 Pravin Satpute <psatpute@redhat.com> - 20141001-2
- Resolves #1159562: Typo in fontconfig file

* Wed Oct 01 2014 Pravin Satpute <psatpute@redhat.com> - 20141001-1
- Google stops release tarball. Zip file derived from git Download zip.
- 45 new packages added as follows.
- kufi-arabic-fonts, naskh-arabic-fonts, naskh-arabic-ui-fonts, sans-balinese-fonts, 
- sans-bamum-fonts, sans-batak-fonts, sans-buginese-fonts, sans-buhid-fonts, 
- sans-canadian-aboriginal-fonts, sans-cham-fonts, sans-cuneiform-fonts, sans-cypriot-fonts, 
- sans-gothic-fonts, sans-gurmukhi-fonts, sans-gurmukhi-ui-fonts, 
- sans-inscriptional-pahlavi-fonts, sans-inscriptional-parthian-fonts, sans-javanese-fonts, 
- sans-lepcha-fonts, sans-limbu-fonts, sans-linearb-fonts, sans-mongolian-fonts, 
- sans-myanmar-fonts, sans-myanmar-ui-fonts, sans-new-tai-lue-fonts, sans-ogham-fonts, 
- sans-ol-chiki-fonts, sans-old-italic-fonts, sans-old-persian-fonts, sans-phags-pa-fonts, 
- sans-rejang-fonts, sans-runic-fonts, sans-samaritan-fonts, sans-saurashtra-fonts, 
- sans-sinhala-fonts, sans-sundanese-fonts, sans-syloti-nagri-fonts, sans-syriac-eastern-fonts, 
- sans-syriac-estrangela-fonts, sans-syriac-western-fonts, sans-tagbanwa-fonts, 
- sans-tai-le-fonts, sans-tifinagh-fonts, sans-yi-fonts
- Resolves #1148413

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130807-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Pravin Satpute <psatpute@redhat.com> - 20130807-1
- Upstream new release of 20130807 tarball.
- Packages Non Hinted upstream tarball.
- This pulled fonts for number of missing Unicode scripts in Fedora

* Tue Jul 16 2013 Pravin Satpute <psatpute@redhat.com> - 20130624-1
- Resolved #984459 :- Upstream new release.
- Added new package google-noto-serif-khmer-fonts

* Mon Jun 24 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-5
- Resolved #971886 :- Georgian Serif fontconfig file error  

* Mon Jun 10 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-4
- Resolved #971886 :- Georgian fontconfig file error 

* Mon May 06 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-3
- Initial import
- Updated spec file

* Fri Apr 19 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-2
- Updated package as per 3rd comment on review request #953859

* Fri Apr 19 2013 Pravin Satpute <psatpute@redhat.com> - 20130411-1
- Initial packaging
