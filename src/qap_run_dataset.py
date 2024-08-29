import numpy as np
from instances.QAP.utils import read_qapdata
from lib.QAP.QAP import qap_linearized
from lib.LSAP.hungarian_n3 import hungarian_n3, gen_phi

file_path = 'src/instances/QAP/qapdata/chr12b.dat'
A, B, C = read_qapdata(file_path)

D = qap_linearized(A, B, C)
# print(D)

row = hungarian_n3(D)
phi = gen_phi(row)

n = D.shape[1]
result = sum(D[i][phi[i]] for i in range(n))
print('phi =', phi)
print('result =', result)
