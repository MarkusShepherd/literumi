# -*- coding: utf-8 -*-

'''spells out numbers in binary'''

from __future__ import absolute_import, division, print_function, unicode_literals

import sys

def spell(number):
    '''spell out a number in binary'''

    if number < 0:
        return 'minus ' + spell(-number)

    if number == 0:
        return 'zero'

    parts = []

    while number:
        high, low = divmod(number, 2)
        parts.append('one' if low else 'zero')
        number = high

    return ' '.join(reversed(parts))

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
