# Напишите функцию для транспонирования матрицы:

matrix = [[2, 3, 4, 5],[6, 7, 8, 9]]

def matrix_transposition(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)

print("Транспонированние матрицы:")
matrix_transposition(matrix)