""" Алгоритм с возвратом при неудачном шаге
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
        X_coord = coord + alpha * get_xsi()

        if not check_conditions(X_coord):
            alpha *= BETTA
        else:
            new_value = func(*X_coord)
            if new_value < value:
                value = new_value
                coord = X_coord

    print('Minimum value is: ', value)
    print('Coords is: ', coord)


if __name__ == '__main__':
    minimize(np.array([2., 2.]))
