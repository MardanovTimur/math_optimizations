""" Наилучший алгоритм с возвратом при неудачном шаге
"""
import math
import numpy as np
import logging
import random

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

ALPHA = 1
BETTA = .2

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
    value = func(*coord)

    while alpha > 0.000000001:
        xsis = [get_xsi() for _ in range(S)]

        X_coords = [coord + alpha * xsi for xsi in xsis if check_conditions(coord + alpha * xsi)]
        for x_coord in X_coords:
            new_value = func(*x_coord)
            if new_value < value:
                value = new_value
                coord = x_coord

        if not X_coords:
            alpha *= BETTA

    print('Minimum value is: ', value)
    print('Coords is: ', coord)


if __name__ == '__main__':
    minimize(np.array([2., 2.]))
