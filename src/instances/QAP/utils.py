import numpy as np

def read_qapdata(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Obtenha o valor de n
        n = int(lines[0].strip())
        
        # Remover linhas vazias e espaços em branco
        matrix_lines = [line.strip() for line in lines if line.strip()]
        
        # Ignorar a primeira linha que contém o valor de n
        matrix_lines = matrix_lines[1:]
        
        # Separar as linhas das matrizes A e B
        half = len(matrix_lines) // 2
        A_lines = matrix_lines[:half]
        B_lines = matrix_lines[half:]
        
        # Criar as matrizes A e B
        A = np.array([list(map(int, line.split())) for line in A_lines])
        B = np.array([list(map(int, line.split())) for line in B_lines])
        
        # Verificar se a matriz C faz sentido
        if A.shape != B.shape or A.shape != (n, n):
            raise ValueError("As dimensões das matrizes A e B não coincidem ou não são quadradas de ordem n.")
        
        return A, B, None  # Retorna None para C já que não está presente nos arquivos

# # Exemplo de uso:
# file_path = 'src/instances/QAP/qapdata/chr12a.dat'
# A, B, C = read_qapdata(file_path)
# print(A)
# print(B)
# print(C)
