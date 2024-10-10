"""
python-dcl is a Python library for working with diacritics in multilingual Latin-based text. 
It provides functionality for adding, removing, modifying and processing diacritic marks, 
supporting functions for orthographic and linguistic analysis.
"""

from __future__ import annotations
from enum import Flag, auto, global_enum
from typing import overload

__version__ = "2.0.0"

@global_enum
class Diacritic(Flag):
    ACUTE = auto()
    BAR = auto()
    BELT = auto()
    BREVE = auto()
    BREVEBELOW = auto()
    CARON = auto()
    CEDILLA = auto()
    CIRCUMFLEX = auto()
    CIRCUMFLEXBELOW = auto()
    COMMABELOW = auto()
    CROSSEDTAIL = auto()
    DESCENDER = auto()
    DIAERESIS = auto()
    DIAERESISBELOW = auto()
    DIAGONALSTROKE = auto()
    DOT = auto()
    DOTABOVE = auto()
    DOTBELOW = auto()
    DOUBLEACUTE = auto()
    DOUBLEBAR = auto()
    DOUBLEGRAVE = auto()
    FLOURISH = auto()
    GRAVE = auto()
    HIGHSTROKE = auto()
    HOOK = auto()
    HOOKABOVE = auto()
    HOOKTAIL = auto()
    HORN = auto()
    INVERTEDBREVE = auto()
    LEFTHOOK = auto()
    LINEBELOW = auto()
    LONGRIGHTLEG = auto()
    LONGSTROKEOVERLAY = auto()
    LOOP = auto()
    MACRON = auto()
    MIDDLEDOT = auto()
    MIDDLETILDE = auto()
    OBLIQUESTROKE = auto()
    OGONEK = auto()
    PALATALHOOK = auto()
    RETROFLEXHOOK = auto()
    RINGABOVE = auto()
    RINGBELOW = auto()
    SHORTSTROKEOVERLAY = auto()
    SQUIRRELTAIL = auto()
    STROKE = auto()
    STROKETHROUGHDESCENDER = auto()
    SWASHTAIL = auto()
    TAIL = auto()
    TILDE = auto()
    TILDEBELOW = auto()
    TOPBAR = auto()

    # Aliases
    OVERDOT = DOTABOVE
    UNDERDOT = DOTBELOW
    UMLAUT = DIAERESIS


