# -*- coding: utf-8 -*-

'spells out numbers in supported languges'

from __future__ import absolute_import, unicode_literals

from num2words import num2words

from . import esperanto as eo

def spell(number, lang):
    'call the function for the specifc language'
    if lang == 'eo':
        return eo.spell(number)
    else:
        return num2words(number, lang=lang)
