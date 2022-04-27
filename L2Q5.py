p = [1,5,6,2,10,4,15,11,3,20]

p_max = 0

p_min = 0

for i in range(10): 
    if p[i] > 10: #Se o elemento da lista for maior q 10, ele vai pra p max
        print('Deu certo')
        p_max += 1
    else:
        print('Deu errado')
        p_min += 1

print('\nA pontuação máxima é: ', p_max)

print('\nA pontuação mínima é: ', p_min)

