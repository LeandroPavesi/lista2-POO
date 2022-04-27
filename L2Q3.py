import statistics

opcoes_validas = [1, 2, 3, 4, 5]
avaliação = []

while True:
    print('\nAvalie a cantina do ifes numa escala de 1 a 5, com 1 sendo péssimo e 5 excelente')
    opcao_voto = int(input('Digite sua nota para avaliação: '))
    if opcao_voto not in opcoes_validas:
        break
    avaliação.append(opcao_voto)

print('\nVotos computados', avaliação)

for op in opcoes_validas:

    total_votos = avaliação.count(op)
    percentual = (total_votos / len(avaliação))

    print(f'\nOpção: {op}')
    print(f'Total de votos : {total_votos}')
    print(f'Percentual : {percentual}')

minimo = min(avaliação)
print('\n O valor minimo é: ', minimo)
maximo = max(avaliação)
print('\n O valor máximo é: ', maximo)

soma = 0
for numero in avaliação:
    soma += numero

media = soma / len(avaliação)
print('\n a media é: ', media)

mediana = statistics.median(avaliação)
print('A mediana é: ', mediana)

moda = statistics.mode(avaliação)
print('A moda é: ', moda)

variancia = statistics.variance(avaliação)
print('A variância é: ', variancia)

desvio_padrão = statistics.stdev(avaliação)
print('O desvio padrão é: ', desvio_padrão)