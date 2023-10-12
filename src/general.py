import numpy as np


def basic_preprocessing(C):
    # n recebe o tamanho da primeira linha da matriz C
    n = C[0].size

    # Inicializa x como uma matrix nxn de inteiros e preenchida por zeros
    x = np.zeros((n, n), dtype=np.int16)

    # captura o menor elemento de cada linha de C
    u = C.min(axis=1)
    print('u = ', u)

    # captura o menor elemento de cada coluna de C
    # 'u[:, np.newaxis]' é igual a 'np.array([u]).T'
    v = (C-u[:, np.newaxis]).min(axis=0)
    print('v = ', v)

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
