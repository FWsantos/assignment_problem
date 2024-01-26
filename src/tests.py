import time
import datetime
import subprocess
import platform
import numpy as np
from scipy.optimize import linprog
from general import gen_phi, read_file, read_big_file, get_files_path
from hungarian_n3 import hungarian_n3

def test_hungarian_n3(output_file_name, type_test = 0):
    
    data_set = get_files_path(type_test)
   
    with open(output_file_name, 'w') as f:
        date_now = datetime.datetime.now()
        date_now_formated = date_now.strftime('%Y-%m-%d %H:%M:%S')

        f.write(f'{date_now_formated}\n')
        print("data_set = ", data_set, "\n")
        for file in data_set:
            C = np.array([])
            
            if type_test == 0:
                C = read_file(file)
            else:
                C = read_big_file(file)
                
            start_time = time.time()

            row = hungarian_n3(C)
            end_time = time.time()
            run_time = end_time - start_time
            phi = gen_phi(row)
            n = C[0].size
            result = sum(C[i][phi[i]] for i in range(n))

            print(f'file = {file}')
            print(f'result = {result}')
            print(f'run_time = {run_time:.2f} seconds\n')

            f.write(f'file = {file}\n')
            f.write(f'result = {result}\n')
            f.write(f'run_time = {run_time:.2f} seconds\n\n')

def test(type_test = 0):
    output_file_name = ""

    if type_test == 0:
        output_file_name = 'output.txt'
    else:
        output_file_name = 'output_big.txt'

    test_hungarian_n3(output_file_name, type_test)

    try:
        result = None
        if(platform.system() == 'Windows'):
            result = subprocess.check_output(['type', output_file_name], shell=True, universal_newlines=True)
        else:
            result = subprocess.check_output(['cat', output_file_name], universal_newlines=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print("Error while executing the 'type' command: {e}")

