import numpy as np
from scipy.optimize import minimize

# Exemplo de dados do QAP
distance_matrix = np.array([
    [0, 22, 53, 53],
    [22, 0, 40, 62],
    [53, 40, 0, 55],
    [53, 62, 55, 0]
])

flow_matrix = np.array([
    [0, 2, 9, 4],
    [2, 0, 6, 8],
    [9, 6, 0, 3],
    [4, 8, 3, 0]
])

# Função de custo para o QAP
def qap_cost(permutation):
    cost = 0
    for i in range(len(permutation)):
        for j in range(len(permutation)):
            cost += flow_matrix[i, j] * distance_matrix[int(permutation[i]), int(permutation[j])]
    return cost

# Inicializando com uma permutação aleatória
n = len(flow_matrix)
initial_permutation = np.arange(n)
np.random.shuffle(initial_permutation)

# Otimização utilizando métodos heurísticos
result = minimize(qap_cost, initial_permutation, method='nelder-mead', options={'xatol': 1e-8, 'disp': True})

# Resultados
optimal_permutation = np.argsort(result.x)
optimal_cost = qap_cost(optimal_permutation)

print(f'Permutação ótima: {optimal_permutation}')
print(f'Custo ótimo: {optimal_cost}')
