from typing import Iterable as _Iterable

from ._maps import _diacritic_cleaner_map, _diacritic_map
from .objects import DiacriticApplicant, Character


__all__ = (
    "grave",
    "acute",
    "circumflex",
    "tilde",
    "umlaut",
    "caron",
    "ring",
    "cedilla",
    "slash",
    "ogonek",
    "macron",
    "breve",
    "tittle",
    "stroke",
    "interpunct",
    "umlaut_and_macron",
    "ring_and_acute",
    "stroke_and_acute",
    "diaresis",
    "diaresis_and_macron",
    "clean_diacritics",
    "has_diacritics",
    "get_diacritic_name_from_character",
    "get_diacritics",
    "count_diacritics",
)

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


def clean_diacritics(string: _Iterable) -> str:
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

def has_diacritics(string: _Iterable) -> str:
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

def get_diacritics(string: _Iterable) -> str:
    """Get all the diacritics from a string.

    Parameters
    ----------
    string: Iterable
        The string to get the diacritics from.

    Returns
    -------
    dict
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

def count_diacritics(string: _Iterable) -> str:
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
