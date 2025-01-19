import numpy as np


def topsis(data, weights, impacts):
    data = np.array(data)
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))

    weighted_data = norm_data * weights

    ideal_best = np.where(np.array(impacts) == '+', weighted_data.max(axis=0), weighted_data.min(axis=0))
    ideal_worst = np.where(np.array(impacts) == '+', weighted_data.min(axis=0), weighted_data.max(axis=0))

    distance_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    scores = distance_worst / (distance_best + distance_worst)

    return scores
