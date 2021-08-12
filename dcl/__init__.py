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

from .functions import *

__version__ = "0.0.2"

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