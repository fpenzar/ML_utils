import numpy as np


def entropy(data):
    n = sum(data)
    probs = np.array([c/n for c in data if c != 0])
    logs = np.log2(probs)
    return -np.sum(probs*logs)


def class_error(data):
    n = sum(data)
    probs = np.array([c/n for c in data])
    max_prob = np.max(probs)
    return 1 - max_prob


def gini(data):
    n = sum(data)
    probs = np.array([c/n for c in data])
    probs_squared = np.power(probs, 2)
    return 1 - np.sum(probs_squared)


def regression(data):
    y = np.array(data)
    mu = np.mean(data)
    return (np.sum(np.power(y - mu, 2))) / len(y)



def purity_gain(data_before, data_after, impurity_func):
    I_r = impurity_func(data_before)
    purities = np.array([impurity_func(partition) for partition in data_after])

    if impurity_func == regression:
        n = len(data_before)
        weights = np.array([len(partition) / n for partition in data_after])
    else:
        n = sum(data_before)
        weights = np.array([sum(partition) / n for partition in data_after])

        
    weighted_purities = purities * weights

    p_gain = I_r - np.sum(weighted_purities)
    return p_gain



if __name__ == "__main__":
    # if regression: put the y values inside data_before and partitions
    # if anything else: put the count of class members inside the list (e.g. values are [c1, c1, c1, c2, c2, c3, c4, c4] -> [3, 2, 1, 2])
    impurity_func = regression
    data_before = [23, 6, 17, 14, 13]
    partition_1 = [23]
    partition_2 = [6, 17, 14, 13]
    data_after = [partition_1, partition_2]

    print(f"Purity gain (\delta): {purity_gain(data_before, data_after, impurity_func)}")