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
        # print('i = ', i)
        SU.add(i)
        # print('pred = ', pred)
        for j in V.difference(LV):
            if C[i][j] - u[i] - v[j] < pi[j]:
                pred[j] = i
                pi[j] = C[i][j] - u[i] - v[j]
                if pi[j] == 0:
                    LV.add(j)
                # print('j = ', j)
                # print('i = ', i)
                # print('pred = ', pred)

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
    #     print('SU = ', SU)
    #     print('pred = ', pred)
    #     print('LV = ', LV)
    #     print('i = ', i)
    #     print('j = ', j)
    #     print('SV = ', SV)
    # print('sink = ', sink)
    return sink, LV, SU, pred


def hungarian_n3(C):
    u, v, row = basic_preprocessing(C)
    # print('u = ', u)
    # print('v = ', v)
    # print('row = ', row)

    phi = gen_phi(row)
    # print('phi = ', phi)
    n = C[0].size
    # print('n = ', n)
    U = set(range(n))
    V = set(range(n))
    # print('U = ', U)
    # print('V = ', V)
    U_ = set(i for i in row if i > -1)
    # print('U_ = ', U_)
    pred = np.full(n, -1)
    # print('pred = ', pred)
    # print('phi = ', phi)
    # print('k = ', k)

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


# C = ler_arquivo(
#     "/home/wesley/dev/assignment_problem/src/file_inputs/assign500.txt")

# print(C)

# row = hungarian_n3(C)
# phi = gen_phi(row)

# # print(x)
# # print('u = ', u)
# # print('v = ', v)
# # print('row = ', row)
# # print('phi = ', phi)
# n = C[0].size
# result = sum(C[i][phi[i]] for i in range(n))
# print('result = ', result)
