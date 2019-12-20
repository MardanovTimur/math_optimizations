"""
Gold slice
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
TAU = (math.sqrt(5) - 1) / 2.

def get_xs(d):
    x0 = d[0] + (1 - TAU) * (d[1] - d[0])
    x1 = d[0] + TAU * (d[1] - d[0])
    return [x0, x1]

def minimize(func, r):
    a_b_distances = copy(r)
    x_distances = get_xs(a_b_distances)
    y = list(map(func, x_distances))
    eps_func = (a_b_distances[1] - a_b_distances[0]) / 2.
    while eps_func > EPS:
        if y[0] < y[1]:
            a_b_distances[1] = x_distances[1]
            x_distances[1] = x_distances[0]
            x_distances[0] = sum(a_b_distances) - x_distances[1]
            y[1] = y[0]
            y[0] = func(x_distances[0])
        else:
            a_b_distances[0] = x_distances[0]
            x_distances[0] = x_distances[1]
            x_distances[1] = sum(a_b_distances) - x_distances[0]
            y[0] = y[1]
            y[1] = func(x_distances[1])
        eps_func *= TAU
    return func(sum(a_b_distances) / 2.)


if __name__ == '__main__':
    function = lambda x: math.pow(x, 4) + math.pow(x, 2) + x + 1

    r = [-1., 0.]
    minimum = minimize(function, r)
    logger.info(f'Min value of function: {minimum}')
