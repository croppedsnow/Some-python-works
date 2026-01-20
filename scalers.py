import numpy as np
import typing


class MinMaxScaler:
    def __init__(self):
        self.__min = np.array([])
        self.__max = np.array([])

    def fit(self, data: np.ndarray) -> None:
        """Store calculated statistics

        Parameters:
        data: train set, size (num_obj, num_features)
        """
        self.__max = np.max(data, axis=0)
        self.__min = np.min(data, axis=0)

    def transform(self, data: np.ndarray) -> np.ndarray:
        """
        Parameters:
        data: train set, size (num_obj, num_features)

        Return:
        scaled data, size (num_obj, num_features)
        """
        return (data - self.__min) / (self.__max - self.__min)


class StandardScaler:
    def __init__(self):
        self.__mat = np.array([])
        self.__dis = np.array([])

    def fit(self, data: np.ndarray) -> None:
        self.__mat = np.mean(data, axis=0)
        self.__dis = np.std(data, axis=0)

    def transform(self, data: np.ndarray) -> np.ndarray:
        return (data - self.__mat) / self.__dis
