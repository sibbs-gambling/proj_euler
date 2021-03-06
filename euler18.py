# Euler Problem 18 #
import numpy as np

pyr = \
"""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

pyr_lst = [x.split(' ') for x in pyr.split('\n')]
pyr_lst = [[int(y) for y in x] for x in pyr_lst]
max_n = np.max([len(x) for x in pyr_lst])
pyr_arr = np.vstack([np.array(x + [0] * (max_n - len(x))) for x in pyr_lst])

# Function defs

def eval_cell(parent, child_l, child_r):
    return parent + max(child_l, child_r)

def find_max(pyr_arr):
    # Solutions so we can use dynamic programming
    sols = np.empty(pyr_arr.shape)
    sols.fill(np.nan)
    sols[sols.shape[0]-1, :] = pyr_arr[sols.shape[0]-1,:]

    # Loop over cells
    for jRow in range(sols.shape[0]-2, -1, -1):
        for jCol in range(0, jRow+1):
            sols[jRow, jCol] = eval_cell(pyr_arr[jRow, jCol],
                                         sols[jRow+1, jCol],
                                         sols[jRow+1, jCol+1])
    return sols[0,0]

print(find_max(pyr_arr))
