import numpy as np

# change S
S = np.array([43.4, 23.39, 18.26, 9.34, 2.14])


S_squared = np.power(S, 2)
total_var = np.sum(S_squared)
n = len(S_squared)

print("#############################################################################################")
for i in range(n):
    print(f"{i+1} component explains: {S_squared[i] / total_var * 100}% of variation")
    print(f"First {i+1} components explain: {np.sum(S_squared[:i+1]) / total_var * 100}% of variation")
    print(f"Last {n - i} components explain: {np.sum(S_squared[i:]) / total_var * 100}% of variation")
    print("#############################################################################################")