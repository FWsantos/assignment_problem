import numpy as np
from scipy.optimize import linear_sum_assignment

from general import read_file

C = read_file("src/file_inputs/assign200.txt")

row_ind, col_ind = linear_sum_assignment(C)

# print(col_ind)
# print(row_ind)
print(C[row_ind, col_ind].sum())
