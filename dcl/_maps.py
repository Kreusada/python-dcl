_diacritic_map = {
    "grave": {
        "A": "\u00c0", 
        "E": "\u00c8", 
        "I": "\u00cc", 
        "O": "\u00d2", 
        "U": "\u00d9", 
        "W": "\u1e80", 
        "Y": "\u1ef2"
    }, 
    "acute": {
        "A": "\u00c1", 
        "C": "\u0106",
        "E": "\u00c9", 
        "G": "\u01f4", 
        "I": "\u00cd", 
        "K": "\u1e30", 
        "L": "\u0139", 
        "N": "\u0143", 
        "O": "\u00d3", 
        "R": "\u0154", 
        "S": "\u015a", 
        "U": "\u00da", 
        "W": "\u1e82", 
        "Y": "\u00dd", 
        "Z": "\u0179"
    }, 
    "double_acute": {
        "O": "\u0150", 
        "U": "\u0170"
    }, 
    "circumflex": {
        "A": "\u00c2", 
        "E": "\u00ca", 
        "G": "\u011c", 
        "H": "\u0124", 
        "I": "\u00ce", 
        "J": "\u0134", 
        "O": "\u00d4", 
        "S": "\u015c", 
        "U": "\u00db", 
        "W": "\u0174", 
        "Y": "\u0176"
    }, 
    "tilde": {
        "A": "\u00c3", 
        "I": "\u0128", 
        "N": "\u00d1", 
        "O": "\u00d5", 
        "U": "\u0168"
    }, 
    "umlaut": {
        "A": "\u00c4", 
        "E": "\u00cb", 
        "I": "\u00cf", 
        "O": "\u00d6", 
        "U": "\u00dc", 
        "W": "\u1e84", 
        "Y": "\u0178"
    }, 
    "ring": {
        "A": "\u00c5", 
        "U": "\u016e"
    }, 
    "cedilla": {
        "C": "\u00c7", 
        "D": "\u1e10", 
        "G": "\u0122", 
        "K": "\u0136", 
        "L": "\u013b", 
        "N": "\u0145", 
        "R": "\u0156", 
        "S": "\u015e", 
        "T": "\u0162"
    }, 
    "caron": {
        "C": "\u010c", 
        "D": "\u010e", 
        "E": "\u011a", 
        "G": "\u01e6", 
        "K": "\u01e8", 
        "L": "\u013d", 
        "N": "\u0147", 
        "R": "\u0158", 
        "S": "\u0160", 
        "T": "\u0164", 
        "Z": "\u017d"
    }, 
    "slash": {
        "O": "\u00d8", 
        "L": "\u0141"
    }, 
    "ogonek": {
        "A": "\u0104", 
        "E": "\u0118", 
        "I": "\u012e", 
        "U": "\u0172"
    }, 
    "macron": {
        "A": "\u0100", 
        "E": "\u0112", 
        "I": "\u012a", 
        "O": "\u014c", 
        "U": "\u016a"
    }, 
    "breve": {
        "A": "\u0102", 
        "E": "\u0114", 
        "G": "\u011e", 
        "I": "\u012c", 
        "O": "\u014e", 
        "U": "\u016c"
    }, 
    "tittle": {
        "B": "\u1e02", 
        "C": "\u010a", 
        "D": "\u1e0a", 
        "E": "\u0116", 
        "F": "\u1e1e", 
        "G": "\u0120", 
        "I": "\u0130", 
        "M": "\u1e40", 
        "P": "\u1e56", 
        "S": "\u1e60", 
        "T": "\u1e6a", 
        "Z": "\u017b"
    }, 
    "stroke": {
        "D": "\u0110", 
        "G": "\u01e4", 
        "H": "\u0126", 
        "T": "\u0166"
    }, 
    "interpunct": {
        "L": "\u013f"
    }, 
    "umlaut_and_macron": {
        "A": "\u01de"
    }, 
    "ring_and_acute": {
        "A": "\u01fa"
    }, 
    "stroke_and_acute": {
        "O": "\u01fe"
    }
}

# Supporting aliases

_update_dict = {}
for k, v in _diacritic_map.items():
    if "umlaut" in k:
        _diacritic_map[k.replace("umlaut", "diaresis")] = v
        _update_dict[k.replace("umlaut", "diaresis")] = v
_diacritic_map.update(_update_dict)

_diacritic_cleaner_map = {}
for val in _diacritic_map.values():
    _diacritic_cleaner_map.update({v: k for k, v in val.items()})
    _diacritic_cleaner_map.update({v.lower(): k.lower() for k, v in val.items()})

_diacritic_char_map = {
    "circumflex": "\u02c6", 
    "caron": "\u02c7", 
    "breve": "\u02d8", 
    "tittle": "\u02d9",
    "ring": "\u02da", 
    "ogonek": "\u02db", 
    "tilde": "\u02dc", 
    "acute": "\u00b4", 
    "cedilla": "\u00b8", 
    "macron": "\u00af", 
    "umlaut": "\u00a8", 
    "interpunct": "\u00b7", 
    "double_acute": "\u02dd",
    "grave": "`"
}