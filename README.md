# DCL - Diacritics Composition Library

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://user-images.githubusercontent.com/6032823/111363465-600fe880-8690-11eb-8377-ec1d4d5ff981.png)](https://github.com/PyCQA/isort)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

This library is for working with diacritics in multilingual Latin-based text.
It provides functionality for adding, removing, modifying and processing diacritic marks,
supporting functions for orthographic and linguistic analysis.

### Getting started

The DCL library supports the following diacritic marks (note: not all examples may appear depending on your browser/site's support):

| Diacritic              |   Applicable | Example   | Attribute                  |
|------------------------|--------------|-----------|----------------------------|
| Acute                  |           34 | Á         | dcl.ACUTE                  |
| Bar                    |            4 | Ꞓ         | dcl.BAR                    |
| Belt                   |            2 | Ɬ         | dcl.BELT                   |
| Breve                  |           12 | Ă         | dcl.BREVE                  |
| Breve Below             |            2 | Ḫ         | dcl.BREVEBELOW             |
| Caron                  |           32 | Ǎ         | dcl.CARON                  |
| Cedilla                |           22 | Ç         | dcl.CEDILLA                |
| Circumflex             |           26 | Â         | dcl.CIRCUMFLEX             |
| Circumflex Below        |           12 | Ḓ         | dcl.CIRCUMFLEXBELOW        |
| Comma Below             |            4 | Ș         | dcl.COMMABELOW             |
| Crossed Tail            |            2 | Ʝ         | dcl.CROSSEDTAIL            |
| Descender              |            8 | Ⱨ         | dcl.DESCENDER              |
| Diaeresis              |           18 | Ä         | dcl.DIAERESIS              |
| Diaeresis Below         |            2 | Ṳ         | dcl.DIAERESISBELOW         |
| Diagonal Stroke         |            8 | Ꝃ         | dcl.DIAGONALSTROKE         |
| Dot                    |            2 | Ꜿ         | dcl.DOT                    |
| Dot Above               |           40 | Ȧ         | dcl.DOTABOVE               |
| Dot Below               |           38 | Ạ         | dcl.DOTBELOW               |
| Double Acute            |            4 | Ő         | dcl.DOUBLEACUTE            |
| Double Bar              |            2 | Ⱡ         | dcl.DOUBLEBAR              |
| Double Grave            |           12 | Ȁ         | dcl.DOUBLEGRAVE            |
| Flourish               |            4 | Ꞗ         | dcl.FLOURISH               |
| Grave                  |           16 | À         | dcl.GRAVE                  |
| High Stroke             |            2 | Ꝉ         | dcl.HIGHSTROKE             |
| Hook                   |           30 | Ɓ         | dcl.HOOK                   |
| Hook Above              |           12 | Ả         | dcl.HOOKABOVE              |
| Hook Tail               |            2 | Ɋ         | dcl.HOOKTAIL               |
| Horn                   |            4 | Ơ         | dcl.HORN                   |
| Inverted Breve          |           12 | Ȃ         | dcl.INVERTEDBREVE          |
| Left Hook               |            2 | Ɲ         | dcl.LEFTHOOK               |
| Line Below              |           16 | Ḇ         | dcl.LINEBELOW              |
| Long Right Leg           |            2 | Ƞ         | dcl.LONGRIGHTLEG           |
| Long Stroke Overlay      |            2 | Ꝋ         | dcl.LONGSTROKEOVERLAY      |
| Loop                   |            4 | Ꝍ         | dcl.LOOP                   |
| Macron                 |           14 | Ā         | dcl.MACRON                 |
| Middle Dot              |            2 | Ŀ         | dcl.MIDDLEDOT              |
| Middle Tilde            |            4 | Ɫ         | dcl.MIDDLETILDE            |
| Oblique Stroke          |           10 | Ꞡ         | dcl.OBLIQUESTROKE          |
| Ogonek                 |           10 | Ą         | dcl.OGONEK                 |
| Palatal Hook            |            4 | Ꞔ         | dcl.PALATALHOOK            |
| Retroflex Hook          |            2 | Ʈ         | dcl.RETROFLEXHOOK          |
| Ring Above              |            4 | Å         | dcl.RINGABOVE              |
| Ring Below              |            2 | Ḁ         | dcl.RINGBELOW              |
| Short Stroke Overlay     |            4 | Ꟈ         | dcl.SHORTSTROKEOVERLAY     |
| Squirrel Tail           |            2 | Ꝕ         | dcl.SQUIRRELTAIL           |
| Stroke                 |           38 | Ⱥ         | dcl.STROKE                 |
| Stroke Through Descender |            4 | Ꝑ         | dcl.STROKETHROUGHDESCENDER |
| Swash Tail              |            4 | Ȿ         | dcl.SWASHTAIL              |
| Tail                   |            2 | Ɽ         | dcl.TAIL                   |
| Tilde                  |           16 | Ã         | dcl.TILDE                  |
| Tilde Below             |            6 | Ḛ         | dcl.TILDEBELOW             |
| Topbar                 |            4 | Ƃ         | dcl.TOPBAR                 |

And for combined diacritic marks...

| Diacritic               |   Applicable | Example   | Attribute                        |
|-------------------------|--------------|-----------|----------------------------------|
| Acute & Breve           |            2 | Ắ         | dcl.ACUTE \| dcl.BREVE           |
| Acute & Cedilla         |            2 | Ḉ         | dcl.ACUTE \| dcl.CEDILLA         |
| Acute & Circumflex      |            6 | Ấ         | dcl.ACUTE \| dcl.CIRCUMFLEX      |
| Acute & Diaeresis       |            4 | Ḯ         | dcl.ACUTE \| dcl.DIAERESIS       |
| Acute & Dot Above        |            2 | Ṥ         | dcl.ACUTE \| dcl.DOTABOVE        |
| Acute & Horn            |            4 | Ớ         | dcl.ACUTE \| dcl.HORN            |
| Acute & Macron          |            4 | Ḗ         | dcl.ACUTE \| dcl.MACRON          |
| Acute & Ring Above       |            2 | Ǻ         | dcl.ACUTE \| dcl.RINGABOVE       |
| Acute & Stroke          |            2 | Ǿ         | dcl.ACUTE \| dcl.STROKE          |
| Acute & Tilde           |            4 | Ṍ         | dcl.ACUTE \| dcl.TILDE           |
| Breve & Cedilla         |            2 | Ḝ         | dcl.BREVE \| dcl.CEDILLA         |
| Breve & Dot Below        |            2 | Ặ         | dcl.BREVE \| dcl.DOTBELOW        |
| Breve & Grave           |            2 | Ằ         | dcl.BREVE \| dcl.GRAVE           |
| Breve & Hook Above       |            2 | Ẳ         | dcl.BREVE \| dcl.HOOKABOVE       |
| Breve & Tilde           |            2 | Ẵ         | dcl.BREVE \| dcl.TILDE           |
| Caron & Diaeresis       |            2 | Ǚ         | dcl.CARON \| dcl.DIAERESIS       |
| Caron & Dot Above        |            2 | Ṧ         | dcl.CARON \| dcl.DOTABOVE        |
| Circumflex & Dot Below   |            6 | Ậ         | dcl.CIRCUMFLEX \| dcl.DOTBELOW   |
| Circumflex & Grave      |            6 | Ầ         | dcl.CIRCUMFLEX \| dcl.GRAVE      |
| Circumflex & Hook Above  |            6 | Ẩ         | dcl.CIRCUMFLEX \| dcl.HOOKABOVE  |
| Circumflex & Tilde      |            6 | Ẫ         | dcl.CIRCUMFLEX \| dcl.TILDE      |
| Diaeresis & Grave       |            2 | Ǜ         | dcl.DIAERESIS \| dcl.GRAVE       |
| Diaeresis & Macron      |            2 | Ṻ         | dcl.DIAERESIS \| dcl.MACRON      |
| Diaeresis & Tilde       |            2 | Ṏ         | dcl.DIAERESIS \| dcl.TILDE       |
| Diagonal Stroke & Stroke |            2 | Ꝅ         | dcl.DIAGONALSTROKE \| dcl.STROKE |
| Dot Above & Dot Below     |            2 | Ṩ         | dcl.DOTABOVE \| dcl.DOTBELOW     |
| Dot Above & Macron       |            4 | Ǡ         | dcl.DOTABOVE \| dcl.MACRON       |
| Dot Below & Horn         |            4 | Ợ         | dcl.DOTBELOW \| dcl.HORN         |
| Dot Below & Macron       |            4 | Ḹ         | dcl.DOTBELOW \| dcl.MACRON       |
| Grave & Horn            |            4 | Ờ         | dcl.GRAVE \| dcl.HORN            |
| Grave & Macron          |            4 | Ḕ         | dcl.GRAVE \| dcl.MACRON          |
| Hook Above & Horn        |            4 | Ở         | dcl.HOOKABOVE \| dcl.HORN        |
| Horn & Tilde            |            4 | Ỡ         | dcl.HORN \| dcl.TILDE            |
| Macron & Ogonek         |            2 | Ǭ         | dcl.MACRON \| dcl.OGONEK         |
| Macron & Tilde          |            2 | Ȭ         | dcl.MACRON \| dcl.TILDE          |

Start by importing the module:

```py
import dcl
```

Diacritic types are expressed as **global enum members**, available as direct attributes
from the module. Take capital A with the ogonek diacritic mark (``Ą``) as an example.
This ogonek diacritic is represented by ``dcl.OGONEK``, and this member can be used whenever
the ogonek diacritic is to be added, removed or processed.

Some diacritics are a combination of two diacritic marks. For example, capital C with cedilla
and acute diacritic marks (``Ḉ``). This letter uses both cedilla and acute diacritics, therefore
we can reference this combination as ``dcl.CEDILLA | dcl.ACUTE`` within our code.

Whilst this may seem confusing at first, it will become easy when put into practice. Lets look
at the functions.

### Function - ``dcl.applicable``

This function returns a list that determines either:
- Which diacritic marks are applicable for the given character
- Which characters are applicable for the given diacritic

This is based on what is available in the unicode library.

**Give a diacritic and see what characters can use that diacritic mark**

```py
>>> dcl.applicable(dcl.STROKE)
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'O', 'P', 'R', 'T', 'U', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'o', 'p', 'r', 't', 'u', 'y', 'z']

>>> dcl.applicable(dcl.RETROFLEXHOOK)
['T', 't']

>>> dcl.applicable(dcl.ACUTE | dcl.TILDE)
['O', 'U', 'o', 'u']
```

**Give a character and see what diacritic marks it could have**

```py
>>> dcl.applicable("A")
[dcl.ACUTE, dcl.BREVE, dcl.ACUTE|dcl.BREVE, dcl.BREVE|dcl.DOTBELOW, dcl.BREVE|dcl.GRAVE, dcl.BREVE|dcl.HOOKABOVE, dcl.BREVE|dcl.TILDE, dcl.CARON, dcl.CIRCUMFLEX, dcl.ACUTE|dcl.CIRCUMFLEX, dcl.CIRCUMFLEX|dcl.DOTBELOW, dcl.CIRCUMFLEX|dcl.GRAVE, dcl.CIRCUMFLEX|dcl.HOOKABOVE, dcl.CIRCUMFLEX|dcl.TILDE, dcl.DIAERESIS, dcl.DOTABOVE, dcl.DOTABOVE|dcl.MACRON, dcl.DOTBELOW, dcl.DOUBLEGRAVE, dcl.GRAVE, dcl.HOOKABOVE, dcl.INVERTEDBREVE, dcl.MACRON, dcl.OGONEK, dcl.RINGABOVE, dcl.ACUTE|dcl.RINGABOVE, dcl.RINGBELOW, dcl.STROKE, dcl.TILDE]

>>> dcl.applicable("z")
[dcl.ACUTE, dcl.CARON, dcl.CIRCUMFLEX, dcl.DESCENDER, dcl.DOTABOVE, dcl.DOTBELOW, dcl.HOOK, dcl.LINEBELOW, dcl.PALATALHOOK, dcl.STROKE, dcl.SWASHTAIL]

>>> dcl.applicable("K")
[dcl.ACUTE, dcl.CARON, dcl.CEDILLA, dcl.DESCENDER, dcl.DIAGONALSTROKE, dcl.DOTBELOW, dcl.HOOK, dcl.LINEBELOW, dcl.OBLIQUESTROKE, dcl.STROKE, dcl.DIAGONALSTROKE|dcl.STROKE]
```

### Function - ``dcl.apply``

This function is used to apply a given diacritic to each character in the given string. It takes two arguments,
the string to apply the diacritic mark to, and the diacritic itself.

```py
>>> dcl.apply("a", dcl.DIAERESIS)
'ä'

>>> dcl.apply("K", dcl.ACUTE)
'Ḱ'

>>> dcl.apply("O", dcl.CIRCUMFLEX | dcl.DOTBELOW)
'Ộ'

>>> dcl.apply("Kreus", dcl.ACUTE)
'Ḱŕéúś'
```

It will error if you don't pass a one-length string, or if the character passed does not support
the given diacritic.

### Function - ``dcl.contains``

This function is used to check whether a string contains a certain diacritic, or any diacritic.
It takes two arguments, the string to check, and the diacritic mark (optional). If no diacritic is
passed, it will check for any diacritic (default argument: ``"any"``).

```py
>>> dcl.contains("Brötchen", dcl.DIAERESIS) # it contains a diaeresis (ö)
True

>>> dcl.contains("Jalapeño", dcl.TILDE) # it contains a tilde (ñ)
True

>>> dcl.contains("Façade", dcl.MACRON) # it contains a cedilla (ç), but that is not a macron
False

>>> dcl.contains("New York", dcl.DESCENDER) # it does not contain a descender
False

>>> dcl.contains("Łódź") # it contains any diacritic mark
True

>>> dcl.contains("Apple") # it does not contain any diacritic mark
False
```

### Function - ``dcl.count``

This function counts how many characters there are that have diacritic marks. Like the ``dcl.contains``
function, this function takes two arguments with the string and the diacritic mark (optional). If no diacritic
is passed, it will count for any diacritic (default argument: ``"any"``).

```py
>>> dcl.count("Brötchen", dcl.DIAERESIS) # it has 1 diaeresis (ö)
1

>>> dcl.count("Brötchen", dcl.HOOK) # it has 1 diaeresis (ö), but that is not a hook
0

>>> dcl.count("Jalapeño") # it has 1 tilde (ñ)
1

>>> dcl.count("Jalapeños in Łódź") # it has 4 diacritic marks (ñ, Ł, ó, ź)
4

>>> dcl.count("Jalapeños in Łódź", dcl.ACUTE) # it has 2 acute (ó, ź)
2
```

### Function - ``dcl.find``

This function returns the indexes in which the string has a particular diacritic, or any diacritic.

```py
>>> dcl.find("Māori", dcl.MACRON) # macron found at index 1
[1]

>>> dcl.find("Hhǎčék", dcl.CARON) # caron found at indexes 2 and 3
[2, 3]

>>> dcl.find("Hhǎčék") # diacritic marks found at indexes 2, 3 and 4
[2, 3, 4]

>>> dcl.find("Apple", dcl.OBLIQUESTROKE) # no oblique strokes found
[]

>>> dcl.find("Mountain") # no diacritic marks found
[]
```

### Function - ``dcl.identify``

This function identifies the diacritic applied to the given character.

```py
>>> dcl.identify("é") # diacritic mark is acute
dcl.ACUTE

>>> dcl.identify("Ꝕ") # diacritic mark is squirrel tail
dcl.SQUIRRELTAIL

>>> dcl.identify("B") # no diacritic mark associated with this character
None
```

### Function - ``dcl.identifyall``

This function identifies all diacritics contained in a string, returning a
dictionary mapping where the keys are the indexes, and the values are the diacritic
or None.

```py
>>> dcl.identifyall("Hhǎčék") # caron at indexes 2 and 3, acute at index 4
{0: None, 1: None, 2: dcl.CARON, 3: dcl.CARON, 4: dcl.ACUTE, 5: None}

>>> dcl.identifyall("Loŝùň") # circumflex at index 2, grave at index 3, caron at index 4
{0: None, 1: None, 2: dcl.CIRCUMFLEX, 3: dcl.GRAVE, 4: dcl.CARON}

>>> dcl.identifyall("Apple") # no diacritic marks found
{0: None, 1: None, 2: None, 3: None, 4: None}
```

### Function - ``dcl.normalize``

This function removes diacritics from a string. It takes two arguments, the string itself,
and the diacritic to remove. If no diacritic is passed, it will remove all diacritic marks (default argument: ``"any"``).

This function has an alias named ``normalise``.

```py
>>> dcl.normalize("Hhǎčék") # no diacritic mark passed, removing all diacritic marks
'Hhacek'

>>> dcl.normalize("Hhǎčék", dcl.CARON) # caron passed, can remove 2/3 diacritic marks
'Hhacék'

>>> dcl.normalize("Brötchen", dcl.SWASHTAIL) # swash tail passed, Brötchen does not contain swash tail
'Brötchen'
```

### Function - ``dcl.substitute``

Substitutes characters in a string containing (or not containing) diacritics. There 
are four arguments, the first being **positional** and the latter three being
**keyword-only**:

- ``string`` - The string to transform.
- ``old_diacritic`` - The old diacritic to substitute. Must be a valid diacritic, or ``None`` (no diacritic mark), or ``"any"`` to replace any diacritic marks.
- ``new_diacritic`` - The new diacritic to substitute the old with. Must be a valid diacritic or ``None`` (no diacritic).
- ``focus_characters`` - An iterable of characters that the substitution applies to. Can also pass ``None`` to not focus on any characters.

This function has an alias named ``replace``. Lets
visualize some examples to make it easier to understand:

```py
>>> string = "Şiņgęrőş"
>>> dcl.substitute(string, old_diacritic=dcl.CEDILLA, new_diacritic=dcl.ACUTE) # we can change the cedilla marks into acute marks like this
'Śińgęrőś'

# same as above, but we will focus on just the Ş and ş in Şiņgęrőş (must pass S and s, case sensitive)
>>> dcl.substitute(string, old_diacritic=dcl.CEDILLA, new_diacritic=dcl.ACUTE, focus_characters="Ss")
'Śiņgęrőś' # the acute is now only applied to Ş and ş, the ņ retains its cedila diacritic because of focus_characters

>>> dcl.substitute("Lìberò", old_diacritic=dcl.GRAVE, new_diacritic=None) # normalise grave diacritics in Lìberò
'Libero'

>>> dcl.substitute("Ǭbȯľĕ", old_diacritic=dcl.MACRON | dcl.OGONEK, new_diacritic=None) # normalise Ǭ in Ǭbȯľĕ
'Obȯľĕ'

# replacing vowels without a diacritic to have an ogonek diacritic in an arbitrary string
>>> dcl.substitute("café au lait", old_diacritic=None, new_diacritic=dcl.OGONEK, focus_characters="aeiou")
'cąfé ąų ląįt'
```

### Object-Oriented Diacritic Handling - ``dcl.DiacriticTransformer``

For more intricate modification and processing of diacritics, the object-oriented approach may suit you better.
All of the module's operations are bundled into a string subclass, facilitating chained operations and negating
the need to repeat strings in function calls. Initialize the class with the string you'd like to modify,
and then access its methods which are renamed appropriately so that the names do not clash with base string methods.

The ``dcl`` methods that return strings will instead return ``dcl.DiacriticTransformer``. As a string subclass,
methods are pure and have no side-effects. The methods are named as followed:


| Module function name | Method name                                          |
|----------------------|------------------------------------------------------|
| ``dcl.applicable``   | ``dcl.DiacriticTransformer.applicable_diacritics``   |
| ``dcl.apply``        | ``dcl.DiacriticTransformer.apply_diacritic``         |
| ``dcl.contains``     | ``dcl.DiacriticTransformer.contains_diacritic``      |
| ``dcl.count``        | ``dcl.DiacriticTransformer.count_diacritic``         |
| ``dcl.find``         | ``dcl.DiacriticTransformer.find_diacritic``          |
| ``dcl.identify``     | ``dcl.DiacriticTransformer.identify_diacritic``      |
| ``dcl.identifyall``  | ``dcl.DiacriticTransformer.identify_all_diacritics`` |
| ``dcl.normalize``    | ``dcl.DiacriticTransformer.normalize_diacritics``    |
| ``dcl.substitute``   | ``dcl.DiacriticTransformer.substitite_diacritics``   |