_diacritic_map = {
    Diacritic.ACUTE: {
        "\u0041": "\u00c1",
        "\u0043": "\u0106",
        "\u0045": "\u00c9",
        "\u0047": "\u01f4",
        "\u0049": "\u00cd",
        "\u004b": "\u1e30",
        "\u004c": "\u0139",
        "\u004d": "\u1e3e",
        "\u004e": "\u0143",
        "\u004f": "\u00d3",
        "\u0050": "\u1e54",
        "\u0052": "\u0154",
        "\u0053": "\u015a",
        "\u0055": "\u00da",
        "\u0057": "\u1e82",
        "\u0059": "\u00dd",
        "\u005a": "\u0179",
    },
    Diacritic.ACUTE | Diacritic.DOTABOVE: {"\u0053": "\u1e64"},
    Diacritic.BAR: {"\u0043": "\ua792", "\u004c": "\u023d"},
    Diacritic.BELT: {"\u004c": "\ua7ad"},
    Diacritic.BREVE: {
        "\u0041": "\u0102",
        "\u0045": "\u0114",
        "\u0047": "\u011e",
        "\u0049": "\u012c",
        "\u004f": "\u014e",
        "\u0055": "\u016c",
    },
    Diacritic.ACUTE | Diacritic.BREVE: {"\u0041": "\u1eae"},
    Diacritic.BREVE | Diacritic.DOTBELOW: {"\u0041": "\u1eb6"},
    Diacritic.BREVE | Diacritic.GRAVE: {"\u0041": "\u1eb0"},
    Diacritic.BREVE | Diacritic.HOOKABOVE: {"\u0041": "\u1eb2"},
    Diacritic.BREVE | Diacritic.TILDE: {"\u0041": "\u1eb4"},
    Diacritic.BREVEBELOW: {"\u0048": "\u1e2a"},
    Diacritic.CARON: {
        "\u0041": "\u01cd",
        "\u0043": "\u010c",
        "\u0044": "\u01c5",
        "\u0045": "\u011a",
        "\u0047": "\u01e6",
        "\u0048": "\u021e",
        "\u0049": "\u01cf",
        "\u004b": "\u01e8",
        "\u004c": "\u013d",
        "\u004e": "\u0147",
        "\u004f": "\u01d1",
        "\u0052": "\u0158",
        "\u0053": "\u0160",
        "\u0054": "\u0164",
        "\u0055": "\u01d3",
        "\u005a": "\u017d",
    },
    Diacritic.CARON | Diacritic.DOTABOVE: {"\u0053": "\u1e66"},
    Diacritic.CEDILLA: {
        "\u0043": "\u00c7",
        "\u0044": "\u1e10",
        "\u0045": "\u0228",
        "\u0047": "\u0122",
        "\u0048": "\u1e28",
        "\u004b": "\u0136",
        "\u004c": "\u013b",
        "\u004e": "\u0145",
        "\u0052": "\u0156",
        "\u0053": "\u015e",
        "\u0054": "\u0162",
    },
    Diacritic.ACUTE | Diacritic.CEDILLA: {"\u0043": "\u1e08"},
    Diacritic.BREVE | Diacritic.CEDILLA: {"\u0045": "\u1e1c"},
    Diacritic.CIRCUMFLEX: {
        "\u0041": "\u00c2",
        "\u0043": "\u0108",
        "\u0045": "\u00ca",
        "\u0047": "\u011c",
        "\u0048": "\u0124",
        "\u0049": "\u00ce",
        "\u004a": "\u0134",
        "\u004f": "\u00d4",
        "\u0053": "\u015c",
        "\u0055": "\u00db",
        "\u0057": "\u0174",
        "\u0059": "\u0176",
        "\u005a": "\u1e90",
    },
    Diacritic.ACUTE
    | Diacritic.CIRCUMFLEX: {
        "\u0041": "\u1ea4",
        "\u0045": "\u1ebe",
        "\u004f": "\u1ed0",
    },
    Diacritic.CIRCUMFLEX
    | Diacritic.DOTBELOW: {"\u0041": "\u1eac", "\u0045": "\u1ec6", "\u004f": "\u1ed8"},
    Diacritic.CIRCUMFLEX
    | Diacritic.GRAVE: {"\u0041": "\u1ea6", "\u0045": "\u1ec0", "\u004f": "\u1ed2"},
    Diacritic.CIRCUMFLEX
    | Diacritic.HOOKABOVE: {"\u0041": "\u1ea8", "\u0045": "\u1ec2", "\u004f": "\u1ed4"},
    Diacritic.CIRCUMFLEX
    | Diacritic.TILDE: {"\u0041": "\u1eaa", "\u0045": "\u1ec4", "\u004f": "\u1ed6"},
    Diacritic.CIRCUMFLEXBELOW: {
        "\u0044": "\u1e12",
        "\u0045": "\u1e18",
        "\u004c": "\u1e3c",
        "\u004e": "\u1e4a",
        "\u0054": "\u1e70",
        "\u0055": "\u1e76",
    },
    Diacritic.COMMABELOW: {"\u0053": "\u0218", "\u0054": "\u021a"},
    Diacritic.CROSSEDTAIL: {"\u004a": "\ua7b2"},
    Diacritic.DESCENDER: {
        "\u0048": "\u2c67",
        "\u004b": "\u2c69",
        "\u004e": "\ua790",
        "\u005a": "\u2c6b",
    },
    Diacritic.DIAERESIS: {
        "\u0041": "\u00c4",
        "\u0045": "\u00cb",
        "\u0048": "\u1e26",
        "\u0049": "\u00cf",
        "\u004f": "\u00d6",
        "\u0055": "\u00dc",
        "\u0057": "\u1e84",
        "\u0058": "\u1e8c",
        "\u0059": "\u0178",
    },
    Diacritic.ACUTE | Diacritic.DIAERESIS: {"\u0049": "\u1e2e", "\u0055": "\u01d7"},
    Diacritic.CARON | Diacritic.DIAERESIS: {"\u0055": "\u01d9"},
    Diacritic.DIAERESIS | Diacritic.GRAVE: {"\u0055": "\u01db"},
    Diacritic.DIAERESIS | Diacritic.MACRON: {"\u0055": "\u1e7a"},
    Diacritic.DIAERESISBELOW: {"\u0055": "\u1e72"},
    Diacritic.DIAGONALSTROKE: {
        "\u004b": "\ua742",
        "\u0051": "\ua758",
        "\u0054": "\u023e",
        "\u0056": "\ua75e",
    },
    Diacritic.DOT: {"\u0043": "\ua73e"},
    Diacritic.DOTABOVE: {
        "\u0041": "\u0226",
        "\u0042": "\u1e02",
        "\u0043": "\u010a",
        "\u0044": "\u1e0a",
        "\u0045": "\u0116",
        "\u0046": "\u1e1e",
        "\u0047": "\u0120",
        "\u0048": "\u1e22",
        "\u0049": "\u0130",
        "\u004d": "\u1e40",
        "\u004e": "\u1e44",
        "\u004f": "\u022e",
        "\u0050": "\u1e56",
        "\u0052": "\u1e58",
        "\u0053": "\u1e60",
        "\u0054": "\u1e6a",
        "\u0057": "\u1e86",
        "\u0058": "\u1e8a",
        "\u0059": "\u1e8e",
        "\u005a": "\u017b",
    },
    Diacritic.DOTABOVE | Diacritic.MACRON: {"\u0041": "\u01e0", "\u004f": "\u0230"},
    Diacritic.DOTBELOW: {
        "\u0041": "\u1ea0",
        "\u0042": "\u1e04",
        "\u0044": "\u1e0c",
        "\u0045": "\u1eb8",
        "\u0048": "\u1e24",
        "\u0049": "\u1eca",
        "\u004b": "\u1e32",
        "\u004c": "\u1e36",
        "\u004d": "\u1e42",
        "\u004e": "\u1e46",
        "\u004f": "\u1ecc",
        "\u0052": "\u1e5a",
        "\u0053": "\u1e62",
        "\u0054": "\u1e6c",
        "\u0055": "\u1ee4",
        "\u0056": "\u1e7e",
        "\u0057": "\u1e88",
        "\u0059": "\u1ef4",
        "\u005a": "\u1e92",
    },
    Diacritic.DOTABOVE | Diacritic.DOTBELOW: {"\u0053": "\u1e68"},
    Diacritic.DOTBELOW | Diacritic.MACRON: {"\u004c": "\u1e38", "\u0052": "\u1e5c"},
    Diacritic.DOUBLEACUTE: {"\u004f": "\u0150", "\u0055": "\u0170"},
    Diacritic.DOUBLEBAR: {"\u004c": "\u2c60"},
    Diacritic.DOUBLEGRAVE: {
        "\u0041": "\u0200",
        "\u0045": "\u0204",
        "\u0049": "\u0208",
        "\u004f": "\u020c",
        "\u0052": "\u0210",
        "\u0055": "\u0214",
    },
    Diacritic.FLOURISH: {"\u0042": "\ua796", "\u0050": "\ua752"},
    Diacritic.GRAVE: {
        "\u0041": "\u00c0",
        "\u0045": "\u00c8",
        "\u0049": "\u00cc",
        "\u004e": "\u01f8",
        "\u004f": "\u00d2",
        "\u0055": "\u00d9",
        "\u0057": "\u1e80",
        "\u0059": "\u1ef2",
    },
    Diacritic.HIGHSTROKE: {"\u004c": "\ua748"},
    Diacritic.HOOK: {
        "\u0042": "\u0181",
        "\u0043": "\u0187",
        "\u0044": "\u018a",
        "\u0046": "\u0191",
        "\u0047": "\u0193",
        "\u0048": "\ua7aa",
        "\u004b": "\u0198",
        "\u004d": "\u2c6e",
        "\u0050": "\u01a4",
        "\u0053": "\ua7c5",
        "\u0054": "\u01ac",
        "\u0056": "\u01b2",
        "\u0057": "\u2c72",
        "\u0059": "\u01b3",
        "\u005a": "\u0224",
    },
    Diacritic.HOOKABOVE: {
        "\u0041": "\u1ea2",
        "\u0045": "\u1eba",
        "\u0049": "\u1ec8",
        "\u004f": "\u1ece",
        "\u0055": "\u1ee6",
        "\u0059": "\u1ef6",
    },
    Diacritic.HOOKTAIL: {"\u0051": "\u024a"},
    Diacritic.HORN: {"\u004f": "\u01a0", "\u0055": "\u01af"},
    Diacritic.ACUTE | Diacritic.HORN: {"\u004f": "\u1eda", "\u0055": "\u1ee8"},
    Diacritic.DOTBELOW | Diacritic.HORN: {"\u004f": "\u1ee2", "\u0055": "\u1ef0"},
    Diacritic.GRAVE | Diacritic.HORN: {"\u004f": "\u1edc", "\u0055": "\u1eea"},
    Diacritic.HOOKABOVE | Diacritic.HORN: {"\u004f": "\u1ede", "\u0055": "\u1eec"},
    Diacritic.HORN | Diacritic.TILDE: {"\u004f": "\u1ee0", "\u0055": "\u1eee"},
    Diacritic.INVERTEDBREVE: {
        "\u0041": "\u0202",
        "\u0045": "\u0206",
        "\u0049": "\u020a",
        "\u004f": "\u020e",
        "\u0052": "\u0212",
        "\u0055": "\u0216",
    },
    Diacritic.LEFTHOOK: {"\u004e": "\u019d"},
    Diacritic.LINEBELOW: {
        "\u0042": "\u1e06",
        "\u0044": "\u1e0e",
        "\u004b": "\u1e34",
        "\u004c": "\u1e3a",
        "\u004e": "\u1e48",
        "\u0052": "\u1e5e",
        "\u0054": "\u1e6e",
        "\u005a": "\u1e94",
    },
    Diacritic.LONGRIGHTLEG: {"\u004e": "\u0220"},
    Diacritic.LONGSTROKEOVERLAY: {"\u004f": "\ua74a"},
    Diacritic.LOOP: {"\u004f": "\ua74c", "\u0059": "\u1efe"},
    Diacritic.MACRON: {
        "\u0041": "\u0100",
        "\u0045": "\u0112",
        "\u0047": "\u1e20",
        "\u0049": "\u012a",
        "\u004f": "\u014c",
        "\u0055": "\u016a",
        "\u0059": "\u0232",
    },
    Diacritic.ACUTE | Diacritic.MACRON: {"\u0045": "\u1e16", "\u004f": "\u1e52"},
    Diacritic.GRAVE | Diacritic.MACRON: {"\u0045": "\u1e14", "\u004f": "\u1e50"},
    Diacritic.MIDDLEDOT: {"\u004c": "\u013f"},
    Diacritic.MIDDLETILDE: {"\u004c": "\u2c62", "\u004f": "\u019f"},
    Diacritic.OBLIQUESTROKE: {
        "\u0047": "\ua7a0",
        "\u004b": "\ua7a2",
        "\u004e": "\ua7a4",
        "\u0052": "\ua7a6",
        "\u0053": "\ua7a8",
    },
    Diacritic.OGONEK: {
        "\u0041": "\u0104",
        "\u0045": "\u0118",
        "\u0049": "\u012e",
        "\u004f": "\u01ea",
        "\u0055": "\u0172",
    },
    Diacritic.MACRON | Diacritic.OGONEK: {"\u004f": "\u01ec"},
    Diacritic.PALATALHOOK: {"\u0043": "\ua7c4", "\u005a": "\ua7c6"},
    Diacritic.RETROFLEXHOOK: {"\u0054": "\u01ae"},
    Diacritic.RINGABOVE: {"\u0041": "\u00c5", "\u0055": "\u016e"},
    Diacritic.ACUTE | Diacritic.RINGABOVE: {"\u0041": "\u01fa"},
    Diacritic.RINGBELOW: {"\u0041": "\u1e00"},
    Diacritic.SHORTSTROKEOVERLAY: {"\u0044": "\ua7c7", "\u0053": "\ua7c9"},
    Diacritic.SQUIRRELTAIL: {"\u0050": "\ua754"},
    Diacritic.STROKE: {
        "\u0041": "\u023a",
        "\u0042": "\u0243",
        "\u0043": "\u023b",
        "\u0044": "\u0110",
        "\u0045": "\u0246",
        "\u0046": "\ua798",
        "\u0047": "\u01e4",
        "\u0048": "\u0126",
        "\u0049": "\u0197",
        "\u004a": "\u0248",
        "\u004b": "\ua740",
        "\u004c": "\u0141",
        "\u004f": "\u00d8",
        "\u0050": "\u2c63",
        "\u0052": "\u024c",
        "\u0054": "\u0166",
        "\u0055": "\ua7b8",
        "\u0059": "\u024e",
        "\u005a": "\u01b5",
    },
    Diacritic.ACUTE | Diacritic.STROKE: {"\u004f": "\u01fe"},
    Diacritic.DIAGONALSTROKE | Diacritic.STROKE: {"\u004b": "\ua744"},
    Diacritic.STROKETHROUGHDESCENDER: {"\u0050": "\ua750", "\u0051": "\ua756"},
    Diacritic.SWASHTAIL: {"\u0053": "\u2c7e", "\u005a": "\u2c7f"},
    Diacritic.TAIL: {"\u0052": "\u2c64"},
    Diacritic.TILDE: {
        "\u0041": "\u00c3",
        "\u0045": "\u1ebc",
        "\u0049": "\u0128",
        "\u004e": "\u00d1",
        "\u004f": "\u00d5",
        "\u0055": "\u0168",
        "\u0056": "\u1e7c",
        "\u0059": "\u1ef8",
    },
    Diacritic.ACUTE | Diacritic.TILDE: {"\u004f": "\u1e4c", "\u0055": "\u1e78"},
    Diacritic.DIAERESIS | Diacritic.TILDE: {"\u004f": "\u1e4e"},
    Diacritic.MACRON | Diacritic.TILDE: {"\u004f": "\u022c"},
    Diacritic.TILDEBELOW: {"\u0045": "\u1e1a", "\u0049": "\u1e2c", "\u0055": "\u1e74"},
    Diacritic.TOPBAR: {"\u0042": "\u0182", "\u0044": "\u018b"},
}

