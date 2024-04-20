import numpy as np
from scipy.optimize import linprog

# Exemplo de matriz de custos
C = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

n = C.shape[0]
c = C.flatten()
print(c)

# Restrições
A_eq = []
b_eq = []

# Cada linha deve somar 1
for i in range(n):
    row = [0] * n * n
    for j in range(n):
        row[i * n + j] = 1
    A_eq.append(row)
    b_eq.append(1)

# Cada coluna deve somar 1
for j in range(n):
    col = [0] * n * n
    for i in range(n):
        col[i * n + j] = 1
    A_eq.append(col)
    b_eq.append(1)

# Resolve o problema
res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[(0, 1)] * n * n, method='highs')

print(res)
