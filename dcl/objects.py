from . import _diacritic_map, _diacritic_char_map
from .errors import DiacriticError

__all__ = ("DiacriticApplicant", "Character")


class Character:
    def __init__(self, char, diacritic_name):
        self.character = char
        self.raw = f"\\U{f'{ord(char):x}':>08}"
        self.diacritic = _diacritic_char_map.get(diacritic_name, "<unprintable>")
        if self.diacritic == "<unprintable>":
            self.raw_diacritic = self.diacritic
        else:
            self.raw_diacritic = f"\\U{f'{ord(self.diacritic):x}':>08}"
        self.diacritic_name = diacritic_name

    def __repr__(self):
        return "<{0.diacritic_name} '{0.character}'>".format(self)

    def __str__(self):
        return self.character

class DiacriticApplicant(object):
    """An object used for applying diacritics to letters.
    
    Initialize the class with a single letter.
    """

    def __init__(self, character):
        if not isinstance(character, str):
            raise TypeError("Must be str, not {}".format(type(character).__name__))
        if len(character) != 1:
            raise ValueError("Given character must be of len 1, not {}".format(str(len(character))))
        
        self.character = character

    def __str__(self):
        return self.character

    def __repr__(self):
        return f"<{self.__class__.__name__} '{self.character}>"

    def _fetch_diacritic(self, diacritic):
        try:
            char = _diacritic_map[diacritic][self.character.upper()]
        except KeyError:
            grammar = "a"
            diacritic = diacritic.replace("_", " ")
            if diacritic[0] in "aeiou":
                grammar += "n"
            raise DiacriticError(self.character, diacritic) from None
        if self.character.islower():
            char = char.lower()
        return Character(char, diacritic)

    @property
    def grave(self):
        return self._fetch_diacritic("grave")

    @property
    def acute(self):
        return self._fetch_diacritic("acute")

    @property
    def circumflex(self):
        return self._fetch_diacritic("circumflex")

    @property
    def tilde(self):
        return self._fetch_diacritic("tilde")

    @property
    def umlaut(self):
        return self._fetch_diacritic("umlaut")

    @property
    def caron(self):
        return self._fetch_diacritic("caron")

    @property
    def ring(self):
        return self._fetch_diacritic("ring")

    @property
    def cedilla(self):
        return self._fetch_diacritic("cedilla")

    @property
    def slash(self):
        return self._fetch_diacritic("slash")

    @property
    def ogonek(self):
        return self._fetch_diacritic("ogonek")

    @property
    def macron(self):
        return self._fetch_diacritic("macron")

    @property
    def breve(self):
        return self._fetch_diacritic("breve")

    @property
    def tittle(self):
        return self._fetch_diacritic("tittle")

    @property
    def stroke(self):
        return self._fetch_diacritic("stroke")

    @property
    def interpunct(self):
        return self._fetch_diacritic("interpunct")

    @property
    def umlaut_and_macron(self):
        return self._fetch_diacritic("umlaut_and_macron")

    @property
    def ring_and_acute(self):
        return self._fetch_diacritic("ring_and_acute")

    @property
    def stroke_and_acute(self):
        return self._fetch_diacritic("stroke_and_acute")

    # Aliases

    @property
    def diaresis(self):
        return self.umlaut

    @property
    def diaresis_and_macron(self):
        return self.umlaut_and_macron