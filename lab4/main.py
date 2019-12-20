"""
 Метод циклического покоординатного спуска
    f(x1, x2) = (x2 - x1^2) + (1 - x1)^2
"""
import math
import numpy as np
import logging

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

ALPHA = 0.5
LAMBDA = 0.5  # коеф увеличения альфа

eps = 0.001


def minimize(func, coord):
    shape = np.array(coord).shape
    value = func(*coord)

    alpha = ALPHA

    while (alpha > eps):
        Sdiag = np.diag(np.full(shape, 1))

        def iteration(coord, value, direction):
            for sdiag in Sdiag:
                step_coord = coord + direction * alpha * sdiag * coord
                step_value = func(*step_coord)
                if step_value < value:
                    return step_coord, step_value

        changed = False
        for direction in [1, -1]:
            values = iteration(coord, value, direction)
            if values:
                coord, value = values
                changed = True
                break

        if not changed:
            alpha *= LAMBDA
    print('Mininum in :', func(*coord))
    print('Coords is :', coord)


if __name__ == '__main__':
    func = lambda x1, x2: (x2 - x1 * x1) + math.pow((1 - x1), 2)
    coord = [-1., 0.]
    minimize(func, coord)
    func = lambda x1, x2: 5 * x1 * x1 + 5 * x2 * x2 + 6* x1 * x2
    coord = [2., 4.]
    minimize(func, coord)
