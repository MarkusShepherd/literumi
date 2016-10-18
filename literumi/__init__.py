# -*- coding: utf-8 -*-

'''spells out numbers in supported languges'''

from __future__ import absolute_import, unicode_literals

from functools import partial

import roman

from num2words import num2words

from . import binary
from . import esperanto

LANGUAGES = {
    'binary': {'name': 'binary', 'function': binary.spell},
    'de': {'name': 'German', 'function': partial(num2words, lang='de')},
    'de_DE': {'name': 'German (Germany)', 'function': partial(num2words, lang='de')},
    'de_CH': {'name': 'German (Switzerland)',
              'function': lambda x: num2words(x, lang='de').replace('ß', 'ss')},
    'da': {'name': 'Danish', 'function': partial(num2words, lang='dk')},
    'en': {'name': 'English', 'function': partial(num2words, lang='en')},
    'en_GB': {'name': 'English (Great Britain)', 'function': partial(num2words, lang='en_GB')},
    'en_IN': {'name': 'English (India)', 'function': partial(num2words, lang='en_IN')},
    'eo': {'name': 'Esperanto', 'function': esperanto.spell},
    'es': {'name': 'Spanish', 'function': partial(num2words, lang='es')},
    'fr': {'name': 'French', 'function': partial(num2words, lang='fr')},
    'fr_FR': {'name': 'French (France)', 'function': partial(num2words, lang='fr')},
    'fr_CH': {'name': 'French (Switzerland)', 'function': partial(num2words, lang='fr_CH')},
    'id': {'name': 'Indonesian', 'function': partial(num2words, lang='id')},
    'lt': {'name': 'Lithuanian', 'function': partial(num2words, lang='lt')},
    'lv': {'name': 'Latvian', 'function': partial(num2words, lang='lv')},
    'no': {'name': 'Norwegian', 'function': partial(num2words, lang='no')},
    'pl': {'name': 'Polish', 'function': partial(num2words, lang='pl')},
    'pt': {'name': 'Portuguese', 'function': partial(num2words, lang='pt_BR')},
    'pt_BR': {'name': 'Portuguese (Brazil)', 'function': partial(num2words, lang='pt_BR')},
    'roman': {'name': 'Roman numerals', 'function': roman.toRoman},
    'ru': {'name': 'Russian', 'function': partial(num2words, lang='ru')},
}

def spell(number, lang):
    '''call the function for the specific language'''

    language = LANGUAGES.get(lang)
    if not language:
        language = LANGUAGES.get(lang[:2])

    if not language:
        raise NotImplementedError('language "{}" is not supported'.format(lang))

    return language['function'](number)
