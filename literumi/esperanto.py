# -*- coding: utf-8 -*-

'''spells out numbers in Esperanto'''

from __future__ import absolute_import, division, print_function, unicode_literals

import sys

NUMBERS = {
    0: 'nulo',
    1: 'unu',
    2: 'du',
    3: 'tri',
    4: 'kvar',
    5: 'kvin',
    6: 'ses',
    7: 'sep',
    8: 'ok',
    9: 'naŭ',
    10: 'dek',
    100: 'cent',
    1000: 'mil',
}

FRAGMENTS = [
    'mil', 'bil', 'tril', 'kvadril', 'kvintil',
    'sekstil', 'septil', 'oktil', 'nonil', 'dekil'
]

def _init():
    '''initialisations'''
    for i, fragment in enumerate(FRAGMENTS):
        exp = (i + 1) * 6
        NUMBERS[10**exp] = fragment + 'iono'
        exp += 3
        NUMBERS[10**exp] = fragment + 'iardo'

_init()

def spell(number, ordinal=False, max_decimals=10):
    '''spell out a number in Esperanto'''

    if number < 0:
        return 'minus ' + spell(-number)

    if ordinal:
        result = spell(number, ordinal=False)
        return result.replace(' ', '') + 'a'

    try:
        is_float = not number.is_integer()
    except AttributeError:
        is_float = False

    if is_float:
        integer, fraction = str(number).split('.')
        result = spell(int(integer)) + ' koma'
        for i, digit in enumerate(fraction[:max_decimals]):
            result += ' ' + NUMBERS[int(digit)]
            if all(d == '0' for d in fraction[i+1:max_decimals]):
                break
        return result

    result = NUMBERS.get(number)
    if result:
        return result

    for pos in (100, 1000):
        if number < pos:
            high, low = divmod(number, pos // 10)
            result = NUMBERS[pos // 10]
            if low:
                result += ' ' + spell(low)
            if high > 1:
                result = NUMBERS[high] + result
            return result

    exp = 3
    high, low = divmod(number, 1000)
    result = spell(low) if low else ''

    while high:
        high, low = divmod(high, 1000)
        if low:
            part = NUMBERS[10**exp]
            if low > 1:
                part = spell(low) + ' ' + part
                if part.endswith('o'):
                    part += 'j'
            result = part + ' ' + result if result else part
        exp += 3

    return result

def main():
    '''main function for testing'''

    for arg in sys.argv[1:]:
        if '.' in arg:
            number_f = float(arg)
            print('{:13f} {}'.format(number_f, spell(number_f)))
        else:
            number_i = int(arg)
            print('{:13d} {}'.format(number_i, spell(number_i)))

if __name__ == '__main__':
    main()
