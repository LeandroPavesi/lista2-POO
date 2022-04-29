vogais = ['a', 'e', 'i', 'o', 'u']

palavra = input('Digite a palavra para jogar: ')



tamanho = len(palavra.split())

teste = palavra.split(' ')

print(teste)
print(tamanho)
print(vogais)

soma = 0
pontos = 0

for c in palavra:
    for d in vogais:
        if palavra[c] == vogais[d]:  #ta dando erro aq
            soma += 1
            if soma/2 % 0:
                pontos += 1
                print('Somou', soma)
            else:
                pontos += 2
                print('Somou2', soma)
        
pontuação_total = soma/tamanho

print(pontuação_total)


            
    