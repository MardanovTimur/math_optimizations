""" Simplex method
"""
import math
import numpy as np
import logging
import random

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

origin_coef = [2, 1, -1, 1, -1]
cond_coefs = [
    [[1, 1, 1, 0, 0], 5],
    [[2, 1, 0, 1, 0], 9],
    [[1, 2, 0, 0, 1], 7],
]

cond_x_coefs = np.array([
    [1, 1, 1, 0, 0],
    [2, 1, 0, 1, 0],
    [1, 2, 0, 0, 1],
])
#  def minimize():


if __name__ == '__main__':
    #  minimize()
    matrix = np.array(cond_coefs)
    print(cond_x_coefs.shape)
