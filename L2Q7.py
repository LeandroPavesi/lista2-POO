n=int(input("Digite o numero de linhas e colunas: "))

matriz = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
    matriz.append(l)

#diagonal principal
magico=0
for i in range(n):
    magico = magico + matriz[i][i]
    
#diagonal secundaria
soma=0
for i in range(n):
    soma = soma + matriz[i][n-1-i]
if (soma != magico):
    print('A matriz não é um quadrado magico')
    exit()

#linhas
for i in range(n):
    soma=0
    for j in range(n):
        soma=soma+matriz[i][j]
    if (soma != magico):
        print('A matriz não é um quadrado magico')
        exit()
        
#colunas
for j in range(n):
    soma=0
    for i in range(n):
        soma=soma+matriz[i][j]
    if (soma != magico):
        print('A matriz não é um quadrado magico')
        exit()
        
print('A matriz é um quadrado magico')