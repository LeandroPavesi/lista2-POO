def eh_palindroma(palavra):

    palavra_min = palavra.lower()

    palavra_invertida = palavra_min[::-1]

    if palavra_min == palavra_invertida:
        return print(True)
    else:
        return print(False)

palavra = input('Digite uma palavra: ')

eh_palindroma(palavra)
