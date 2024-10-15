from enum import Flag
from typing import Iterable, Literal, overload

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

def apply(string: str, /, diacritic: Diacritic) -> str: ...
def identify(string: str, /) -> Diacritic | None: ...
def identifyall(string: str, /) -> dict[int, Diacritic | None]: ...
def contains(string: str, /, diacritic: Diacritic | Literal["any"] = "any") -> bool: ...
def find(string: str, /, diacritic: Diacritic) -> list[int]: ...
def normalize(string: str, /, diacritic: Diacritic | Literal["any"] = "any") -> str: ...
def count(string: str, /, diacritic: Diacritic | Literal["any"] = "any") -> int: ...
@overload
def applicable(character: str, /) -> list[Diacritic]: ...
@overload
def applicable(diacritic: Diacritic, /) -> list[str]: ...
def applicable(diacritic_or_character: Diacritic | str, /) -> list[str | Diacritic]: ...
def substitute(
    string: str,
    /,
    *,
    old_diacritic: Diacritic | Literal["any"] | None,
    new_diacritic: Diacritic | None,
    focus_characters: str | Iterable[str] = "",
) -> str: ...

# Aliases
normalise = normalize
replace = substitute

class DiacriticTransformer(str):
    def apply_diacritic(self, diacritic: Diacritic) -> DiacriticTransformer: ...
    def identify_diacritic(self) -> Diacritic | None: ...
    def identify_all_diacritics(self) -> dict[int, Diacritic | None]: ...
    def contains_diacritic(
        self, diacritic: Diacritic | Literal["any"] = "any"
    ) -> bool: ...
    def find_diacritic(self, diacritic: Diacritic) -> list[int]: ...
    def normalize_diacritics(
        self, diacritic: Diacritic | Literal["any"] = "any"
    ) -> DiacriticTransformer: ...
    def count_diacritic(self, diacritic: Diacritic | Literal["any"] = "any") -> int: ...
    def applicable_diacritics(self) -> list[Diacritic]: ...
    def substitute_diacritics(
        self,
        string: str,
        /,
        *,
        old_diacritic: Diacritic | Literal["any"] | None,
        new_diacritic: Diacritic | None,
        focus_characters: str | Iterable[str] = "",
    ) -> DiacriticTransformer: ...

    # Aliases
    normalise_diacritics = normalize_diacritics
    replace_diacritics = substitute_diacritics

del Flag, Iterable, Literal, overload
