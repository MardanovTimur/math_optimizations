"""
2. Минимизировать функцию  на отрезке [0,1;3 ]. Поразрядный поиск
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
    h = abs(r[1] - r[0]) / 4.
    direction = 1

    def revert(direction, h):
        return -direction, h / 4.

    x0 = r[0]
    y0 = func(x0)
    steps = 0
    while (h > EPS):
        steps += 1
        x1 = x0 + direction * h

        if not r[0] <= x1 <= r[1]:
            direction, h = revert(direction, h)
            continue

        y1 = func(x1)
        if y0 < y1:
            x0 = x1
            y0 = y1
            direction, h = revert(direction, h)
            continue
        x0 = x1
        y0 = y1

    logger.info(f'Count of steps: {steps}')
    return func(x0)


if __name__ == '__main__':
    function = lambda x: x * math.log(x) + math.pow(x, 2) / 4

    r = [0.1, 3.]
    minimum = minimize(function, r)
    logger.info(f'Min value of function: {minimum}')
