"""
Метод градиентного спуска
"""
import math
import numpy as np
import logging

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)


EPS = 0.1
ALPHA = 1.5
LAMBDA = 0.8


func = lambda x1, x2: 9 * x1 * x1 + x2 * x2 - 36 * x1 - 2 * x2 + 37

der_functions = [
    lambda x1, x2: 18 * x1 - 36,
    lambda x1, x2: 2 * x2 - 2
]
coord = [2., 0.]


def minimize(coord):
    condition = True
    value = func(*coord)
    alpha = ALPHA
    while condition:
        derivation = np.array(list(map(lambda func: func(*coord), der_functions)))
        derivation_len = math.sqrt(math.pow(derivation[0], 2) +
                                   math.pow(derivation[1], 2))
        if derivation_len <= EPS:
            condition = False

        X_coord = coord - alpha * derivation
        Y = func(*X_coord)
        if Y < value:
            coord = X_coord
            value = Y
        else:
            alpha *= LAMBDA

    print('Minimum of function: ', value)
    print('Coords (min): ', coord)


if __name__ == '__main__':
    minimize(np.array(coord))
