# -*- coding: utf-8 -*-

'spells out numbers in supported languges'

from __future__ import absolute_import, unicode_literals

from num2words import num2words

from . import binary
from . import esperanto

LANGUAGES = {
	'binary': {'name': 'binary', 'function': binary.spell},
	'eo': {'name': 'Esperanto', 'function': esperanto.spell},
}

def spell(number, lang):
    'call the function for the specifc language'

    lanugage = LANGUAGES.get(lang)

    if lanugage:
        return lanugage['function'](number)
    else:
        return num2words(number, lang=lang)
