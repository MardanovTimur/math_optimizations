"""
Дихотомия
[-1; 0] отрезок
Минимизировать функцию f(x) = x^4 + x^2 + x + 1
"""
import math
import logging
from copy import copy

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

EPS = 0.01
DELTA = 1.9 * EPS

EPS_FUNC = lambda a, b: abs(a - b) / 2.


def get_xs(distances):
    result = sum(distances) / 2.
    return result - DELTA / 2., result + DELTA / 2.


def minimize(func, r):
    a_b_distances = copy(r)
    while EPS_FUNC(*a_b_distances) > EPS:
        x_distances = get_xs(a_b_distances)
        y = list(map(func, x_distances))
        if y[0] < y[1]:
            a_b_distances = [a_b_distances[0], x_distances[1]]
        else:
            a_b_distances = [x_distances[0], a_b_distances[1]]
    return func(sum(a_b_distances) / 2.)


if __name__ == '__main__':
    function = lambda x: math.pow(x, 4) + math.pow(x, 2) + x + 1

    r = [-1., 0.]
    minimum = minimize(function, r)
    logger.info(f'Min value of function: {minimum}')
