%global cionly 0

%global _fontname google-noto
%global fontname %{_fontname}
%global fontconf %{_fontname}
%global common_desc Noto fonts aims to remove tofu from web by providing fonts for all \
Unicode supported scripts. Its design goal is to achieve visual harmonization\
between multiple scripts. Noto family supports almost all scripts available\
in Unicode.\
%{nil}

%global srcver	20201206-phase3
%global hprio	65
%global mprio	66
%global lprio	67

Name:           %{fontname}-fonts
Version:        20201206
Release:        4%{?dist}
Summary:        Hinted and Non Hinted OpenType fonts for Unicode scripts
License:        OFL
URL:            https://github.com/googlefonts/noto-fonts/
Source0:        https://github.com/googlefonts/noto-fonts/archive/v20201206-phase3.tar.gz#/noto-fonts-%{srcver}.tar.gz

BuildArch:      noarch
BuildRequires:  fonts-rpm-macros
Requires:       fontpackages-filesystem

%description
%common_desc


%package common
Summary:        Common files for Noto fonts

%description common
Common files for Google Noto fonts.

%{lua:
-- To make lua-mode happy: '
local group = {}
group["sans-serif"] = "Noto Sans"
group["serif"] = "Noto Serif"
group["monospace"] = "Noto Sans Mono"

local subpackages = {
    { alias="cursive",    family="Kufi Arabic", lang={ "ar" } },
    { alias="fantasy",    family="Music" },
    { alias="cursive",    family="Naskh Arabic", lang={ "ar" } },
    { alias="cursive",    family="Naskh Arabic UI", lang={ "ar" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="cursive",    family="Nastaliq Urdu", lang={ "ur" } },
    { alias="serif",      family="Rashi Hebrew", lang={ "he" } },
    { alias="sans-serif", family="Sans" },
    { alias="sans-serif", family="Sans Display",
      priority=rpm.expand('%{lprio}'),
      obsoletes={ "sans-ui" }
    },
    { alias="sans-serif", family="Sans Adlam" },
    { alias="sans-serif", family="Sans Adlam Unjoined" },
    { alias="sans-serif", family="Sans Anatolian Hieroglyphs" },
    { alias="sans-serif", family="Sans Arabic", lang={ "ar" } },
    { alias="sans-serif", family="Sans Arabic UI", lang={ "ar" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Armenian", lang={ "hy" } },
    { alias="sans-serif", family="Sans Avestan" },
    { alias="sans-serif", family="Sans Balinese", lang={ "ban" } },
    { alias="sans-serif", family="Sans Bamum", lang={ "bax" } },
    { alias="sans-serif", family="Sans Bassa Vah" },
    { alias="sans-serif", family="Sans Batak", lang={ "bbc" } },
    { alias="sans-serif", family="Sans Bengali", lang= { "bn" } },
    { alias="sans-serif", family="Sans Bengali UI", lang= { "bn" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Bhaiksuki" },
    { alias="sans-serif", family="Sans Brahmi" },
    { alias="sans-serif", family="Sans Buginese", lang={ "bug" } },
    { alias="sans-serif", family="Sans Buhid", lang={ "bku" } },
    { alias="sans-serif", family="Sans Canadian Aboriginal", lang={ "iu" } },
    { alias="sans-serif", family="Sans Caucasian Albanian" },
    { alias="sans-serif", family="Sans Carian" },
    { alias="sans-serif", family="Sans Chakma" },
    { alias="sans-serif", family="Sans Cham", lang={ "cjm" } },
    { alias="sans-serif", family="Sans Cherokee", lang={ "chr" } },
    { alias="sans-serif", family="Sans Coptic", lang={ "cop" } },
    { alias="sans-serif", family="Sans Cuneiform", lang={ "slv" } },
    { alias="sans-serif", family="Sans Cypriot" },
    { alias="sans-serif", family="Sans Deseret" },
    { alias="sans-serif", family="Sans Devanagari", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" } },
    { alias="sans-serif", family="Sans Devanagari UI", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Duployan" },
    { alias="sans-serif", family="Sans Egyptian Hieroglyphs" },
    { alias="sans-serif", family="Sans Elbasan" },
    { alias="sans-serif", family="Sans Elymaic" },
    { alias="sans-serif", family="Sans Ethiopic", lang={ "am", "byn", "gez", "sid", "ti-er", "ti-et", "tig", "wal" } },
    { alias="sans-serif", family="Sans Georgian", lang={ "ka" } },
    { alias="sans-serif", family="Sans Glagolitic" },
    { alias="sans-serif", family="Sans Gothic", lang={ "got" } },
    { alias="sans-serif", family="Sans Grantha" },
    { alias="sans-serif", family="Sans Gujarati", lang={ "gu" } },
    { alias="sans-serif", family="Sans Gujarati UI", lang={ "gu" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Gunjala Gondi" },
    { alias="sans-serif", family="Sans Gurmukhi", lang={ "pa" },
      priority=rpm.expand('%{hprio}')
    },
    { alias="sans-serif", family="Sans Gurmukhi UI", lang={ "pa" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Hanifi Rohingya" },
    { alias="sans-serif", family="Sans Hanunoo", lang={ "hnn" },
      obsoletes={ "sans-hanunno" }
    },
    { alias="sans-serif", family="Sans Hatran" },
    { alias="sans-serif", family="Sans Hebrew", lang={ "he" } },
    { alias="sans-serif", family="Sans Imperial Aramaic" },
    { alias="sans-serif", family="Sans Indic Siyaq Numbers" },
    { alias="sans-serif", family="Sans Inscriptional Pahlavi" },
    { alias="sans-serif", family="Sans Inscriptional Parthian" },
    { alias="sans-serif", family="Sans Javanese" },
    { alias="sans-serif", family="Sans Kaithi" },
    { alias="sans-serif", family="Sans Kannada", lang={ "kn" } },
    { alias="sans-serif", family="Sans Kannada UI", lang={ "kn" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Kayah Li" },
    { alias="sans-serif", family="Sans Kharoshthi" },
    { alias="sans-serif", family="Sans Khmer", lang={ "km" } },
    { alias="sans-serif", family="Sans Khmer UI", lang={ "km" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Khojki" },
    { alias="sans-serif", family="Sans Khudawadi" },
    { alias="sans-serif", family="Sans Lao", lang={ "lo" } },
    { alias="sans-serif", family="Sans Lao Looped", lang={ "lo" } },
    { alias="sans-serif", family="Sans Lao UI", lang={ "lo" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Lepcha", lang={ "lep" } },
    { alias="sans-serif", family="Sans Limbu", lang={ "lif" } },
    { alias="sans-serif", family="Sans Linear A" },
    { alias="sans-serif", family="Sans Linear B",
      obsoletes={ "sans-linearb" }
    },
    { alias="sans-serif", family="Sans Lisu" },
    { alias="sans-serif", family="Sans Lycian" },
    { alias="sans-serif", family="Sans Lydian" },
    { alias="sans-serif", family="Sans Mahajani" },
    { alias="sans-serif", family="Sans Malayalam", lang={ "ml" } },
    { alias="sans-serif", family="Sans Malayalam UI", lang={ "ml" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Mandaic" },
    { alias="sans-serif", family="Sans Manichaean" },
    { alias="sans-serif", family="Sans Marchen" },
    { alias="sans-serif", family="Sans Masaram Gondi" },
    { alias="sans-serif", family="Sans Math",
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Mayan Numerals" },
    { alias="sans-serif", family="Sans Meetei Mayek",
      obsoletes={ "sans-meeteimayek" }
    },
    { alias="sans-serif", family="Sans Medefaidrin" },
    { alias="sans-serif", family="Sans Mende Kikakui" },
    { alias="sans-serif", family="Sans Meroitic" },
    { alias="sans-serif", family="Sans Miao" },
    { alias="sans-serif", family="Sans Modi" },
    { alias="sans-serif", family="Sans Mongolian", lang={ "mn-cn" } },
    { alias="monospace",  family="Sans Mono",
      obsoletes={ "mono" }
    },
    { alias="sans-serif", family="Sans Mro" },
    { alias="sans-serif", family="Sans Multani" },
    { alias="sans-serif", family="Sans Myanmar", lang={ "my" } },
    { alias="sans-serif", family="Sans Myanmar UI", lang={ "my" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Nabataean" },
    { alias="sans-serif", family="Sans New Tai Lue", lang={ "khb" } },
    { alias="sans-serif", family="Sans Newa" },
    { alias="sans-serif", family="Sans NKo", lang={ "nqo" } },
    { alias="sans-serif", family="Sans Nushu" },
    { alias="sans-serif", family="Sans Ogham", lang={ "pgl" } },
    { alias="sans-serif", family="Sans Ol Chiki" },
    { alias="sans-serif", family="Sans Old Hungarian" },
    { alias="sans-serif", family="Sans Old Italic" },
    { alias="sans-serif", family="Sans Old North Arabian" },
    { alias="sans-serif", family="Sans Old Permic" },
    { alias="sans-serif", family="Sans Old Persian" },
    { alias="sans-serif", family="Sans Old Sogdian" },
    { alias="sans-serif", family="Sans Old South Arabian" },
    { alias="sans-serif", family="Sans Old Turkic" },
    { alias="sans-serif", family="Sans Oriya", lang={ "or" } },
    { alias="sans-serif", family="Sans Oriya UI", lang={ "or" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Osage" },
    { alias="sans-serif", family="Sans Osmanya" },
    { alias="sans-serif", family="Sans Pahawh Hmong" },
    { alias="sans-serif", family="Sans Palmyrene" },
    { alias="sans-serif", family="Sans Pau Cin Hau" },
    { alias="sans-serif", family="Sans Phags Pa" },
    { alias="sans-serif", family="Sans Phoenician" },
    { alias="sans-serif", family="Sans Psalter Pahlavi" },
    { alias="sans-serif", family="Sans Rejang", lang={ "rej" } },
    { alias="sans-serif", family="Sans Runic", lang={ "gem" } },
    { alias="sans-serif", family="Sans Samaritan" },
    { alias="sans-serif", family="Sans Saurashtra", lang={ "saz" } },
    { alias="sans-serif", family="Sans Sharada" },
    { alias="sans-serif", family="Sans Shavian", lang={ "en@shaw" } },
    { alias="sans-serif", family="Sans Siddham" },
    { alias="sans-serif", family="Sans SignWriting" },
    { alias="sans-serif", family="Sans Sinhala", lang={ "si" } },
    { alias="sans-serif", family="Sans Sinhala UI", lang={ "si" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Sogdian" },
    { alias="sans-serif", family="Sans Sora Sompeng" },
    { alias="sans-serif", family="Sans Soyombo" },
    { alias="sans-serif", family="Sans Sundanese" },
    { alias="sans-serif", family="Sans Syloti Nagri" },

    { alias="fantasy",    family="Sans Symbols" },
    { alias="fantasy",    family="Sans Symbols2" },

    { alias="sans-serif", family="Sans Syriac", lang={ "syr" },
      obsoletes={ "sans-syriac-eastern", "sans-syriac-estrangela", "sans-syriac-western" }
    },
    { alias="sans-serif", family="Sans Tagalog" },
    { alias="sans-serif", family="Sans Tagbanwa", lang={ "twb" } },
    { alias="sans-serif", family="Sans Takri" },
    { alias="sans-serif", family="Sans Tai Le" },
    { alias="sans-serif", family="Sans Tai Tham" },
    { alias="sans-serif", family="Sans Tai Viet" },
    { alias="sans-serif", family="Sans Tamil", lang={ "ta" } },
    { alias="sans-serif", family="Sans Tamil Supplement", lang={ "ta" },
      excludeci=true
    },
    { alias="sans-serif", family="Sans Tamil UI", lang={ "ta" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Telugu", lang={ "te" } },
    { alias="sans-serif", family="Sans Telugu UI", lang={ "te" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Thaana", lang={ "dv" } },
    { alias="sans-serif", family="Sans Thai", lang={ "th" } },
    { alias="sans-serif", family="Sans Thai Looped", lang={ "th" } },
    { alias="sans-serif", family="Sans Thai UI", lang={ "th" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", family="Sans Tifinagh", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh APT", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Adrar", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Agraw Imazighen", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Ahaggar", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Air", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Azawagh", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Ghat", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Hawad", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Rhissa Ixa", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh SIL", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Tawellemmet", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tirhuta" },
    { alias="sans-serif", family="Sans Ugaritic" },
    { alias="sans-serif", family="Sans Vai", lang={ "vai" } },
    { alias="sans-serif", family="Sans Wancho" },
    { alias="sans-serif", family="Sans Warang Citi" },
    { alias="sans-serif", family="Sans Yi" },
    { alias="sans-serif", family="Sans Zanabazar Square" },

    { alias="serif",      family="Serif" },
    { alias="serif",      family="Serif Ahom" },
    { alias="serif",      family="Serif Armenian", lang={ "hy" } },
    { alias="serif",      family="Serif Balinese", lang={ "ban" },
      obsoletes={ "sans-balinese" }
    },
    { alias="serif",      family="Serif Bengali", lang={ "bn" } },
    { alias="serif",      family="Serif Devanagari", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" } },
    { alias="serif",      family="Serif Display",
      priority=rpm.expand('%{lprio}')
    },
    { alias="serif",      family="Serif Dogra" },
    { alias="serif",      family="Serif Ethiopic", lang={ "am", "byn", "gez", "sid", "ti-er", "ti-et", "tig", "wal" } },
    { alias="serif",      family="Serif Georgian", lang={ "ka" } },
    { alias="serif",      family="Serif Grantha" },
    { alias="serif",      family="Serif Gujarati", lang={ "gu" } },
    { alias="serif",      family="Serif Gurmukhi", lang={ "pa" } },
    { alias="serif",      family="Serif Hebrew", lang={ "he" } },
    { alias="serif",      family="Serif Kannada", lang={ "kn" } },
    { alias="serif",      family="Serif Khmer", lang={ "km" } },
    { alias="serif",      family="Serif Khojki" },
    { alias="serif",      family="Serif Lao", lang={ "lo" } },
    { alias="serif",      family="Serif Malayalam", lang={ "ml" } },
    { alias="serif",      family="Serif Myanmar", lang={ "my" } },
    { alias="serif",      family="Serif Nyiakeng Puachue Hmong" },
    { alias="serif",      family="Serif Sinhala", lang={ "si" } },
    { alias="serif",      family="Serif Tamil", lang={ "ta" } },
    { alias="serif",      family="Serif Tamil Slanted", lang={ "ta" } },
    { alias="serif",      family="Serif Tangut" },
    { alias="serif",      family="Serif Telugu", lang={ "te" } },
    { alias="serif",      family="Serif Thai", lang={ "th" } },
    { alias="serif",      family="Serif Tibetan", lang={ "bo", "dz" },
      obsoletes={ "sans-tibetan" }
    },
    { alias="serif",      family="Serif Yezidi" },
    { alias="serif",      family="Traditional Nushu" },

    { alias="cursive",    variable=true, family="Kufi Arabic", lang={ "ar" } },
    { alias="cursive",    variable=true, family="Naskh Arabic", lang={ "ar" } },
    { alias="cursive",    variable=true, family="Naskh Arabic UI", lang={ "ar" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="serif",      variable=true, family="Rashi Hebrew", lang={ "he" } },
    { alias="sans-serif", variable=true, family="Sans" },
    { alias="sans-serif", variable=true, family="Sans Adlam" },
    { alias="sans-serif", variable=true, family="Sans Adlam Unjoined" },
    { alias="sans-serif", variable=true, family="Sans Anatolian Hieroglyphs" },
    { alias="sans-serif", variable=true, family="Sans Arabic", lang={ "ar" } },
    { alias="sans-serif", variable=true, family="Sans Arabic UI", lang={ "ar" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Armenian", lang={ "hy" } },
    { alias="sans-serif", variable=true, family="Sans Avestan" },
    { alias="sans-serif", variable=true, family="Sans Balinese", lang={ "ban" } },
    { alias="sans-serif", variable=true, family="Sans Bamum", lang={ "bax" } },
    { alias="sans-serif", variable=true, family="Sans Bassa Vah" },
    { alias="sans-serif", variable=true, family="Sans Bengali", lang={ "bn" } },
    { alias="sans-serif", variable=true, family="Sans Bengali UI", lang={ "bn" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Buginese", lang={ "bug" } },
    { alias="sans-serif", variable=true, family="Sans Buhid", lang={ "bku" } },
    { alias="sans-serif", variable=true, family="Sans Canadian Aboriginal", lang={ "iu" } },
    { alias="sans-serif", variable=true, family="Sans Carian" },
    { alias="sans-serif", variable=true, family="Sans Cham", lang={ "cjm" } },
    { alias="sans-serif", variable=true, family="Sans Cherokee", lang={ "chr" } },
    { alias="sans-serif", variable=true, family="Sans Cuneiform", lang={ "slv" } },
    { alias="sans-serif", variable=true, family="Sans Cypriot" },
    { alias="sans-serif", variable=true, family="Sans Deseret" },
    { alias="sans-serif", variable=true, family="Sans Devanagari", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" } },
    { alias="sans-serif", variable=true, family="Sans Devanagari UI", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Display",
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Egyptian Hieroglyphs" },
    { alias="sans-serif", variable=true, family="Sans Elymaic" },
    { alias="sans-serif", variable=true, family="Sans Ethiopic", lang={ "am", "byn", "gez", "sid", "ti-er", "ti-et", "tig", "wal" } },
    { alias="sans-serif", variable=true, family="Sans Georgian", lang={ "ka" } },
    { alias="sans-serif", variable=true, family="Sans Gothic", lang={ "got" } },
    { alias="sans-serif", variable=true, family="Sans Gurmukhi", lang={ "pa" } },
    { alias="sans-serif", variable=true, family="Sans Gurmukhi UI", lang={ "pa" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Hanifi Rohingya" },
    { alias="sans-serif", variable=true, family="Sans Hatran" },
    { alias="sans-serif", variable=true, family="Sans Hebrew", lang={ "he" } },
    { alias="sans-serif", variable=true, family="Sans Imperial Aramaic" },
    { alias="sans-serif", variable=true, family="Sans Kannada", lang={ "kn" } },
    { alias="sans-serif", variable=true, family="Sans Kannada UI", lang={ "kn" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Kayah Li" },
    { alias="sans-serif", variable=true, family="Sans Khmer", lang={ "km" } },
    { alias="sans-serif", variable=true, family="Sans Khmer UI", lang={ "km" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Lao", lang={ "lo" } },
    { alias="sans-serif", variable=true, family="Sans Lao Looped", lang={ "lo" } },
    { alias="sans-serif", variable=true, family="Sans Lao UI", lang={ "lo" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Linear A" },
    { alias="sans-serif", variable=true, family="Sans Linear B" },
    { alias="sans-serif", variable=true, family="Sans Lisu" },
    { alias="sans-serif", variable=true, family="Sans Lycian" },
    { alias="sans-serif", variable=true, family="Sans Lydian" },
    { alias="sans-serif", variable=true, family="Sans Malayalam", lang={ "ml" } },
    { alias="sans-serif", variable=true, family="Sans Malayalam UI", lang={ "ml" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Mandaic" },
    { alias="sans-serif", variable=true, family="Sans Marchen" },
    { alias="sans-serif", variable=true, family="Sans Math" },
    { alias="sans-serif", variable=true, family="Sans Mayan Numerals" },
    { alias="sans-serif", variable=true, family="Sans Medefaidrin" },
    { alias="sans-serif", variable=true, family="Sans MeeteiMayek" },
    { alias="monospace", variable=true, family="Sans Mono" },
    { alias="sans-serif", variable=true, family="Sans Mro" },
    { alias="sans-serif", variable=true, family="Sans Multani" },
    { alias="sans-serif", variable=true, family="Sans Myanmar", lang={ "my" },
      obsoletes={ "serif-myanmar-vf" }
    },
    { alias="sans-serif", variable=true, family="Sans Myanmar UI", lang={ "my" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Nabataean" },
    { alias="sans-serif", variable=true, family="Sans New Tai Lue", lang={ "khb" } },
    { alias="sans-serif", variable=true, family="Sans Ogham", lang={ "pgl" } },
    { alias="sans-serif", variable=true, family="Sans Ol Chiki" },
    { alias="sans-serif", variable=true, family="Sans Osmanya" },
    { alias="sans-serif", variable=true, family="Sans Phoenician" },
    { alias="sans-serif", variable=true, family="Sans Runic", lang={ "gem" } },
    { alias="sans-serif", variable=true, family="Sans Shavian", lang={ "en@shaw" } },
    { alias="sans-serif", variable=true, family="Sans Sinhala", lang={ "si" },
      priority=rpm.expand('%{hprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Sinhala UI", lang={ "si" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Sora Sompeng" },
    { alias="sans-serif", variable=true, family="Sans Soyombo" },
    { alias="sans-serif", variable=true, family="Sans Sundanese" },
    { alias="fantasy",    variable=true, family="Sans Symbols" },
    { alias="sans-serif", variable=true, family="Sans Tagbanwa", lang={ "twb" } },
    { alias="sans-serif", variable=true, family="Sans Tai Tham" },
    { alias="sans-serif", variable=true, family="Sans Takri" },
    { alias="sans-serif", variable=true, family="Sans Tamil", lang={ "ta" } },
    { alias="sans-serif", variable=true, family="Sans Tamil Supplement", lang={ "ta" },
      excludeci=true
    },
    { alias="sans-serif", variable=true, family="Sans Tamil UI", lang={ "ta" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Telugu", lang={ "te" } },
    { alias="sans-serif", variable=true, family="Sans Telugu UI", lang={ "te" },
      priority=rpm.expand('%{lprio}')
    },
    { alias="sans-serif", variable=true, family="Sans Thaana", lang={ "dv" } },
    { alias="sans-serif", variable=true, family="Sans Thai", lang={ "th" } },
    { alias="sans-serif", variable=true, family="Sans Thai UI", lang={ "th" } },
    { alias="sans-serif", variable=true, family="Sans Ugaritic" },
    { alias="sans-serif", variable=true, family="Sans Vai", lang={ "vai" } },
    { alias="sans-serif", variable=true, family="Sans Wancho" },
    { alias="sans-serif", variable=true, family="Sans Warang Citi" },
    { alias="sans-serif", variable=true, family="Sans Yi" },
    { alias="sans-serif", variable=true, family="Sans Zanabazar Square" },
    { alias="sans-serif", variable=true, family="SansThai Looped", lang={ "th" } },
    { alias="serif",      variable=true, family="Serif" },
    { alias="serif",      variable=true, family="Serif Armenian", lang={ "hy" } },
    { alias="serif",      variable=true, family="Serif Bengali", lang={ "bn" } },
    { alias="serif",      variable=true, family="Serif Devanagari", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" } },
    { alias="serif",      variable=true, family="Serif Display",
      priority=rpm.expand('%{lprio}')
    },
    { alias="serif",      variable=true, family="Serif Ethiopic", lang={ "am", "byn", "gez", "sid", "ti-er", "ti-et", "tig", "wal" } },
    { alias="serif",      variable=true, family="Serif Georgian", lang={ "ka" } },
    { alias="serif",      variable=true, family="Serif Gujarati", lang={ "gu" } },
    { alias="serif",      variable=true, family="Serif Gurmukhi", lang={ "pa" } },
    { alias="serif",      variable=true, family="Serif Hebrew", lang={ "he" } },
    { alias="serif",      variable=true, family="Serif Kannada", lang={ "kn" } },
    { alias="serif",      variable=true, family="Serif Khmer", lang={ "km" } },
    { alias="serif",      variable=true, family="Serif Khojki" },
    { alias="serif",      variable=true, family="Serif Lao", lang={ "lo" } },
    { alias="serif",      variable=true, family="Serif Malayalam", lang={ "ml" } },
    { alias="serif",      variable=true, family="Serif Nyiakeng Puachue Hmong" },
    { alias="serif",      variable=true, family="Serif Sinhala", lang={ "si" } },
    { alias="serif",      variable=true, family="Serif Tamil", lang={ "ta" } },
    { alias="serif",      variable=true, family="Serif Tamil Slanted", lang={ "ta" } },
    { alias="serif",      variable=true, family="Serif Tangut" },
    { alias="serif",      variable=true, family="Serif Telugu", lang={ "te" } },
    { alias="serif",      variable=true, family="Serif Thai", lang={ "th" } },
    { alias="serif",      variable=true, family="Serif Tibetan", lang={ "bo", "dz" } },
    { alias="serif",      variable=true, family="Serif Yezidi" }

}
local _fcconflist = ''
local _metafilelist = ''
local _fcconfbuild = ''
local _metainfobuild = ''

local function genfcconf(table)
    local generic = [[
    <test name="family">\
      <string>]] .. table.alias .. [[</string>\
    </test>\
    <edit name=\"family\" mode=\"prepend\">\
      <string>Noto ]] .. table.family .. [[</string>\
    </edit>\
    <edit name=\"fonthashint\" mode=\"append\">\
      <bool>]] .. (table.variable and "true" or "false") .. [[</bool>\
    </edit>\]]
    local xml = [[
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
<!DOCTYPE fontconfig SYSTEM \"urn:fontconfig:fonts.dtd\">\
<fontconfig>\
]]
    if table.lang then
        for i = 1, #table.lang do
	    xml = xml .. [[  <match>\
    <test name=\"lang\" compare=\"contains\">\
      <string>]] .. table.lang[i] .. [[</string>\
    </test>\
]] .. generic .. "\n" .. [[
  </match>\
]]
	end
    else
        xml = xml .. [[  <match>\
]] .. generic .. "\n" .. [[
  </match>\
]]
    end
    xml = xml .. [[
  <alias>\
    <family>Noto ]] .. table.family .. [[</family>\
    <default>\
      <family>]] .. table.alias .. [[</family>\
    </default>\
  </alias>\
</fontconfig>\]]
    _fcconfbuild = (_fcconfbuild ~= '' and _fcconfbuild .. "\n" or '') .. "cat<<_EOL_>" .. table.fcconf .. "\\\n" .. xml .. "\n_EOL_\\"
end

-- Borrowed from fonts-rpm-macros
-- koji doesn't sasisfy BR during generating srpm yet.
-- We can't add a dependant code to fonts-rpm-macros at this stage.

-- https://github.com/rpm-software-management/rpm/issues/566
-- Reformat a text intended to be used used in a package description, removing
-- rpm macro generation artefacts.
-- – remove leading and ending empty lines
-- – trim intermediary empty lines to a single line
-- – fold on spaces
-- Should really be a %%{wordwrap:…} verb
local function wordwrap(text)
  text = rpm.expand(text .. "\n")
  text = string.gsub(text, "\t",              "  ")
  text = string.gsub(text, "\r",              "\n")
  text = string.gsub(text, " +\n",            "\n")
  text = string.gsub(text, "\n+\n",           "\n\n")
  text = string.gsub(text, "^\n",             "")
  text = string.gsub(text, "\n( *)[-*—][  ]+", "\n%1– ")
  output = ""
  for line in string.gmatch(text, "[^\n]*\n") do
    local pos = 0
    local advance = ""
    for word in string.gmatch(line, "%s*[^%s]*\n?") do
      local wl, bad = utf8.len(word)
      if not wl then
        print("%{warn:Invalid UTF-8 sequence detected in:}" ..
              "%{warn:" .. word .. "}" ..
              "%{warn:It may produce unexpected results.}")
        wl = bad
      end
      if (pos == 0) then
        advance, n = string.gsub(word, "^(%s*– ).*", "%1")
        if (n == 0) then
          advance = string.gsub(word, "^(%s*).*", "%1")
        end
        advance = string.gsub(advance, "– ", "  ")
        pos = pos + wl
      elseif  (pos + wl  < 81) or
             ((pos + wl == 81) and string.match(word, "\n$")) then
        pos = pos + wl
      else
        word = advance .. string.gsub(word, "^%s*", "")
        output = output .. "\n"
        pos = utf8.len(word)
      end
      output = output .. word
      if pos > 80 then
        pos = 0
        if not string.match(word, "\n$") then
          output = output .. "\n"
        end
      end
    end
  end
  output = string.gsub(output, "\n*$", "\n")
  return output
end

-- A helper to close AppStream XML runs
local function closetag(oldtag, newtag)
  if (oldtag == nil) then
    return ""
  else
    local output = "]]></" .. oldtag .. ">"
    if (oldtag == "li") and (newtag ~= oldtag) then
      output = output .. "</ul>"
    end
    return output
  end
end

-- A helper to open AppStream XML runs
local function opentag(oldtag, newtag)
  if (newtag == nil) then
    return ""
  else
    local output = "<" .. newtag .. "><![CDATA["
    if (newtag == "li") and (newtag ~= oldtag) then
      output = "<ul>" .. output
    end
    return output
  end
end

-- A helper to switch AppStream XML runs
local function switchtag(oldtag, newtag)
  return closetag(oldtag, newtag) .. opentag(oldtag, newtag)
end

-- Reformat some text into something that can be included in an AppStream
-- XML description
local function txt2xml(text)
  local        text = wordwrap(text)
  local      output = ""
  local     oldtag  = nil
  local oldadvance  = nil
  local      newtag = nil
  text = string.gsub(text, "^\n*", "")
  text = string.gsub(text, "\n*$", "\n")
  for line in string.gmatch(text, "[^\n]*\n") do
    local change = true
    local advance, n = string.gsub(line, "^(%s*– ).*", "%1")
    if (n == 1) then
      newtag = "li"
    else
      advance = string.gsub(line, "^(%s*).*", "%1")
      if (line == "\n") then
        newtag = nil
      elseif (advance ~= oldadvance) then
        newtag = "p"
      else
        change = false
      end
    end
    local result = ""
    if change then
      result     = string.gsub(line, "^" .. advance, switchtag(oldtag,newtag))
      oldtag     = newtag
      oldadvance = string.gsub(advance, "– ", "  ")
    else
      result = string.gsub(line, "^" .. advance, " ")
    end
    result = string.gsub(result, "\n$", "")
    output = output .. result
  end
  output = output .. closetag(oldtag, nil)
  return output
end

local function genmetainfo(table)
    local xmlfontname = '$(cmd=$(for f in %{buildroot}' .. table.filename .. '; do fc-scan "$f" -f "echo \\\\\"    <font>%{fullname[0]}</font>\\\\\";"; done); if test x"$cmd" != x; then echo "echo \\\\\"  <provides>\\\\\"; $cmd echo \\\\\"  </provides>\\\\\""|sh; fi|grep -v "font></font")'
    local xmlfontlang = '$(cmd=$(for f in %{buildroot}' .. table.filename .. '; do fc-scan "$f" -f "%{[]lang{echo \\\\\"    <lang>%{lang}</lang>\\\\\";}}"; done); if test x"$cmd" != x; then echo "echo \\\\\"  <languages>\\\\\"; ($cmd)|sort -u; echo \\\\\"  </languages>\\\\\""|sh; fi)'
    local xml = [[
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
<!-- $PDX-License-Identifier: MIT -->\
<component type=\"font\">\
  <id>]] .. rpm.expand("%{fontorg}.") .. table.pkgname .. [[</id>\
  <metadata_license>MIT</metadata_license>\
  <project_license>]] .. rpm.expand("%{license}") .. [[</project_license>\
  <name>Noto ]] .. table.family .. [[</name>\
  <summary><![CDATA[Noto ]] .. table.summary .. [[\]\]></summary>\
  <description>\
]] .. txt2xml(table.description) .. "\\\n" .. [[
  </description>\
  <updatecontact>]] .. rpm.expand("%{fontcontact}") .. [[</updatecontact>\
  <url type=\"homepage\">]] .. rpm.expand("%{url}") .. [[</url>\
  <releases>\
    <release version=\"]] .. rpm.expand("%{version}") .. [[\" date=\"$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)\"/>\
  </releases>]] .. "\\\n" .. xmlfontname .. "\\\n" .. xmlfontlang .. "\\\n" .. [[
</component>\]]
    _metainfobuild = (_metainfobuild ~= '' and _metainfobuild .. "\n" or '') .. "cat<<_EOL_>" .. table.metainfo .. "\\\n" .. xml .. "\n_EOL_\\\nif ! grep provides " .. table.metainfo .. " > /dev/null 2>&1; then echo \"" .. table.pkgname .. ": No family names provided\"; exit 1; fi\\"
end

local function has_value(table, value)
    for _,v in ipairs(table) do
        if v == value then
            return true
        end
    end
    return false
end

local function gentestyaml()
    local fcorth = { "aa","ab","af","ak","am","an","ar","as","ast","av","ay","az_az","az_ir","ba","be","ber_dz","ber_ma","bg","bh","bho","bi","bin","bm","bn","bo","br","brx","bs","bua","byn","ca","ce","ch","chm","chr","co","crh","cs","csb","cu","cv","cy","da","de","doi","dv","dz","ee","el","en","eo","es","et","eu","fa","fat","ff","fi","fil","fj","fo","fr","fur","fy","ga","gd","gez","gl","gn","gu","gv","ha","haw","he","hi","hne","ho","hr","hsb","ht","hu","hy","hz","ia","id","ie","ig","ii","ik","io","is","it","iu","ja","jv","ka","kaa","kab","ki","kj","kk","kl","km","kn","ko","kok","kr","ks","ku_am","ku_iq","ku_ir","ku_tr","kum","kv","kw","kwm","ky","la","lah","lb","lez","lg","li","ln","lo","lt","lv","mai","mg","mh","mi","mk","ml","mn_cn","mn_mn","mni","mo","mr","ms","mt","my","na","nb","nds","ne","ng","nl","nn","no","nqo","nr","nso","nv","ny","oc","om","or","os","ota","pa","pa_pk","pap_an","pap_aw","pes","pl","prs","ps_af","ps_pk","pt","qu","quz","rm","rn","ro","ru","rw","sa","sah","sat","sc","sco","sd","se","sel","sg","sh","shs","si","sid","sk","sl","sm","sma","smj","smn","sms","sn","so","sq","sr","ss","st","su","sv","sw","syr","szl","ta","te","tg","th","ti_er","ti_et","tig","tk","tl","tn","to","tr","ts","tt","tw","ty","tyv","ug","uk","und_zmth","und_zsye","ur","uz","ve","vi","vo","vot","wa","wal","wen","wo","xh","yap","yi","yo","za","zh_cn","zh_hk","zh_mo","zh_sg","zh_tw","zu" }
    local yaml = [[
- hosts: localhost
  tags:
    - classic
  roles:
    - role: custom-test-fonts
      required_packages:
]]
    local langs = {}
    local hash = {}
    local files = {}
    local exfiles = {}
    for i = 1, #subpackages do
	if subpackages[i]["lang"] ~= nil then
            for _,v in ipairs(subpackages[i].lang) do
--                local f = has_value(fcorth, v)
                local f = true
                local fname = string.gsub(subpackages[i].filename, "(.*/)(.*)", "%2")
                if f and (not hash[v]) then
                    langs[#langs+1] = v
                    hash[v] = true
                    files[v] = {}
		    exfiles[v] = {}
                elseif (not f) then
                    io.stderr:write("WARNING: " .. fname .. ": " .. v .. " isn't supported in fontconfig\n")
                end
                if files[v] ~= nil then
		    if subpackages[i]["excludeci"] ~= nil then
		        exfiles[v][#exfiles[v]+1] = fname
		    else
                        files[v][#files[v]+1] = fname
                    end
                end
            end
        end
	yaml = yaml .. "        - " .. subpackages[i].pkgname .. "\n"
    end
    yaml = yaml .. "      coverage:\n"
    for i = 1, #langs do
        local f = has_value(fcorth, langs[i])
        if f then
            yaml = yaml .. "        " .. langs[i] .. [[:
          path_prefix:
            - /usr/share/fonts/google-noto-vf
            - /usr/share/fonts/google-noto
          include:]] .. "\n"
            for j = 1, #files[langs[i]] do
                yaml = yaml .. "            - " .. files[langs[i]][j] .. "\n"
            end
            if next(exfiles[langs[i]]) ~= nil then
	        yaml = yaml .. [[
          exclude:]] .. "\n"
		for j = 1, #exfiles[langs[i]] do
		    yaml = yaml .. "            - " .. exfiles[langs[i]][j] .. "\n"
		end
	    end
        end
    end
    yaml = yaml .. "      families:\n"
    for i = 1, #subpackages do
	if subpackages[i].lang then
            for _,v in ipairs(subpackages[i].lang) do
		yaml = yaml .. "        - lang: " .. v .. "\n" .. [[
          package: ]] .. subpackages[i].pkgname .. "\n" .. [[
          alias: ]] .. subpackages[i].alias .. "\n" .. [[
          family: Noto ]] .. subpackages[i].family .. "\n"
            end
        end
    end
    io.stderr:write("Generating tests.yml...")
    local f = io.open("tests/tests.yml", "w")
    if f then
        f:write(yaml)
	f:close()
	io.stderr:write("Done!")
    else
        io.stderr:write("Unable to open tests.yml")
    end
end

local function notopkg(table)
    local _pname = string.lower(table.family):gsub(' ', '-')
    local pname = _pname .. (table.variable and '-vf' or '')
    local pkgname = rpm.expand('%{_fontname}-') .. pname .. '-fonts'
    local prio = tostring((table.priority and table.priority or (table.variable and rpm.expand('%{hprio}') or rpm.expand('%{mprio}'))))
    local fcconf = prio .. '-' .. rpm.expand('%{fontconf}') .. '-' .. pname .. '.conf'
    local fontdir = rpm.expand('%{_fontbasedir}') .. '/google-noto' .. (table.variable and '-vf/' or '/')
    local fontname = 'Noto' .. (table.fontname and table.fontname or string.gsub(table.family, ' ', '')) .. (table.variable and '-*VF*.*tf' or '-[^VF]*.*tf')
    local metaname = rpm.expand('%{fontorg}.') .. pkgname .. '.metainfo.xml'

    table.fcconf = fcconf
    table.pkgname = pkgname
    table.filename = fontdir .. fontname
    table.summary = 'Noto ' .. table.family .. (table.variable and ' variable' or '') .. ' font'
    table.description = rpm.expand('%{common_desc}') .. [[
Noto ]] .. table.family .. (table.variable and ' variable' or '') .. " font."
    table.metainfo = metaname
    _fcconflist = (_fcconflist ~= '' and _fcconflist .. ':' or '') .. fcconf
    _metafilelist = (_metafilelist ~= '' and _metafilelist .. ':' or '') .. metaname

    local obsoletes = ''

    if table.obsoletes then
        for i = 1, #table.obsoletes do
            obsoletes = obsoletes .. "Obsoletes: %{_fontname}-" .. table.obsoletes[i] .. "-fonts < %{version}-%{release}\n"
	end
    end
    print(rpm.expand([[

%package -n ]] .. table.pkgname .. "\n" .. [[
Summary:    ]] .. table.summary .. "\n" .. [[
Requires:   fontpackages-filesystem
Requires:   %{name}-common = %{version}-%{release}
]] .. obsoletes .. [[

%description -n ]] .. table.pkgname .. "\n" .. table.description .. "\n" .. [[

%files -n ]] .. pkgname .. "\n" .. [[
%dir ]] .. fontdir .. "\n" .. [[
%config(noreplace) %{_fontconfig_confdir}/]] .. fcconf .. "\n" .. [[
%{_fontconfig_templatedir}/]] .. fcconf .. "\n" .. [[
]] .. fontdir .. fontname .."\n" ..  [[
%{_metainfodir}/]] .. metaname .. "\n"))
end

for i = 1, #subpackages do
    notopkg(subpackages[i])
    if rpm.expand("%{cionly}") ~= 0 then
        genfcconf(subpackages[i])
	genmetainfo(subpackages[i])
    else
        _fcconfbuild = "false"
	_metainfobuild = "false"
    end
end
if rpm.expand("%{cionly}") == 1 then
    gentestyaml()
end

rpm.define("noto_fcconflist " .. _fcconflist)
rpm.define("noto_metafilelist " .. _metafilelist)
local f = io.open("debug-noto-fcconf-build.sh", "w")
if f then
    f:write(_fcconfbuild)
    f:close()
end
local f = io.open("debug-noto-metainfo-build.sh", "w")
if f then
    f:write(_metainfobuild)
    f:close()
end
rpm.define("notobuild_fcconf " .. _fcconfbuild .. "\n")
rpm.define("notobuild_metainfo " .. _metainfobuild .. "\n")
} ## end of lua

%prep
%setup -q -n noto-fonts-%{srcver}


%build
%if %{cionly}
exit 1
%endif
%{notobuild_fcconf}

%install
install -m 0755 -d %{buildroot}%{_fontbasedir}/google-noto
for f in unhinted/ttf/*/Noto*.ttf hinted/ttf/*/Noto*.ttf; do
  install -m 0644 -p $f %{buildroot}%{_fontbasedir}/google-noto/
done
install -m 0755 -d %{buildroot}%{_fontbasedir}/google-noto-vf
install -m 0644 -p unhinted/slim-variable-ttf/Noto*.ttf %{buildroot}%{_fontbasedir}/google-noto-vf/

# fc-scan in script expects fonts are already installed
%{notobuild_metainfo}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir} \
                   %{buildroot}%{_metainfodir}

IFS=":"
for f in $(echo %{noto_fcconflist}); do
    install -m 0644 -p $f %{buildroot}%{_fontconfig_templatedir}/$f
    ln -s $(realpath --relative-to=%{_fontconfig_confdir}/ %{_fontconfig_templatedir}/$f) \
	  %{buildroot}%{_fontconfig_confdir}/$f
done
for f in $(echo %{noto_metafilelist}); do
    install -m 0644 -p $f %{buildroot}%{_metainfodir}/$f
done


%check
IFS=":"
for f in $(echo %{noto_fcconflist}); do
    xmllint --loaddtd --valid --nonet %{buildroot}%{_fontconfig_templatedir}/$f
done
for f in $(echo %{noto_metafilelist}); do
    appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/$f
done

%files common
%license LICENSE
%doc README.md FAQ.md


%changelog
* Wed May 18 2022 Akira TAGOH <tagoh@redhat.com> - 20201206-4
- Rebuilt to ship google-noto-sans-symbols2-fonts in CRB.
  Resolves: rhbz#2082681

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 20201206-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed May 12 2021 Akira TAGOH <tagoh@redhat.com> - 20201206-2
- Add some Obsoletes lines for dropped sub packages.

* Fri May 12 2021 Akira TAGOH <tagoh@redhat.com> - 20201206-1
- Updates to 20201206.
  Resolves: rhbz#1899847
- Refactoring spec file.
- Fix invalid metainfo files.
  Resolves: rhbz#1830709

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 20181223-10
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20181223-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20181223-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20181223-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Akira TAGOH <tagoh@redhat.com> - 20181223-6
- Make variable fonts priority more than non variable fonts. (#1739976)

* Fri Jul 26 2019 Parag Nemade <pnemade AT redhat DOT com> - 20181223-5
- Resolves:rh#1554988 - google-noto-sans-gurmkukhi-fonts default for pa_IN locale

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181223-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun  4 2019 Akira TAGOH <tagoh@redhat.com> - 20181223-3
- Install metainfo files under %%{_metainfodir}.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181223-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Akira TAGOH <tagoh@redhat.com> - 20181223-1
- Updates to 20181223.
- Add new sub-packages for variable fonts.

* Mon Dec 17 2018 Akira TAGOH <tagoh@redhat.com> - 20181130-2
- Make Display and UI fonts lower priority.
- Add more languages to google-noto-*-devanagari.conf, google-noto-sans-ethiopic.conf,
  and google-noto-sans-hebrew.conf

* Fri Dec  7 2018 Akira TAGOH <tagoh@redhat.com> - 20181130-1
- Updates to 20181130.
- Noto Sans Balinese is now Noto Serif Balinese.
- Add new sub-packages: google-noto-music-fonts,
  google-noto-sans-bassa-vah-fonts, google-noto-sans-bhaiksuki-fonts,
  google-noto-sans-caucasian-albanian-fonts, google-noto-sans-duployan-fonts,
  google-noto-sans-elbasan-fonts, google-noto-sans-grantha-fonts,
  google-noto-sans-hatran-fonts, google-noto-sans-khojki-fonts,
  google-noto-sans-khudawadi-fonts, google-noto-sans-linear-a-fonts,
  google-noto-sans-mahajani-fonts, google-noto-sans-manichaean-fonts,
  google-noto-sans-marchen-fonts, google-noto-sans-mende-kikakui-fonts,
  google-noto-sans-meroitic-fonts, google-noto-sans-miao-fonts,
  google-noto-sans-modi-fonts, google-noto-sans-mro-fonts,
  google-noto-sans-multani-fonts, google-noto-sans-nabataean-fonts,
  google-noto-sans-newa-fonts, google-noto-sans-old-hungarian-fonts,
  google-noto-sans-old-north-arabian-fonts, google-noto-sans-old-permic-fonts,
  google-noto-sans-pahawh-hmong-fonts, google-noto-sans-palmyrene-fonts,
  google-noto-sans-pau-cin-hau-fonts, google-noto-sans-psalter-pahlavi-fonts,
  google-noto-sans-sharada-fonts, google-noto-sans-sora-sompeng-fonts,
  google-noto-sans-syriac-fonts, google-noto-sans-takri-fonts,
  google-noto-sans-tirhuta-fonts, google-noto-sans-warang-citi-fonts,
  google-noto-serif-ahom-fonts, google-noto-serif-gurmukhi-fonts,
  google-noto-serif-tamil-slanted-fonts, google-noto-serif-tibetan-fonts

* Fri Sep 21 2018 Akira TAGOH <tagoh@redhat.com> - 20180905-1
- Updates to 20180905.
- Remove Group tag.
- Don't call fc-cache in scriptlets. this isn't needed anymore.
- Drop BR: fontforge.
- Generate fontconfig config files in macro for simple one.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20161022-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
