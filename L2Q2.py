texto = input('Digite um texto: ')

novo_texto = ""
for letra in texto: 
    if letra in "Aa":
        novo_texto = novo_texto + "4"
    elif letra in "Bb":
        novo_texto = novo_texto + "8"
    elif letra in "Ee":
        novo_texto = novo_texto + "3"
    elif letra in "Oo":
        novo_texto = novo_texto + "0" 
    elif letra in "Ss":
        novo_texto = novo_texto + "5"
    elif letra in "Tt":
        novo_texto = novo_texto + "7"
    else:
        novo_texto += letra

print('O novo texto é: ', novo_texto)