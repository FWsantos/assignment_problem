def qap_linearized(A, B, C):
    n = A.shape[0]
    D = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            soma = 0
            for k in range(n):
                for l in range(n):
                    soma += A[i, k] * B[j, l]:
            D[i, j] = soma + C[i, j]

    return D
