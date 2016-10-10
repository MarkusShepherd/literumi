# -*- coding: utf-8 -*-

'spells out numbers in binary'

from __future__ import absolute_import, division, print_function, unicode_literals

import sys

def spell(number):
    'spell out a number in Esperanto'

    if number < 0:
        return 'minus ' + spell(-number)

    if number == 0:
        return 'zero'

    parts = []

    while number:
        high, low = divmod(number, 2)
        parts.insert(0, 'one' if low else 'zero')
        number = high

    return ' '.join(parts)

def main():
    'main function for testing'

    for arg in sys.argv[1:]:
        if '.' in arg:
            number = float(arg)
            print('{:13f} {}'.format(number, spell(number)))
        else:
            number = int(arg)
            print('{:13d} {}'.format(number, spell(number)))

if __name__ == '__main__':
    main()
