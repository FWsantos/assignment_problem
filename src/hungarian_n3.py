import numpy as np
from general import basic_preprocessing, gen_phi, ler_arquivo

def augment(k, C, V, u, v, row, pred):
    pi = np.full(len(V), np.inf)
    SU = set()
    LV = set()
    SV = set()
    sink = -1
    i = k

    while sink == -1:
        SU.add(i)
        for j in V.difference(LV):
            if C[i][j] - u[i] - v[j] < pi[j]:
                pred[j] = i
                pi[j] = C[i][j] - u[i] - v[j]
                if pi[j] == 0:
                    LV.add(j)

        if not LV.difference(SV):
            delta = np.min(pi[list(V.difference(LV))])
            for i in SU:
                u[i] += delta
            for j in LV:
                v[j] -= delta
            for j in V.difference(LV):
                pi[j] -= delta
                if pi[j] == 0:
                    LV.add(j)
        j = list(LV.difference(SV))[0]
        SV.add(j)
        if row[j] == -1:
            sink = j
        else:
            i = row[j]
    return sink, LV, SU, pred


def hungarian_n3(C):
    u, v, row = basic_preprocessing(C)

    phi = gen_phi(row)
    n = C[0].size
    U = set(range(n))
    V = set(range(n))
    U_ = set(i for i in row if i > -1)
    pred = np.full(n, -1)

    while len(U_) < n:
        k = list(U.difference(U_))[0]
        sink, LV, SU, pred = augment(k, C, V, u, v, row, pred)
        U_.add(k)
        j = sink
        while True:
            i = pred[j]
            row[j] = i
            tmp = phi[i]
            phi[i] = j
            j = tmp
            if (i == k):
                break
    return row

