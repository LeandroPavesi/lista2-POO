n = int(input('Digite o tamanho max das lista'))

l1 = []
p_a1 = 0

l2 = []
p_a2 = 0

for i in range(n):
    pontos1 = int(input('\nDigite os numeros da primeira lista'))
    l1.append(pontos1)

for i in range(n):
    pontos2 = int(input('\nDigite os numeros da segunda lista'))
    l2.append(pontos2)

d = 0
while d <= n:
    for c in range(n):
        if l1[d] > l2[d]:
            p_a1 += 1
            print('O Aluno 1 ganhou um ponto')
        elif l1[d] < l2[d]:
            p_a2 += 1
            print('O Aluno 2 ganhou um ponto')
        else:
            print('Ninguem ganhou ponto')
        d += 1

    print('A pontuação do Aluno 1 é de: ', p_a1)

    print('A pontuação do Aluno 2 é de: ', p_a2)
        

