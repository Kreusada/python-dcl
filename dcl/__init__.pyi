from enum import Flag
from typing import overload

__version__: str

class Diacritic(Flag):
    ACUTE: Diacritic
    BAR: Diacritic
    BELT: Diacritic
    BREVE: Diacritic
    BREVEBELOW: Diacritic
    CARON: Diacritic
    CEDILLA: Diacritic
    CIRCUMFLEX: Diacritic
    CIRCUMFLEXBELOW: Diacritic
    COMMABELOW: Diacritic
    CROSSEDTAIL: Diacritic
    DESCENDER: Diacritic
    DIAERESIS: Diacritic
    DIAERESISBELOW: Diacritic
    DIAGONALSTROKE: Diacritic
    DOT: Diacritic
    DOTABOVE: Diacritic
    DOTBELOW: Diacritic
    DOUBLEACUTE: Diacritic
    DOUBLEBAR: Diacritic
    DOUBLEGRAVE: Diacritic
    FLOURISH: Diacritic
    GRAVE: Diacritic
    HIGHSTROKE: Diacritic
    HOOK: Diacritic
    HOOKABOVE: Diacritic
    HOOKTAIL: Diacritic
    HORN: Diacritic
    INVERTEDBREVE: Diacritic
    LEFTHOOK: Diacritic
    LINEBELOW: Diacritic
    LONGRIGHTLEG: Diacritic
    LONGSTROKEOVERLAY: Diacritic
    LOOP: Diacritic
    MACRON: Diacritic
    MIDDLEDOT: Diacritic
    MIDDLETILDE: Diacritic
    OBLIQUESTROKE: Diacritic
    OGONEK: Diacritic
    PALATALHOOK: Diacritic
    RETROFLEXHOOK: Diacritic
    RINGABOVE: Diacritic
    RINGBELOW: Diacritic
    SHORTSTROKEOVERLAY: Diacritic
    SQUIRRELTAIL: Diacritic
    STROKE: Diacritic
    STROKETHROUGHDESCENDER: Diacritic
    SWASHTAIL: Diacritic
    TAIL: Diacritic
    TILDE: Diacritic
    TILDEBELOW: Diacritic
    TOPBAR: Diacritic

    # Aliases
    OVERDOT: Diacritic
    UNDERDOT: Diacritic
    UMLAUT: Diacritic

ACUTE: Diacritic
BAR: Diacritic
BELT: Diacritic
BREVE: Diacritic
BREVEBELOW: Diacritic
CARON: Diacritic
CEDILLA: Diacritic
CIRCUMFLEX: Diacritic
CIRCUMFLEXBELOW: Diacritic
COMMABELOW: Diacritic
CROSSEDTAIL: Diacritic
DESCENDER: Diacritic
DIAERESIS: Diacritic
DIAERESISBELOW: Diacritic
DIAGONALSTROKE: Diacritic
DOT: Diacritic
DOTABOVE: Diacritic
DOTBELOW: Diacritic
DOUBLEACUTE: Diacritic
DOUBLEBAR: Diacritic
DOUBLEGRAVE: Diacritic
FLOURISH: Diacritic
GRAVE: Diacritic
HIGHSTROKE: Diacritic
HOOK: Diacritic
HOOKABOVE: Diacritic
HOOKTAIL: Diacritic
HORN: Diacritic
INVERTEDBREVE: Diacritic
LEFTHOOK: Diacritic
LINEBELOW: Diacritic
LONGRIGHTLEG: Diacritic
LONGSTROKEOVERLAY: Diacritic
LOOP: Diacritic
MACRON: Diacritic
MIDDLEDOT: Diacritic
MIDDLETILDE: Diacritic
OBLIQUESTROKE: Diacritic
OGONEK: Diacritic
PALATALHOOK: Diacritic
RETROFLEXHOOK: Diacritic
RINGABOVE: Diacritic
RINGBELOW: Diacritic
SHORTSTROKEOVERLAY: Diacritic
SQUIRRELTAIL: Diacritic
STROKE: Diacritic
STROKETHROUGHDESCENDER: Diacritic
SWASHTAIL: Diacritic
TAIL: Diacritic
TILDE: Diacritic
TILDEBELOW: Diacritic
TOPBAR: Diacritic

# Aliases
OVERDOT: Diacritic
UNDERDOT: Diacritic
UMLAUT: Diacritic

def apply(character: str, /, diacritic: Diacritic) -> str: ...
def identify(string: str, /) -> Diacritic | None: ...
def identifyall(string: str, /) -> dict[int, Diacritic | None]: ...
def contains(string: str, /, diacritic: Diacritic | None = None) -> bool: ...
def find(string: str, /, diacritic: Diacritic) -> list[int]: ...
def remove(string: str, /, diacritic: Diacritic) -> str: ...
def normalize(string: str, /) -> str: ...
def substitute(string: str, /, old: Diacritic | None, new: Diacritic | None) -> str: ...
def replace(string: str, /, character: str, diacritic: Diacritic) -> str: ...
def count(string: str, /, diacritic: Diacritic) -> int: ...
@overload
def applicable(character: str, /) -> list[Diacritic]: ...
@overload
def applicable(diacritic: Diacritic, /) -> list[str]: ...
def applicable(diacritic_or_character: Diacritic | str, /) -> list[str | Diacritic]: ...

# Aliases
normalise = normalize

class DiacriticTransformer(str):
    def apply_diacritic(self, diacritic: Diacritic) -> DiacriticTransformer: ...
    def identify_diacritic(self) -> Diacritic | None: ...
    def identify_all_diacritics(self) -> dict[int, Diacritic | None]: ...
    def contains_diacritic(self, diacritic: Diacritic | None = None) -> bool: ...
    def find_diacritic(self, diacritic: Diacritic) -> list[int]: ...
    def remove_diacritic(self, diacritic: Diacritic) -> DiacriticTransformer: ...
    def normalize_diacritics(self) -> DiacriticTransformer: ...
    def substitute_diacritics(
        self, old: Diacritic | None, new: Diacritic | None
    ) -> DiacriticTransformer: ...
    def replace_diacritics(
        self, character: str, diacritic: Diacritic
    ) -> DiacriticTransformer: ...
    def count_diacritics(self, diacritic: Diacritic) -> int: ...
    @overload
    def applicable(self, character: str, /) -> list[Diacritic]: ...
    @overload
    def applicable(self, diacritic: Diacritic, /) -> list[str]: ...
    def applicable(
        self, diacritic_or_character: Diacritic | str, /
    ) -> list[str | Diacritic]: ...

    # Aliases
    normalise_diacritics = normalize_diacritics

del Flag, overload
