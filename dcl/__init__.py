"""DCL - An easy to use diacritic library used for diacritic and accent modification.
This library adds, removes, identifies, and modifies diacritics, with a knuckled down
easy implementation.

DCL currently supports a multitude of diacritics:

* acute
* breve
* caron
* cedilla
* grave
* interpunct
* macron
* ogonek
* ring
* ring_and_acute
* slash
* stroke
* stroke_and_acute
* tilde
* tittle
* umlaut/diaresis
* umlaut_and_macron

We can use these functions directly from the dcl object to convert a single string
into the given letter with the appropriate diacritic.
"""

from .errors import *
from .objects import *
from typing import Dict as _Dict, List as _List, Iterable as _Iterable

__version__ = "1.0.0"

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


diacritic_list = [
    "acute",
    "breve",
    "caron",
    "cedilla",
    "diaresis",
    "grave",
    "interpunct",
    "macron",
    "ogonek",
    "ring",
    "ring_and_acute",
    "slash",
    "stroke",
    "stroke_and_acute",
    "tilde",
    "tittle",
    "umlaut",
    "umlaut_and_macron",
]

isdiacritictype = frozenset(diacritic_list).__contains__

def _apply_diacritic(string, accent):
    a = DiacriticApplicant(string)
    return getattr(a, accent)


def grave(string: str):
    """Returns the given character with a grave diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the grave diacritic.

    Returns
    -------
    Character
        The string with the grave diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a grave diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "grave")


def acute(string: str):
    """Returns the given character with an acute diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the acute diacritic.

    Returns
    -------
    Character
        The string with the acute diacritic.

    Raises
    ------
    AccentError
        The given string could not be given an acute diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "acute")


def circumflex(string: str):
    """Returns the given character with a circumflex diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the circumflex diacritic.

    Returns
    -------
    Character
        The string with the circumflex diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a circumflex diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "circumflex")


def tilde(string: str):
    """Returns the given character with a tilde diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the tilde diacritic.

    Returns
    -------
    Character
        The string with the tilde diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a tilde diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "tilde")


def umlaut(string: str):
    """Returns the given character with an umlaut diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the umlaut diacritic.

    Returns
    -------
    Character
        The string with the umlaut diacritic.

    Raises
    ------
    AccentError
        The given string could not be given an umlaut diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "umlaut")


def caron(string: str):
    """Returns the given character with a caron diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the caron diacritic.

    Returns
    -------
    Character
        The string with the caron diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a caron diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "caron")


def ring(string: str):
    """Returns the given character with a ring diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the ring diacritic.

    Returns
    -------
    Character
        The string with the ring diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a ring diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "ring")


def cedilla(string: str):
    """Returns the given character with a cedilla diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the ring diacritic.

    Returns
    -------
    Character
        The string with the ring diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a ring diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "cedilla")

def slash(string: str):
    """Returns the given character with a slash diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the slash diacritic.

    Returns
    -------
    Character
        The string with the slash diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a slash diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "slash")


def ogonek(string: str):
    """Returns the given character with an ogonek diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the ogonek diacritic.

    Returns
    -------
    Character
        The string with the ogonek diacritic.

    Raises
    ------
    AccentError
        The given string could not be given an ogonek diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "ogonek")


def macron(string: str):
    """Returns the given character with a macron diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the macron diacritic.

    Returns
    -------
    Character
        The string with the macron diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a macron diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "macron")


def breve(string: str):
    """Returns the given character with a breve diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the breve diacritic.

    Returns
    -------
    Character
        The string with the breve diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a breve diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "breve")


def tittle(string: str):
    """Returns the given character with a tittle diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the tittle diacritic.

    Returns
    -------
    Character
        The string with the tittle diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a tittle diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "tittle")


def stroke(string: str):
    """Returns the given character with a stroke diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the stroke diacritic.

    Returns
    -------
    Character
        The string with the stroke diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a stroke diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "stroke")


def interpunct(string: str):
    """Returns the given character with an interpunct diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the interpunct diacritic.

    Returns
    -------
    Character
        The string with the interpunct diacritic.

    Raises
    ------
    AccentError
        The given string could not be given an interpunct diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "interpunct")

def umlaut_and_macron(string: str):
    """Returns the given character with an umlaut and macron diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the umlaut and macron diacritic.

    Returns
    -------
    Character
        The string with the umlaut and macron diacritic.

    Raises
    ------
    AccentError
        The given string could not be given an umlaut and macron diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "umlaut_and_macron")


