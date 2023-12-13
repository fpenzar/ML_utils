import math
import numpy as np

def AdaBoost(y_true, y_hat):
    # change w if needed
    w = np.full(len(y_true), 1/len(y_true))

    diff = np.array([0 if x == y else 1 for x, y in zip(y_true, y_hat)])
    # or add your own epsilon
    epsilon = w @ diff
    
    alpha = 0.5*np.log((1-epsilon)/epsilon)

    w_tilda_correct = np.array([math.exp(-alpha) * (w[i]) * (1 - diff[i]) for i in range(len(w))])
    w_tilda_incorrect = np.array([math.exp(alpha) * (w[i]) * diff[i] for i in range(len(w))])

    w_tilda = w_tilda_correct + w_tilda_incorrect

    w_next = w_tilda / np.sum(w_tilda)

    print(f"Updated weights:")
    print(w_next)


if __name__ == "__main__":
    y_true = np.array([2, 1, 1, 1, 2, 2, 2])
    y_hat = np.array([2, 1, 2, 1, 2, 2, 2])

    AdaBoost(y_true, y_hat)