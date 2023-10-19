import time
from general import gen_phi, ler_arquivo, ler_data_set
from hungarian_n3 import hungarian_n3


def test_hungarian_n3():
    data_set = ler_data_set()
    with open('output.txt', 'w') as f:
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


test_hungarian_n3()
