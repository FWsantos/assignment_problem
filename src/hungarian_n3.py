import numpy as np
from general import basic_preprocessing, gen_phi

def augment(k, C, V, u, v, row, pred):
    """
    Perform the augment phase of the Hungarian algorithm.
    
    Parameters:
    k (int): Current node in U.
    C (ndarray): Cost matrix.
    V (set): Set of nodes in V.
    u (ndarray): Potential u for nodes in U.
    v (ndarray): Potential v for nodes in V.
    row (ndarray): Row assignments.
    pred (ndarray): Predecessor array.
    
    Returns:
    tuple: (sink, LV, SU, pred)
        - sink (int): The sink node found.
        - LV (set): Set of labeled nodes in V.
        - SU (set): Set of labeled nodes in U.
        - pred (ndarray): Updated predecessor array.
    """
    n = len(V)
    pi = np.full(n, np.inf)
    SU = set()
    LV = set()
    SV = set()
    sink = -1
    i = k

    while sink == -1:
        SU.add(i)
        for j in V.difference(LV):
            reduced_cost = C[i][j] - u[i] - v[j]
            if reduced_cost < pi[j]:
                pred[j] = i
                pi[j] = reduced_cost
                if reduced_cost == 0:
                    LV.add(j)

        if not LV.difference(SV):
            # Calculate delta and update potentials in one go
            delta = np.min(pi[list(V.difference(LV))])
            u[list(SU)] += delta
            v[list(LV)] -= delta
            pi[list(V.difference(LV))] -= delta
            LV.update({j for j in V.difference(LV) if pi[j] == 0})

        j = next(iter(LV.difference(SV)))
        SV.add(j)
        if row[j] == -1:
            sink = j
        else:
            i = row[j]
    return sink, LV, SU, pred

def hungarian_n3(C):
    """
    Implement the Hungarian algorithm to solve the assignment problem in O(n^3) time.
    
    Parameters:
    C (ndarray): Cost matrix.
    
    Returns:
    ndarray: Row assignments.
    """
    u, v, row = basic_preprocessing(C)
    phi = gen_phi(row)
    n = C.shape[1]
    U = set(range(n))
    V = set(range(n))
    U_ = {i for i in row if i > -1}
    pred = np.full(n, -1)

    while len(U_) < n:
        k = next(iter(U.difference(U_)))
        sink, LV, SU, pred = augment(k, C, V, u, v, row, pred)
        U_.add(k)
        j = sink
        while True:
            i = pred[j]
            row[j] = i
            tmp = phi[i]
            phi[i] = j
            j = tmp
            if i == k:
                break
    return row

# Example usage
# C = np.array([
#     [7, 9, 8, 9],
#     [2, 8, 5, 7],
#     [1, 6, 6, 9],
#     [3, 6, 2, 2]
# ])

# row = hungarian_n3(C)
# phi = gen_phi(row)

# n = C.shape[1]
# result = sum(C[i][phi[i]] for i in range(n))
# print('phi =', phi)
# print('result =', result)