_diacritic_cleaner_map = {}
for val in _diacritic_map.values():
    _diacritic_cleaner_map.update({v: k for k, v in val.items()})
    _diacritic_cleaner_map.update({v.lower(): k.lower() for k, v in val.items()})


def apply(character: str, /, diacritic: Diacritic) -> str:
    """Apply a given diacritic to a character."""
    if len(character) != 1:
        raise ValueError("Can only apply a diacritic for one-length strings.")
    if diacritic not in _diacritic_map:
        raise ValueError("Invalid diacritic or combination of diacritics")
    index = _diacritic_map[diacritic]
    if character.upper() not in index:
        raise ValueError(
            f"Character {character!r} is not applicable for the {diacritic.name} diacritic"
        )
    func = str.lower if character.islower() else str.upper
    return func(index[character.upper()])


def identify(string: str, /) -> Diacritic | None:
    """Identify the diacritic applied to the given character."""
    for diacritic, characters in _diacritic_map.items():
        for accented in characters.values():
            if string.upper() in accented:
                return diacritic


def identifyall(string: str, /) -> dict[int, Diacritic | None]:
    """Identify the diacritics applied to the given string."""
    return {idx: identify(char) for idx, char in enumerate(string)}


def contains(string: str, /, diacritic: Diacritic | None = None) -> bool:
    """Check if a string contains particular, or any diacritics."""
    values = identify(string).values()
    if diacritic is None:
        return any(values)
    return diacritic in values


