def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_new = []
        for j in range(m):
            matrix_new.append(value)

        matrix.append(matrix_new)
        if value <= 0:
            matrix = []

    return matrix

result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
print(result_1)
print(result_2)
print(result_3)