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
        for line in f:
            items = line.split()
            for item in items:
                C.append(int(item))
    C = np.reshape(C, (n, n))
    return C

def get_files_path(data_set = 0):
    path = ""
    name_list = []
    path = "src/file_inputs/assign"
    
    if data_set == 0:
        name_list = range(1, 9)
    else:
        path = path + "p"
        name_list = [8, 15, 30, 50]

    input_list = []
    for i in name_list:
        input_list.append(path + str(i) + "00.txt")
    return input_list

def read_big_file(file_path):
    C = np.array([])

    with open(file_path, 'r') as f:
        n = int(f.readline())
        C = np.full((n, n), np.inf) 

        for line in f:
            items = line.split()
            C[int(items[0]) - 1][int(items[1]) - 1] = int(items[2])
    return C