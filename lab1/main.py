
"""
2. Минимизировать функцию  на отрезке [0,1;3 ].
    f(x) = x*lnx + (x^2)/4

"""
import math
import logging

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

EPS = 0.001


def minimize(func, r):
    """ r - range
    """
    min_of_function = func(r[0])
    min_of_x = r[0]

    n = int((r[-1] - r[0]) / EPS)
    logger.info(f'Count of steps {n}, eps is {EPS}')

    for i in range(n):
        xi = r[0] + i * (r[-1] - r[0]) / n
        yi = func(xi)
        min_of_function = yi if yi < min_of_function else min_of_function
    return min_of_function


if __name__ == '__main__':
    function = lambda x: x * math.log(x) + math.pow(x, 2) / 4

    r = [0.1, 3.]
    minimum = minimize(function, r)
    print('Min value of function: ', minimum)
