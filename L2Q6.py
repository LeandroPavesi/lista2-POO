def matriz(num_linhas, num_colunas):
    mat = [[0,0,0], [0,0,0], [0,0,0]]
    #cria a matriz com 0, e ai substitui os 0 dps p preencher
    '''for l in range(num_linhas): #quantidade de linhas
            elemento = []
            for c in range(num_colunas): #quanti de colunas
                    elemento.append(0)
                    mat.append(elemento)
    print(mat)'''
    
    #preencher a matriz
    for l in range(num_linhas, num_colunas):
        for c in range(num_linhas, num_colunas):
            mat[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

    #printando a matriz de forma bonitinha
    for l in range(num_linhas, num_colunas):
        for c in range(num_linhas, num_colunas):
            print(f'[{mat[l][c]}]', end=' ')
        print()
    
    
    M_t = list(map(list, zip(*mat)))
    return M_t


Quant_linhas = int(input('Digite a quantidade de linhas:'))

Quant_colunas = int(input('Digite a quantidade de colunas:'))

matriz_transposta = matriz(3, 3)

for j in matriz_transposta:
    print(j)