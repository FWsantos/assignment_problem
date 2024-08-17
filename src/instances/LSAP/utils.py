import numpy as np

def read_file(file_path):
    C = np.array([])
    with open(file_path, 'r') as f:
        n = int(f.readline())
        for line in f:
            items = line.split()
            for item in items:
                C = np.append(C, int(item))
    C = np.reshape(C, (n, n))
    return C

def get_files_path(data_set = 0):
    path = ""
    name_list = []
    path = "src/instances/LSAP/input/assign"
    
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
