import numpy as np



def parse(file, n):
    data = np.loadtxt(file)
    matrix = data.reshape(n, n)
    return matrix


def maximum_linkage(data, partition_1, partition_2):
    max_distance = 0
    for x in partition_1:
        i = x - 1
        for y in partition_2:
            j = y - 1
            if data[i, j] > max_distance:
                max_distance = data[i, j]
    return max_distance


def minimum_linkage(data, partition_1, partition_2):
    min_distance = np.inf
    for x in partition_1:
        i = x - 1
        for y in partition_2:
            j = y - 1
            if data[i, j] < min_distance:
                min_distance = data[i, j]
    return min_distance


def average_linkage(data, partition_1, partition_2):
    total_sum = 0
    for x in partition_1:
        i = x - 1
        for y in partition_2:
            j = y - 1
            total_sum += data[i, j]
    return total_sum / (len(partition_1) * len(partition_2))


def make_linkage(data, n, link_function):
    partitions = [[i + 1] for i in range(n)]
    for iter in range(n-1):
        min_distance = np.inf
        part_1 = None
        part_2 = None
        for i in range(len(partitions)):
            for j in range(i + 1, len(partitions)):
                distance = link_function(data, partitions[i], partitions[j])
                if distance >= min_distance:
                    continue
                min_distance = distance
                part_1 = i
                part_2 = j
        print(f"Iteration {iter + 1}: {partitions[part_1]} <--> {partitions[part_2]} distance: {min_distance}")
        partitions[part_1].extend(partitions[part_2])
        partitions.pop(part_2)


if __name__ == "__main__":
    # change these 3 params
    file = "data.txt"
    n = 10
    linkage = maximum_linkage # maximum_linkage / minimum_linkage / average_linkage

    data = parse(file, n)
    data = np.where(data==0, np.inf, data)
    print(data)
    make_linkage(data, n, linkage)