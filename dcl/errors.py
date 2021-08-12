class DiacriticError(Exception):
    """Used when a diacritic cannot be applied"""

    def __init__(self, char, diacritic):
        grammar = "a"
        if diacritic[0] in "aeiou":
            grammar += "n"
        super().__init__(f"Character {char} cannot take {grammar} {diacritic} diacritic")
