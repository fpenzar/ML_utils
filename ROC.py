import numpy as np


def TPR(TP, FN):
    return TP / (TP + FN)


def FPR(FP, TN):
    return FP / (TN + FP)


def ROC(x):
    for i in range(len(x) + 1):
        classified_as_zero = x[:i]
        classified_as_one = x[i:]
        
        TN = sum(1 for j in classified_as_zero if j==0)
        FN = sum(1 for j in classified_as_zero if j==1)

        TP = sum(1 for j in classified_as_one if j==1)
        FP = sum(1 for j in classified_as_one if j==0)

        tpr = TPR(TP, FN)
        fpr = FPR(FP, TN)

        print(f"(FPR, TPR): ({fpr}, {tpr})")


if __name__ == "__main__":
    x = [1, 0, 0, 1, 1, 0]

    ROC(x)