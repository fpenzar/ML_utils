import numpy as np

def SMC(v1, v2):
    f00 = sum(1 for x, y in zip(v1, v2) if x == 0 and y == 0)
    f11 = sum(1 for x, y in zip(v1, v2) if x == 1 and y == 1)
    return (f00 + f11) / len(v1)


def J(v1, v2):
    f00 = sum(1 for x, y in zip(v1, v2) if x == 0 and y == 0)
    f11 = sum(1 for x, y in zip(v1, v2) if x == 1 and y == 1)
    return f11 / (len(v1) - f00)


def COS(v1, v2):
    v1_sum = sum(v1)
    v2_sum = sum(v2)

    v1t_y = sum(1 for x, y in zip(v1, v2) if x == 1 and y == 1)
    return v1t_y / np.sqrt(v1_sum * v2_sum)



if __name__ == "__main__":
    x = [1, 1, 0, 0, 0, 0]
    y = [1, 1, 1, 0, 0, 0]

    print(f"SMC: {SMC(x, y)}")
    print(f"Jaccard: {J(x, y)}")
    print(f"cos: {COS(x, y)} ")