from collections import Counter
from typing import List

def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    if len(x) != len(y):
        return False
    x.sort()
    y.sort()
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
    return True

def max_prod_mod_3(x: List[int]) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    fl = False
    mx = -1
    for i in range(len(x) - 1):
        if (x[i] % 3 == 0 or x[i + 1] % 3 == 0) and (not fl or x[i] * x[i + 1] > mx):
            mx = x[i] * x[i + 1]
            fl = True
    return mx



def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    """
    Сложить каналы изображения с указанными весами.
    """
    lst = []
    for i in range(len(image)):
        lst.append([])
        for j in range(len(image[0])):
            lst[i].append(sum([image[i][j][k] * weights[k] for k in range(len(image[0][0]))]))
    return lst


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    lst1 = []
    lst2 = []
    for i in range(len(x)):
        lst1 += [x[i][0]] * x[i][1]

    for i in range(len(y)):
        lst2 += [y[i][0]] * y[i][1]

    if len(lst1) != len(lst2):
        return -1

    sc = 0
    for i in range(len(lst1)):
        sc += lst1[i] * lst2[i]

    return sc


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y. 
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    lst = []
    for i in range(len(X)):
        lst.append([1] * len(Y))

    for i in range(len(X)):
        for j in range(len(Y)):
            sc = sum([X[i][k] * Y[j][k] for k in range(len(X[0]))])
            lenx = sum([X[i][k] ** 2 for k in range(len(X[0]))]) ** 0.5
            leny = sum([Y[j][k] ** 2 for k in range(len(X[0]))]) ** 0.5

            if lenx and leny:
                lst[i][j] = sc / (lenx * leny)

    return lst