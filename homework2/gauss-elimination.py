import numpy as np
from math import *


def bigger_power_of_two(n):
    m = ceil(log(n, 2))
    return 2 ** int(m)


def read_one_matrix(file_handle):
    first_matrix_size = file_handle.readline().strip().split(' ')
    n = int(first_matrix_size[0])
    m = int(first_matrix_size[1])

    A = [[0 for i in range(n)] for j in range(m)]

    for i in range(n):
        line = file_handle.readline().strip().split(' ')
        for j in range(n):
            A[i][j] = int(line[j])

    return A, n


def read_matrix(filename):
    file = open(filename)

    A, nA = read_one_matrix(file)
    B, nB = read_one_matrix(file)

    return (A, nA), (B, nB)


def switch_lines(A, B, n, row_index1, row_index2):
    for j in range(0, n):
        aux = A[row_index1][j]
        A[row_index1][j] = A[row_index2][j]
        A[row_index2][j] = aux

    aux = B[row_index1][0]
    B[row_index1][0] = B[row_index2][0]
    B[row_index2][0] = aux

    return A, B


def find_max_pivot(column, A, n):
    pivot = abs(A[column][0])
    max_pivot_row = 0
    for i in range(1, n):
        if abs(A[column][i]) > pivot:
            pivot = abs(A[column][i])
            max_pivot_row = i
    return pivot, max_pivot_row


def substract_matrix_lines(A, n, row1, row2):
    for j in range(0, n):
        A[row1][j] -= A[row2][j]
    return A


