import numpy as np
import numbers


def norm_1(coords, offset):
    value = coords - offset
    return np.sum(np.abs(value))


def norm_2(coords, offset):
    value = coords - offset
    return np.sqrt(np.sum(np.power(value, 2)))


def norm_inf(coords, offset):
    value = coords - offset
    return np.max(np.abs(value))


def propagate(tree, coords):
    parent = -0.5
    condition = True
    for i in range(len(tree)):
        layer = tree[i]
        if condition:
            # go right
            node = layer[int(2*parent + 1)]
            parent = int(2*parent + 1)
        else:
            # go left
            node = layer[int(2*parent + 0)]
            parent = int(2*parent + 0)
        
        if isinstance(node, numbers.Number):
            return node
        
        offset = node[0]
        func = node[1]
        relational_operator = node[2]
        threshold = node[3]

        value = func(coords, offset)
        if relational_operator == "<":
            if value < threshold:
                condition = True
            else:
                condition = False
        elif relational_operator == ">":
            if value > threshold:
                condition = True
            else:
                condition = False
        else:
            print("Unrecognized relational operator!")
            exit(1)


def is_setup_possible(tree, data):
    for class_index in data:
        for coords in data[class_index]:
            obtained_class_index = propagate(tree, coords)
            if class_index != obtained_class_index:
                print("FALSE")
                print("This setup is NOT POSSIBLE for given coords")
                return
    
    print("TRUE")
    print("This setup is POSSIBLE for given coords")


if __name__ == "__main__":
    # A = (offset, function, relational_operator, threshold_value)
    A = (np.array([2, 4]), norm_1, "<", 3)
    C = (np.array([6, 4]), norm_1, "<", 3)
    B = (np.array([4, 2]), norm_1, "<", 3)

    # data - sample some datapoints from multiple areas of the graph (cover all classes)
    # {class_index: [coordinates read from the graph]}
    data = {1: np.array([[1, 1], [2, 4], [3, 4.5]]),
            2: np.array([[4, 4], [4.5, 4], [4, 4.5]]),
            3: np.array([[3, 2], [4, 0], [5, 1], [3, 2.5], [4, 2]])}
    
    # tree goes by levels (the left branch is always False, right is always True)
    #           A
    #      F   / \   T
    #         /    \
    #       B       C
    #   F  / \ T  F / \  T
    #     1   3    1   2     :   CLASS
    tree = [[A], [B, C], [1, 3, 1, 2]]



    is_setup_possible(tree, data)