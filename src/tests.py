import time
import datetime
from general import gen_phi, ler_arquivo
from hungarian_n3 import hungarian_n3

def ler_data_set(data_set = 0):
    path = ""
    name_list = []
    if data_set == 0:
        path = "src/file_inputs/assign"
        name_list = range(1, 9)
    elif data_set == 1:
        path = "src/file_inputs/assignp"
        name_list = [8, 15, 30, 50] 
    input_list = []
    for i in name_list:
        input_list.append(path + str(i) + "00.txt")
    return input_list

def test_hungarian_n3(ds = 0):
    data_set = []
    if ds == 0:
        data_set = ler_data_set()
    elif ds == 1:
        data_set = ler_data_set(1)

    with open('output.txt', 'w') as f:
        date_now = datetime.datetime.now()
        date_now_formated = date_now.strftime('%Y-%m-%d %H:%M:%S')

        f.write(f'{date_now_formated}\n')
        for file in data_set:

            C = ler_arquivo(file)

            start_time = time.time()
            row = hungarian_n3(C)
            end_time = time.time()
            run_time = end_time - start_time

            phi = gen_phi(row)
            n = C[0].size
            result = sum(C[i][phi[i]] for i in range(n))

            # f.write(f'C = {C}\n')
            # f.write(f'row = {row}\n')
            # f.write(f'phi = {phi}\n')

            f.write(f'file = {file}\n')
            f.write(f'result = {result}\n')
            f.write(f'run_time = {run_time:.2f} seconds\n\n')


