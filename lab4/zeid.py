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

eps = 0.1


def minimize(func, coord):
    shape = np.array(coord).shape
    value = func(*coord)

    alpha = ALPHA
    k = 0

    while (True):
        Sdiag = np.diag(np.full(shape, 1))
        j = k - len(coord) * round(k / float(len(coord))) + 1

        alpha_a = 1.
        min_value = 10**10
        while alpha_a > -1.:
            matrix = coord + alpha_a * Sdiag[j - 1]
            if func(*matrix) < min_value:
                min_value = func(*matrix)
                alpha = alpha_a
            alpha_a -= 0.1

        prev_value = value
        prev_coord = coord

        coord = coord + alpha * Sdiag[j - 1]
        value = min_value

        if j < len(coord):
            k += 1
            continue
        elif abs(prev_value - value) < eps or \
                math.sqrt(math.pow((coord[0]-prev_coord[0]), 2) + math.pow((coord[1]-prev_coord[1]), 2)) < eps:
            break
        else:
            k += 1
            continue

    print('Mininum in :', value)
    print('Coords is :', coord)


if __name__ == '__main__':
    func = lambda x1, x2: 5 * x1 * x1 + 5 * x2 * x2 + 6* x1 * x2
    coord = [2., 4.]
    minimize(func, coord)
