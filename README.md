# Diacritics Library

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://user-images.githubusercontent.com/6032823/111363465-600fe880-8690-11eb-8377-ec1d4d5ff981.png)](https://github.com/PyCQA/isort)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

This library is used for adding, and removing diacritics from strings.

### Getting started

Start by importing the module:

```py
import dcl
```

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

Each accent has their own attribute which is directly accessible from the dcl module.

```py
dcl.acute('a')
>>> 'á'
```

These attributes return a Character object, which is essentially just a handy "wrapper" 
around our diacritic, which we can use to access various attributes to retrieve further 
information about the diacritic we're focusing on.

```py
char = dcl.ogonek('a')

repr(char)
>>> "<ogonek 'ą'>"

char.character  # the same as str(char)
>>> 'ą'

char.diacritic  # some return <unprintable>
>>> '˛'

char.diacritic_name
>>> 'ogonek'

char.raw  # returns the raw representation of our character
>>> '\U00000105'

char.raw_diacritic 
>>> '\U000002db'
```

Some functions can't take certain letters. For example, the letter ``h`` cannot take
a cedilla diacritic. In this case, an exception is raised named ``DiacriticError``.
You can access this exception via ``dcl.errors.DiacriticError``.

```py
from dcl.errors import DiacriticError

try:
    char = dcl.cedilla('h')
except DiacriticError as e:
    print(e)
else:
    print(repr(char))

>>> 'Character h cannot take a cedilla diacritic'
```

If you want to, you may also use the ``DiacriticApplicant`` object from 
``dcl.objects``. The functions you see above use this object too, and it's virtually
the same principle, except from the fact that we use properties to get the 
diacritic, and the class simply holds the string and it's properties. Alas with the 
functions above, this object also returns the same ``Character`` object through it's properties.

```py
from dcl.objects import DiacriticApplicant

da = DiacriticApplicant('a')
repr(da.ogonek)
>>> "<ogonek 'ą'>"
```

There is also the ``clean_diacritics`` function, accessible straight from the dcl module.
This function allows us to completely clean a string from any diacritics.

```py
dcl.clean_diacritics("Krëûšàdå")
>>> 'Kreusada'

dcl.clean_diacritics("Café")
>>> 'Cafe'
```

Along with this function, there's also ``count_diacritics``, ``get_diacritics`` and ``has_diacritics``.

The ``has_diacritics`` function simply checks if the string contains a character
with a diacritic.

```py
dcl.has_diacritics("Café")
>>> True

dcl.has_diacritics("dcl")
>>> False
```

The ``get_diacritics`` function is used to get all the diacritics in a string.
It returns a dictionary. For each diacritic in the string, the key will show
the diacritic's index in the string, and the value will show the ``Character``
representation. 

```py
dcl.get_diacritics("Café")
>>> {3: <acute 'é'>}

dcl.get_diacritics("Krëûšàdå")
>>> {2: <umlaut 'ë'>, 3: <circumflex 'û'>, 4: <caron 'š'>, 5: <grave 'à'>, 7: <ring 'å'>}
```

The ``count_diacritics`` function counts the number of diacritics in a string. The actual
implementation of this simply returns the dictionary length from ``get_diacritics``.

```py
dcl.count_diacritics("Café")
>>> 1
```

### Creating an end user program

Creating a program would be pretty simple for this, and I'd love to be able to help
you out with a base idea. Have a look at this for example:

```py
import dcl
import string

from dcl.errors import DiacriticError

char = str(input("Enter a character: "))
if not char in string.ascii_letters:
    print("Please enter a letter from a-Z.")
else:
    accent = str(input("Enter an accent, you can choose from the following: " + ", ".join(dcl.diacritic_list)))
    if not dcl.isdiacritictype(accent):
        print("That was not a valid accent.")
    else:
        try:
            function = getattr(dcl, accent)  # or dcl.objects.DiacriticApplicant
            output = function(char)
        except DiacriticError as e:
            print(e)
        else:
            print(str(output))
```

It's worth checking if the provided accent is a diacritic type. If it is, then you can use ``getattr``. 
Without checking, the user could provide a default global such as ``__file__``.

You can also create a program which can remove diacritics from a string. It's made easy!

```py
import dcl

string = str(input("Enter the string which you want to be cleared from diacritics: "))
print("Here is your cleaned string: " + dcl.clean_diacritics(string))
```

Or perhaps your program wants to count the number of diacritics contained
within your string.

```py
import dcl

string = str(input("This program will count the number of diacritics contained in your input. Enter a string: "))
count = dcl.count_diacritics(string)
if count == 1:
    grammar = "is"
else:
    grammar = "are"
print(f"There {grammar} {count} diacritics/accent in your string.")
```