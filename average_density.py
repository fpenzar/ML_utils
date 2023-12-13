import numpy as np

def parse(file, n):
    data = np.loadtxt(file)
    matrix = data.reshape(n, n)
    return matrix

def find_nearest_neigbours(data, o_i, K):
    o_i_row = data[o_i - 1, :]
    o_i_neighbours = np.sort(o_i_row)[:K]
    neighbours_indexes = np.argpartition(o_i_row, K)

    return o_i_neighbours, (neighbours_indexes[:K] + 1)

def calculate_ard(data, o_i, K):
    nearest_neighbours, neighbours_indexes = find_nearest_neigbours(data, o_i, K)
    o_i_density = density(nearest_neighbours, K)
    print("o_" + str(o_i) +" density: " + str(o_i_density))
    nearest_neighbours_densities = 0

    for neigh in neighbours_indexes:
        neigh_neighbours = find_nearest_neigbours(data, neigh, K)[0]
        neigh_density = density(neigh_neighbours, K)
        print("o_" + str(neigh) +" density: " + str(neigh_density))
        nearest_neighbours_densities += neigh_density

    return o_i_density / ( 1/K * nearest_neighbours_densities )

def density(nearest_neighbours, K):
    return 1 / ((1/K) * sum(nearest_neighbours))

if __name__ == "__main__":
    # change these 4 params
    file = "data.txt"
    n = 11 # number of observations
    o_i = 5 # the 0 indexed index of the observation ard is being calculated for
    K = 3 # nearest neighbours parameter
    
    data = parse(file, n)
    data = np.where(data==0, np.inf, data)
    print(data)
    ard = calculate_ard(data, o_i, K)
    print("ard: ", ard)