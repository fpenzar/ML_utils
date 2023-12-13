import numpy as np

# IMPORTANT
# change np.log according to the question (np.log -> natural log, np.log2 -> log base 2, np.log10 -> log base 10)
def entropy(X):
    s = np.sum(X)
    x_tilda = X / s
    ent = - sum([p*np.log(p) for p in x_tilda.flatten() if p != 0])
    return ent


def MI(n, n_z, n_q):
    return entropy(n_z) + entropy(n_q) - entropy(n)


def NMI(n, n_z, n_q):
    return MI(n, n_z, n_q) / (np.sqrt(entropy(n_z) * entropy(n_q)))


# rand_index
def R(S, D, N):
    return 2*(S+D) / (N*(N-1))


def J(S, D, N):
    return S / (0.5*(N*(N-1)) - D)


def compare(Z, Q):
    z_classes = len(set(list(Z)))
    q_classes = len(set(list(Q)))
    N = len(Z)

    n = np.zeros((z_classes, q_classes))
    for i in range(N):
        z = Z[i] - 1
        q = Q[i] - 1
        n[z, q] += 1
    
    n_z = n.sum(axis=1)
    n_q = n.sum(axis=0)

    S = sum([n_km*(n_km -1)/2 for n_km in n.flatten()])
    D = (N*(N-1)/2) - sum([n_kz*(n_kz-1)/2 for n_kz in n_z.flatten()]) \
        - sum([n_qm*(n_qm-1)/2 for n_qm in n_q.flatten()]) + S
    
    print(f"S: {S}")
    print(f"D: {D}")
    print(f"Rand Index: {R(S, D, N)}")
    print(f"Jaccard similarity: {J(S, D, N)}")
    print(f"MI: {MI(n, n_z, n_q)}")
    print(f"NMI: {NMI(n, n_z, n_q)}")


if __name__ == "__main__":
    # IMPORTANT see notice in entropy function regarding log!!!!!!!!!!!!!!
    Z = np.array([1, 3, 1, 2, 1, 2, 1, 1, 1, 1])
    Q = np.array([1, 1, 1, 2, 2, 2, 2, 2, 3, 3])

    compare(Z, Q)