def ring_and_acute(string: str):
    """Returns the given character with a ring and acute diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the ring and acute diacritic.

    Returns
    -------
    Character
        The string with the ring and acute diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a ring and acute diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "ring_and_acute")


def stroke_and_acute(string: str):
    """Returns the given character with a stroke and acute diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the stroke and acute diacritic.

    Returns
    -------
    Character
        The string with the stroke and acute diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a stroke and acute diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "stroke_and_acute")

# Aliases

def diaresis(string: str):
    """Returns the given character with a diaresis diacritic (umlaut).

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the diaresis diacritic.

    Returns
    -------
    Character
        The string with the diaresis diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a diaresis diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "diaresis")

def diaresis_and_macron(string: str):
    """Returns the given character with a diaresis (umlaut) and macron diacritic.

    This function only takes a string of length 1.

    Parameters
    ----------
    string: str
        The string to give the diaresis and macron diacritic.

    Returns
    -------
    Character
        The string with the diaresis and macron diacritic.

    Raises
    ------
    AccentError
        The given string could not be given a diaresis and macron diacritic.
    TypeError
        The parameter was not a string.
    ValueError
        The string was not of length 1.
    """
    return _apply_diacritic(string, "diaresis_and_macron")


def clean_diacritics(string: str) -> str:
    """Returns the given string cleaned from diacritics.

    Parameters
    ----------
    string: Iterable
        The string to clean accents from.
    diacritics: Optional[List[str]]
        The list of diacritics to clean. If not provided, all diacritics will be cleaned.

    Returns
    -------
    str
        The cleaned string.
    """
    if not isinstance(string, str):
        raise TypeError(f"clean_diacritics function takes str, not {type(string).__name__}")

    ret = []

    for i in string:
        if i in _diacritic_cleaner_map.keys():
            ret.append(_diacritic_cleaner_map[i])
        else:
            ret.append(i)

    return "".join(ret)

def has_diacritics(string: _Iterable) -> bool:
    """Returns a bool as to whether the string contains diacritics.

    Parameters
    ----------
    string: Iterable
        The string to check.

    Returns
    -------
    bool
        Whether the string has diacritics.
    """
    if not isinstance(string, str):
        raise TypeError(f"has_diacritics function takes str, not {type(string).__name__}")

    for i in string:
        if i in _diacritic_cleaner_map.keys():
            return True
    return False

def get_diacritic_name_from_character(chararcter: _Iterable) -> str:
    """Get the diacritic name from a character.

    Parameters
    ----------
    chararcter: Iterable
        The character to get the diacritic for.

    Returns
    -------
    Union[str, None]
        The diacritic name.
    """
    if not chararcter in _diacritic_cleaner_map.keys():
        return
    
    for key in _diacritic_map.keys():
        for v in _diacritic_map[key].values():
            if chararcter.upper() == v:
                return key

def get_diacritics(string: _Iterable) -> _Dict[int, Character]:
    """Get all the diacritics from a string.

    Parameters
    ----------
    string: Iterable
        The string to get the diacritics from.

    Returns
    -------
    Dict[int, Character]
        A dict with str.index as the key,
        and Charaacter as the value.
    """
    if not isinstance(string, str):
        raise TypeError(f"get_diacritics function takes str, not {type(string).__name__}")

    ret = {}

    for i in string:
        if i in _diacritic_cleaner_map.keys():
            ret[string.index(i)] = Character(i, get_diacritic_name_from_character(i))
    
    return ret

def count_diacritics(string: _Iterable) -> int:
    """Returns a sum of all the characters with diacritics in a string.

    Parameters
    ----------
    string: Iterable
        The string count diacritics from.

    Returns
    -------
    int
        The number of diacritics.
    """
    return len(get_diacritics(string))

def cantake(characters: _Iterable, diacritic: str) -> bool:
    """Returns whether all characters in the iterable can take the given diacritic.

    Parameters
    ----------
    characters: Iterable
        The string count diacritics from.

    Returns
    -------
    int
        The number of diacritics.
    """
    if not isdiacritictype(diacritic):
        raise ValueError(f"'{diacritic}' is not a valid diacritic")
    
    for c in characters:
        try:
            _diacritic_map[diacritic][c.upper()]
        except KeyError:
            return False
    
    return True

def cantakelist(diacritic: str) -> _List[str]:
    """Returns every character that can take the diacritic.

    The list is returned as a list of strings in lower case.

    Parameters
    ----------
    diacritic: str
        The diacritic to get the cantake list for.

    Returns
    -------
    List[str]
        Each character in lower case that can take the diacritic.
    """
    if not isdiacritictype(diacritic):
        raise ValueError(f"'{diacritic}' is not a valid diacritic")
    return list(map(str.lower, _diacritic_map[diacritic].keys()))