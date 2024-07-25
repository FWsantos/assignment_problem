import numpy as np
from general import basic_preprocessing, gen_phi

def alternate(k, C, V, u, v, row, pred):
    SU = set()
    LV = set()
    SV = set()
    fail = False
    sink = -1
    i = k

    while fail == False and sink == -1:
        SU.add(i)
        for j in V.difference(LV):
            if C[i][j] - u[i] - v[j] == 0:
                LV.add(j)
                pred[j] = i

        LV_diff_SV = LV.difference(SV)
        if not LV_diff_SV:
            fail = True
        else:
            j = list(LV_diff_SV)[0]
            SV.add(j)
            if row[j] == -1:
                sink = j
            else:
                i = row[j]
    return sink, LV, SU, pred


def hungarian_n4(C):
    u, v, row = basic_preprocessing(C)

    phi = gen_phi(row)
    n = C[0].size
    U = set(range(n))
    V = set(range(n))
    U_ = set(i for i in row if i > -1)
    pred = np.full(n, -1)

    while len(U_) < n:
        k = list(U.difference(U_))[0]
        while k not in U_:
            sink, LV, SU, pred = alternate(k, C, V, u, v, row, pred)

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

    return row

C = np.array([
    [7, 9, 8, 9],
    [2, 8, 5, 7],
    [1, 6, 6, 9],
    [3, 6, 2, 2]
])

row = hungarian_n4(C)
# u, v, row = basic_preprocessing(C)
phi = gen_phi(row)

# print(x)
# print('u = ', u)
# print('v = ', v)
# print('row = ', row)
print('phi = ', phi)
n = C[0].size
result = sum(C[i][phi[i]] for i in range(n))
print('result = ', result)
