import numpy as np
import typing
from collections import defaultdict


def kfold_split(num_objects: int,
                num_folds: int) -> list[tuple[np.ndarray, np.ndarray]]:
    """Split [0, 1, ..., num_objects - 1] into equal num_folds folds
       (last fold can be longer) and returns num_folds train-val
       pairs of indexes.

    Parameters:
    num_objects: number of objects in train set
    num_folds: number of folds for cross-validation split

    Returns:
    list of length num_folds, where i-th element of list
    contains tuple of 2 numpy arrays, he 1st numpy array
    contains all indexes without i-th fold while the 2nd
    one contains i-th fold
    """
    mas = np.arange(num_objects)
    ret = []
    count_del = num_objects // num_folds
    for i in range(num_folds - 1):
        ret.append((np.hstack([mas[: i * count_del], mas[(i + 1) * count_del:]]), mas[i * count_del: (i + 1) * count_del]))
    ret.append((mas[: (num_folds - 1) * count_del], mas[(num_folds - 1) * count_del:]))
    return ret


def knn_cv_score(X: np.ndarray, y: np.ndarray, parameters: dict[str, list],
                 score_function: callable,
                 folds: list[tuple[np.ndarray, np.ndarray]],
                 knn_class: object) -> dict[str, float]:
    """Takes train data, counts cross-validation score over
    grid of parameters (all possible parameters combinations)

    Parameters:
    X: train set
    y: train labels
    parameters: dict with keys from
        {n_neighbors, metrics, weights, normalizers}, values of type list,
        parameters['normalizers'] contains tuples (normalizer, normalizer_name)
        see parameters example in your jupyter notebook

    score_function: function with input (y_true, y_predict)
        which outputs score metric
    folds: output of kfold_split
    knn_class: class of knn model to fit

    Returns:
    dict: key - tuple of (normalizer_name, n_neighbors, metric, weight),
    value - mean score over all folds
    """
    ret = dict()
    for normalizer in parameters['normalizers']:
        for n_neighbor in parameters['n_neighbors']:
            for metrics in parameters["metrics"]:
                for weight in parameters["weights"]:
                    scores = np.array([])
                    for fold in folds:
                        x_train = X[fold[0]]
                        x_test = X[fold[1]]
                        if normalizer[0] is not None:
                            normalizer[0].fit(x_train)
                            x_train = normalizer[0].transform(x_train)
                            x_test = normalizer[0].transform(x_test)
                        y_train = y[fold[0]]
                        y_test = y[fold[1]]

                        ml = knn_class(metric=metrics, n_neighbors=n_neighbor, weights=weight)
                        ml.fit(x_train, y_train)
                        y_pred = ml.predict(x_test)
                        scores = np.append(scores, score_function(y_test, y_pred))
                    ret[(normalizer[1], n_neighbor, metrics, weight)] = scores.mean()
    return ret
