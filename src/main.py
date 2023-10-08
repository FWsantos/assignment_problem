import numpy as np


def basic_preprocessing(C):
    # n recebe o tamanho da primeira linha da matriz C
    n = C[0].size

    # Inicializa x como uma matrix nxn de inteiros e preenchida por zeros
    x = np.zeros((n, n), dtype=np.int16)

    # captura o menor elemento de cada linha de C
    u = C.min(axis=1)
    # print(u)

    # captura o menor elemento de cada coluna de C
    # 'u[:, np.newaxis]' é igual a 'np.array([u]).T'
    v = (C-u[:, np.newaxis]).min(axis=0)
    # print(v)

    # Inicializa o vetor row com -1
    row = np.full(n, -1)

    for i in range(n):
        for j in range(n):
            if (row[j] == -1) and (C[i][j] - u[i] - v[j] == 0):
                x[i][j] = 1
                row[j] = i
                break

    return u, v, row


def generate_phi(row):

    phi = np.full(row.size, -1)
    for j in range(row.size):
        if row[j] != -1:
            phi[row[j]] = j
    return phi


def alternate(k, C, V, u, v, row, pred):
    SU = set()
    LV = set()
    SV = set()
    fail = False
    sink = -1
    i = k

    while fail == False and sink == -1:
        # print('i = ', i)
        SU.add(i)
        for j in np.arange(len(V.difference(LV))):
            if C[i][j] - u[i] - v[j] == 0:
                LV.add(j)
                pred[j] = i

        LV_diff_SV = LV.difference(SV)
        if not LV_diff_SV:
            fail = True
            # print(fail)
        else:
            # print('LV = ', LV)
            # print('SV = ', SV)
            # print('LV-SV = ', LV-SV)
            j = list(LV_diff_SV)[0]
            SV.add(j)
            if row[j] == -1:
                sink = j
            else:
                i = row[j]
    #     print('SU = ', SU)
    #     print('pred = ', pred)
    #     print('LV = ', LV)
    #     print('j = ', j)
    #     print('SV = ', SV)
    # print('sink = ', sink)
    return sink, LV, SU, pred


# def menor_elemento_expressao(c, u, v, conjunto_i, conjunto_j):
#     sub_c = c[np.ix_(list(conjunto_i), list(conjunto_j))]
#     sub_u = u[list(conjunto_i)]
#     sub_v = v[list(conjunto_j)]
#     resultado = sub_c - sub_u[:, np.newaxis] - sub_v
#     return np.min(resultado)


def hungarian_n4(C):
    u, v, row = basic_preprocessing(C)
    # print('u = ', u)
    # print('v = ', v)
    # print('row = ', row)

    phi = generate_phi(row)
    # print('phi = ', phi)
    n = C[0].size
    # print('n = ', n)
    U = set(range(n))
    V = set(range(n))
    # print('U = ', U)
    # print('V = ', V)
    U_ = set(row)
    # print('U_ = ', U_)
    pred = np.full(n, -1)
    # print('pred = ', pred)
    # print('phi = ', phi)
    # k = next(iter(U.difference(U_)))
    k = list(U.difference(U_))[0]
    # print('k = ', k)

    while len(U_) < n:
        while k not in U_:
            sink, LV, SU, pred = alternate(k, C, V, u, v, row, pred)
            # print('sink = ', sink)
            # print('LV = ', LV)
            # print('SU = ', SU)
            # print('pred = ', pred)

            if sink > -1:
                U_.add(k)
                j = sink
                while True:
                    i = pred[j]
                    row[j] = i
                    h = phi[i]
                    phi[i] = j
                    j = h
                    if i == k:
                        break
            else:
                V_diff_LV = V - LV
                sub_C = C[np.ix_(list(SU), list(V_diff_LV))]
                sub_u = u[list(SU)]
                sub_v = v[list(V_diff_LV)]
                results = sub_C - sub_u[:, np.newaxis] - sub_v
                delta = np.min(results)

                u[list(SU)] += delta
                v[list(LV)] -= delta
            break
        break
    return row


C = np.array([
    [7, 9, 8, 9],
    [2, 8, 5, 7],
    [1, 6, 6, 9],
    [3, 6, 2, 2]
])

row = hungarian_n4(C)
# u, v, row = basic_preprocessing(C)
# phi = generate_phi(row)


# print(x)
# print('u = ', u)
# print('v = ', v)
# print('row = ', row)
# print('phi = ', phi)
