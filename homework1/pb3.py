from math import *


def bigger_power_of_two(n):
    m = ceil(log(n, 2))
    return 2 ** int(m)


def read_one_matrix(file_handle):
    first_matrix_size = file_handle.readline().strip().split(' ')
    n = int(first_matrix_size[0])
    m = int(first_matrix_size[1])

    maxim = n
    if m > maxim:
        maxim = m

    maxim = bigger_power_of_two(maxim)

    A = [[0 for i in range(maxim)] for j in range(maxim)]

    for i in range(n):
        line = file_handle.readline().strip().split(' ')
        for j in range(m):
            A[i][j] = int(line[j])

    return A, n, m


def read_matrix(filename):
    file = open(filename)

    A, nA, mA = read_one_matrix(file)
    B, nB, mB = read_one_matrix(file)

    return (A, nA, mA), (B, nB, mB)


def simple_matrix_product(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def simple_matrix_add(A, B, n, substract=False):
    C = [[0 for j in range(0, n)] for i in range(0, n)]

    for i in range(0, n):
        for j in range(0, n):
            if not substract:
                C[i][j] = A[i][j] + B[i][j]
            else:
                C[i][j] = A[i][j] - B[i][j]

    return C


def get_null_matrix(n):
    return [[0 for j in range(n)] for i in range(n)]


def get_submatrixes(A, n):
    a_1_1 = get_null_matrix(n)
    a_1_2 = get_null_matrix(n)
    a_2_1 = get_null_matrix(n)
    a_2_2 = get_null_matrix(n)

    for i in range(n):
        for j in range(n):
            upper_j = j + n
            upper_i = i + n

            a_1_1[i][j] = A[i][j]
            a_1_2[i][j] = A[i][upper_j]
            a_2_1[i][j] = A[upper_i][j]
            a_2_2[i][j] = A[upper_i][upper_j]

    return a_1_1, a_1_2, a_2_1, a_2_2


def unite_matrix(c_1_1, c_1_2, c_2_1, c_2_2, n):
    C = [[0 for j in range(n * 2)] for i in range(n * 2)]

    for i in range(n):
        for j in range(n):
            upper_j = j + n
            upper_i = i + n

            C[i][j] = c_1_1[i][j]
            C[i][upper_j] = c_1_2[i][j]
            C[upper_i][j] = c_2_1[i][j]
            C[upper_i][upper_j] = c_2_2[i][j]

    return C


def strassen(A, B, n, n_min):
    if n <= n_min:
        return simple_matrix_product(A, B, n)

    n = n / 2

    a_1_1, a_1_2, a_2_1, a_2_2 = get_submatrixes(A, n)
    b_1_1, b_1_2, b_2_1, b_2_2 = get_submatrixes(B, n)

    p1 = simple_matrix_product(
        simple_matrix_add(a_1_1, a_2_2, n),
        simple_matrix_add(b_1_1, b_2_2, n), n)

    p2 = simple_matrix_product(
        simple_matrix_add(a_2_1, a_2_2, n),
        b_1_1, n)

    p3 = simple_matrix_product(
        a_1_1,
        simple_matrix_add(b_1_2, b_2_2, n, substract=True),
        n)

    p4 = simple_matrix_product(
        a_2_2,
        simple_matrix_add(b_2_1, b_1_1, n, substract=True),
        n)

    p5 = simple_matrix_product(
        simple_matrix_add(a_1_1, a_1_2, n),
        b_2_2, n)

    p6 = simple_matrix_product(
        simple_matrix_add(a_2_1, a_1_1, n, substract=True),
        simple_matrix_add(b_1_1, b_1_2, n),
        n)

    p7 = simple_matrix_product(
        simple_matrix_add(a_1_2, a_2_2, n, substract=True),
        simple_matrix_add(b_2_1, b_2_2, n),
        n)

    c_1_1 = simple_matrix_add(
        simple_matrix_add(p1, p4, n),
        simple_matrix_add(p7, p5, n, substract=True), n)

    c_1_2 = simple_matrix_add(p3, p5, n)
    c_2_1 = simple_matrix_add(p2, p4, n)

    c_2_2 = simple_matrix_add(
        simple_matrix_add(p1, p3, n),
        simple_matrix_add(p6, p2, n, substract=True), n)

    return unite_matrix(c_1_1, c_1_2, c_2_1, c_2_2, n)


def do_strassen(filename, minim):
    Adata, Bdata = read_matrix(filename)

    n = len(Adata[0])
    C = strassen(Adata[0], Bdata[0], n, minim)

    An = Adata[1]
    Bm = Bdata[2]

    for i in range(An):
        for j in range(Bm):
            print C[i][j],
        print ''


def main():
    do_strassen('matrici.data', 4)


if __name__ == '__main__':
    main()