def find(string: str, /, diacritic: Diacritic) -> list[int]:
    """Find where a string has a certain diacritic."""
    return [idx for idx, dia in identifyall(string).items() if diacritic is dia]


def remove(string: str, /, diacritic: Diacritic) -> str:
    """Remove a given diacritic from a string."""
    return "".join(
        _diacritic_cleaner_map.get(char, char) if identify(char) is diacritic else char
        for char in string
    )


def normalize(string: str, /) -> str:
    """Remove all diacritics from a string."""
    return "".join(_diacritic_cleaner_map.get(char, char) for char in string)


normalise = normalize


@overload
def applicable(character: str, /) -> list[Diacritic]:
    ...


@overload
def applicable(diacritic: Diacritic, /) -> list[str]:
    ...


def applicable(diacritic_or_character: str, /) -> list[Diacritic]:
    """Get diacritics for character or character for diacritics."""
    if isinstance(diacritic_or_character, str):
        return [
            k
            for k in _diacritic_map
            if diacritic_or_character.upper() in _diacritic_map[k]
        ]
    else:
        ret = [k for k in _diacritic_map.get(diacritic_or_character, [])]
        return ret + list(map(str.lower, ret))


def substitute(string: str, /, old: Diacritic | None, new: Diacritic | None) -> str:
    """Substitute diacritics with a different diacritic."""
    ret = ""

    for char in string:
        diacritic = identify(char)
        if new is None:
            ret += normalize(char)
        else:
            ret += apply(normalize(char), d=new) if diacritic is old else char

    return ret


