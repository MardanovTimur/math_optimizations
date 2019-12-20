""" Static gradient descend
"""
import math
import numpy as np
import logging
import random

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

ALPHA = .1
BETTA = .1

S = 10

func = lambda x1, x2: x1 * x1 + 9 * x2 * x2 - 10 * x1 - 36 * x2 + 61

g = [
    lambda x1, x2: - x1 * x1 + 4 * x1 - 4 * x2 + 12 >= 0,
    lambda x1, x2: -3 * x1 * x1 + 7 * x2 + 23 >= 0,
    lambda x1, x2: x1 >= 0,
    lambda x1, x2: x2 >= 0,
]


def get_xsi():
    return np.array([random.uniform(0, 2) - 1., random.uniform(0, 2) - 1.])


def check_conditions(X_coord):
    return all(map(lambda f: f(*X_coord), g))


def minimize(coord):
    alpha = ALPHA
    betta = BETTA
    value = func(*coord)

    while alpha > 0.00000000001:
        xsis = [get_xsi() for _ in range(S)]

        X_coords = []
        X_xsis = []  # selected
        summ = np.array([0., 0.])
        for xsi in xsis:
            if check_conditions(coord + betta * xsi):
                X_coords.append(coord + betta * xsi)
                X_xsis.append(xsi)

                summ += xsi * (value - func(*list(coord + betta * xsi)))

        if len(X_coords) == 0:
            betta *= 0.3
            continue

        pk = summ / betta
        new_coord = coord + alpha * pk

        if not check_conditions(new_coord):
            alpha *= 0.2
            continue

        new_value = func(*new_coord)
        if new_value < value:
            print(value, coord)
            value = new_value
            coord = new_coord

    print('Minimum value is: ', value)
    print('Coords is: ', coord)


if __name__ == '__main__':
    minimize(np.array([2., 2.]))
