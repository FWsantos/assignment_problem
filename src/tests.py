import time
import datetime
import subprocess
import platform
from scipy.optimize import linprog
from general import gen_phi, read_file
from hungarian_n3 import hungarian_n3

def read_data_set():
    path = ""
    name_list = []
    path = "src/file_inputs/assign"
    name_list = range(1, 9)
    input_list = []
    for i in name_list:
        input_list.append(path + str(i) + "00.txt")
    return input_list


def test_hungarian_n3():
    data_set = []
    data_set = read_data_set()

    with open('output.txt', 'w') as f:
        date_now = datetime.datetime.now()
        date_now_formated = date_now.strftime('%Y-%m-%d %H:%M:%S')

        f.write(f'{date_now_formated}\n')
        for file in data_set:
            C = read_file(file)
            start_time = time.time()

            row = hungarian_n3(C)
            end_time = time.time()
            run_time = end_time - start_time
            phi = gen_phi(row)
            n = C[0].size
            result = sum(C[i][phi[i]] for i in range(n))

            f.write(f'file = {file}\n')
            f.write(f'result = {result}\n')
            f.write(f'run_time = {run_time:.2f} seconds\n\n')

def test(type_test):
    if type_test == 1:
        test_hungarian_n3()
    else:
        pass
    
    try:
        result = None
        if(platform.system() == 'Windows'):
            result = subprocess.check_output(['type', 'output.txt'], shell=True, universal_newlines=True)
        else:
            result = subprocess.check_output(['cat', 'output.txt'], universal_newlines=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print("Error while executing the 'type' command: {e}")
# def test_with_linprog():
    # import numpy as np
