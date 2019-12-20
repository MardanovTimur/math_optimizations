import math
import numpy as np
import logging

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

T = 1.0
EPS = 0.0000000000001

GAMMA = 2.
ALPHA = 0.5
BETTA = 0.3

def swap(values, i, j):
    swap_value = values[i]
    values[i] = values[j]
    values[j] = swap_value

def calc_eps_iter(values):
    fx0 = values[0]

    eps_iter = 0
    for fx in values[1:]:
        eps_iter += math.pow((fx - fx0), 2)
    return eps_iter / float(len(values))

def find_center(coords):
    return np.mean(np.array(coords), axis=0)

def find_mirror(center, coord):
    return 2 * center - np.array(coord)


def find_xn2(coords):
    return np.sum(coords[:-1], axis=0) / float(len(coords) - 1)


def find_xn3(coords, xn2):
    return xn2 + ALPHA * (xn2 - coords[-1])


def find_xn4(coords, xn3, xn2):
    return xn2 + GAMMA * (xn3 - xn2)


def find_xn5(coords, xn2):
    return xn2 + BETTA * (coords[-1] - xn2)


def minimize(func, coords):
    eps_iter = 100
    while eps_iter > EPS:
        values = list(map(lambda x: func(x[0], x[1]), coords))
        for i in range(len(values) - 1):
            for j in range(i, len(values)):
                if values[i] > values[j]:
                    swap(values, i, j)
                    swap(coords, i, j)

        eps_iter = calc_eps_iter(values)

        xn2 = find_xn2(coords)
        xn3 = find_xn3(coords, xn2)

        if func(*xn3) < values[0]:
            # растяжение выполняем
            xn4 = find_xn4(coords, xn3, xn2)
            if func(*xn4) < values[0]:
                values[-1] = func(*xn4)
                coords[-1] = xn4
            else:
                # отражение
                values[-1] = func(*xn3)
                coords[-1] = xn3
        elif all(map(lambda value: func(*xn3) > value, values[:-1])):
            # сжатие
            xn5 = find_xn5(coords, xn2)
            values[-1] = func(*xn5)
            coords[-1] = xn5
        else:
            # редукция
            xc = find_center(coords[:-1])
            mirror = find_mirror(xc, coords[-1])
            if func(mirror[0], mirror[1]) < values[-1]:
                values[-1] = func(mirror[0], mirror[1])
                coords[-1] = mirror
            else:
                xc = find_center(list(coords[:-2]) + [coords[-1], ])
                mirror = find_mirror(xc, coords[-2])
                if func(mirror[0], mirror[1]) < values[-2]:
                    values[-2] = func(mirror[0], mirror[1])
                    coords[-2] = mirror
                else:
                    # step 6
                    x0 = coords[0]
                    coords = (np.array(coords[1:]) + np.array(x0)) / 2.
                    coords = [x0, ] + list(coords)
    print('Mininum in :', func(*coords[0]))
    print('Coords is :', coords[0])


if __name__ == '__main__':
    func = lambda x1, x2: 100 * math.pow((x2 - (x1 * x1)), 2) + math.pow((1 - x1), 2)
    coords = [
        [-1, 1],
        [-0.1, 1],
        [-1, 2],
    ]

    minimize(func, coords)