def replace(string: str, /, character: str, diacritic: Diacritic) -> str:
    """Replace characters with their diacritic version."""
    ret = ""

    for char in string:
        if char == character:
            func = str.lower if character.islower() else str.upper
            ret += func(apply(char, diacritic))
        else:
            ret += char

    return ret


def count(string: str, /, diacritic: Diacritic) -> int:
    """Count the occurances of a diacritic within a string."""
    return sum(1 for d in identifyall(string).values() if diacritic is d)


class DiacriticTransformer(str):
    """An object that employs all of dcl's major functions."""

    def apply_diacritic(self, diacritic: Diacritic) -> DiacriticTransformer:
        """Apply a diacritic. This will only work for one-length strings."""
        return DiacriticTransformer(apply(self, diacritic))

    def identify_diacritic(self) -> Diacritic | None:
        """Identify the diacritic. This will only work for one-length strings."""
        return identify(self)

    def identify_all_diacritics(self) -> dict[int, Diacritic | None]:
        """Identify all the diacritics applied to this string."""
        return identifyall(self)

    def contains_diacritic(self, diacritic: Diacritic | None = None) -> bool:
        """Check if the string contains particular, or any diacritic."""
        return contains(self, diacritic)

    def find_diacritic(self, diacritic: Diacritic) -> list[int]:
        """Find where the string has a certain diacritic."""
        return find(self, diacritic)

    def remove_diacritic(self, diacritic: Diacritic) -> DiacriticTransformer:
        """Remove a given diacritic from the string."""
        return DiacriticTransformer(remove(self, diacritic))

    def normalize_diacritics(self) -> DiacriticTransformer:
        """Remove all diacritics from the string."""
        return DiacriticTransformer(normalize(self))

    normalise_diacritics = normalize_diacritics

    @overload
    def applicable(self, character: str, /) -> list[Diacritic]:
        ...

    @overload
    def applicable(self, diacritic: Diacritic, /) -> list[str]:
        ...

    def applicable(self) -> list[Diacritic]:
        """Get a list of diacritics applicable. This will only work for one-length strings."""
        return applicable(self)

    def substitute_diacritics(
        self, old: Diacritic | None, new: Diacritic | None
    ) -> DiacriticTransformer:
        """Substitute diacritics with a different diacritic."""
        return DiacriticTransformer(substitute(self, old, new))

    def replace_diacritics(
        self, character: str, diacritic: Diacritic
    ) -> DiacriticTransformer:
        """Replace characters with their diacritic version."""
        return DiacriticTransformer(replace(self, character, diacritic))

    def count_diacritics(self, diacritic: Diacritic) -> int:
        """Count the occurances of a diacritic."""
        return count(self, diacritic)
