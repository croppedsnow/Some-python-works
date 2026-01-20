from typing import List
from copy import deepcopy

import numpy as np
import pickle

def get_part_of_array(X: List[List[float]]) -> List[List[float]]:
    return [[X[y][x] for x in range(120, 500, 5)] for y in range(0, len(X), 4)]




def sum_non_neg_diag(X: List[List[int]]) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    sm = 0
    fl = 0
    for i in range(0, min(len(X[0]), len(X))):
        if X[i][i] >= 0:
            fl = 1
            sm += X[i][i]
    return sm if fl else -1


def replace_values(X: List[List[float]]) -> List[List[float]]:
    """
    X - двумерный массив вещественных чисел размера n x m.
    По каждому столбцу нужно почитать среднее значение M.
    В каждом столбце отдельно заменить: значения, которые < 0.25M или > 1.5M на -1
    Вернуть: двумерный массив, копию от X, с измененными значениями по правилу выше
    """
    y = deepcopy(X)
    m = [sum([y[j][i] for j in range(0, len(y))]) / len(y) for i in range(0, len(y[0]))]
    for i in range(0, len(y[0])):
        for j in range(0, len(y)):
            if y[j][i] > 1.5 * m[i] or y[j][i] < 0.25 * m[i]:
                y[j][i] = -1
    return y







