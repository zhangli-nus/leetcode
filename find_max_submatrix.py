#coding: utf-8
import numpy as np

#submatrix

def find_max(input):
    h, w = input.shape
    matrix_cumsum = np.zeros((h,w))
    matrix_cumsum[0, :] = np.cumsum(input[0, :])
    matrix_cumsum[:,0] = np.cumsum(input[:, 0])
    for idy in range(1, h):
        for idx in range(1, w):
            matrix_cumsum[idy, idx] = matrix_cumsum[idy-1, idx]+matrix_cumsum[idy, idx-1]-matrix_cumsum[idy-1, idx-1] + input[idy, idx]

    new_matrix_cumsum = np.zeros((h+1, w+1))
    new_matrix_cumsum[1:, 1:] = matrix_cumsum
    matrix_cumsum = new_matrix_cumsum
    print(matrix_cumsum)
    max_value = -1*np.inf
    res = []
    for i in range(1, h+1):
        for j in range(1, w+1):
            for t in range(i, h+1):
                for s in range(j, w+1):
                    value = matrix_cumsum[t, s]-matrix_cumsum[t,j-1]-matrix_cumsum[i-1, s]+matrix_cumsum[i-1,j-1]
                    if value>max_value:
                        max_value = value
                        res = [i-1,j-1,t-1,s-1]
    return res, max_value


if __name__ == '__main__':
    input = np.array([[1,2,3],[2,-3,-4],[3,-9,5]])
    res, max_value = find_max(input)
    print(res)
    print(max_value)
