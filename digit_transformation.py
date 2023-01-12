from fractions import Fraction
from typing import List, Any


def digit_formatting_complex(dct_user_id):
    digit_1, digit_2, operation = dct_user_id

    digit_1 = complex(digit_1)
    digit_2 = complex(digit_2)

    lst_value = [digit_1, digit_2, operation]
    return lst_value


def digit_formatting_rational(dct_user_id):
    digit_1, digit_2, operation = dct_user_id
    a = digit_1
    digit_1 = Fraction(int(a[0: a.index(
        '/')]), int(a[a.index('/') + 1:len(a)]))

    g = digit_2
    digit_2 = Fraction(int(g[0: g.index(
        '/')]), int(g[g.index('/') + 1:len(g)]))

    lst_value: list[Fraction | Any] = [digit_1, digit_2, operation]
    return lst_value
