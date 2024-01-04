import numpy as np

def basic_preprocessing(C):
    n = C[0].size
    x = np.zeros((n, n), dtype=np.int16)
    u = C.min(axis=1)
    v = (C-u[:, np.newaxis]).min(axis=0)
    row = np.full(n, -1)

    for i in range(n):
        for j in range(n):
            if (row[j] == -1) and (C[i][j] - u[i] - v[j] == 0):
                x[i][j] = 1
                row[j] = i
                break

    return u, v, row

def gen_phi(row):
    phi = np.full(row.size, -1)
    for j in range(row.size):
        if row[j] != -1:
            phi[row[j]] = j
    return phi

def read_file(file_path):
    C = []
    with open(file_path, 'r') as f:
        n = int(f.readline())
        for linha in f:
            elementos = linha.split()
            for elemento in elementos:
                C.append(int(elemento))
    C = np.reshape(C, (n, n))
    return C

