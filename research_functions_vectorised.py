import numpy as np
import pickle


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    x = np.sort(x)
    y = np.sort(y)
    return bool(np.prod(x == y))

def max_prod_mod_3(x: np.ndarray) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    y = x
    y = y * np.hstack((y[1:], y[0]))
    if np.sum(x % 3 == 0) and x.shape[0] > 1:
        return np.max(y[x % 3 == 0])
    else:
        return -1



def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    Сложить каналы изображения с указанными весами.
    """
    ni = image * weights
    ni = np.sum(ni, axis = 2)
    return ni


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    if np.sum(x, axis = 0)[1] != np.sum(y, axis = 0)[1]:
        return -1
    nx = np.repeat(x[:, 0], x[:, 1])
    ny = np.repeat(y[:, 0], y[:, 1])
    return np.dot(nx, ny)


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y.
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    lx = np.sqrt(np.sum(np.pow(X, 2), axis = 1))
    ly = np.sqrt(np.sum(np.pow(Y, 2), axis = 1))
    o = X @ Y.T
    o = o * (o != 0) / (ly * lx[:, np.newaxis] + (o + (o == 0)) * ((ly == 0) + (lx == 0)[:, np.newaxis])) + (o == 0) * ((ly == 0) + (lx == 0)[:, np.newaxis])
    return o