def matriz(mat):
    M_t = list(map(list, zip(*mat)))
    return M_t

matriz1 = [[1,1,1], [2,4,6], [8,6,2]]

for j in matriz1:
    print(j)

matriz_transposta = matriz(matriz1)
print('\n')

for j in matriz_transposta:
    print(j)
