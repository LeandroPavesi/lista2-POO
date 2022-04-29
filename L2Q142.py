def incluir_novo_nome(listatelefonica):

    chave = input('Digite o nome da pessoa que deseja adicionar: ')
    conteudo = input('Digite o numero da pessoa que vc adicinou: ')

    listatelefonica[chave] = conteudo

    return listatelefonica
    ''' – essa função acrescenta um novo nome na agenda, com um
ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
'''
def incluir_telefone(listatelefonica): 

    chave = input('Digite o nome da pessoa que deseja adicionar: ')
    conteudo = input('Digite o numero da pessoa que vc adicinou: ')

    listatelefonica.update({f'{chave} :', conteudo})
    #falta conseguir adicionar mais um conteudo numa mesma chave
    return
'''– essa função acrescenta um telefone em um nome existente na
agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa
deseja incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir
o novo nome.'''

def excluir_telefone(listatelefonica): 

    remover = input('Digite o numero que deseja excluir')


    print(listatelefonica)

    tamamanho = len(listatelefonica)

    print(tamamanho)

    
    del listatelefonica[remover]

    return listatelefonica
    
    '''– essa função exclui um telefone de uma pessoa que já está na
agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.'''

def excluir_nome():
    
    ''' – essa função exclui uma pessoa da agenda.'''

def consultar_telefone():
    
    ''' – essa função retorna os telefones de uma pessoa na agenda.'''

