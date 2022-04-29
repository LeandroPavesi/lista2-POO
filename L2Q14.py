from typing import List
from L2Q142 import excluir_telefone, incluir_novo_nome, incluir_telefone


Listatelefonica = {}


while True:

    print('\n------ Menu Agenda ------')

    print('\n1 – Incluir novo nome')
    print('2 – Incluir telefone')
    print('3 – Excluir telefone')
    print('4 – Excluir nome')
    print('5 - Consultar telefone')
    print('6 - Sair')


    opcao = (input('Digite sua opção '))

    if opcao == '1':
            Listatelefonica =  incluir_novo_nome(Listatelefonica)

            print(Listatelefonica)#só de teste, ta funcionando
    elif opcao == '2':
            
            Listatelefonica =  incluir_telefone(Listatelefonica)

            print(Listatelefonica)#só de teste, ta funcionando
    elif opcao == '3':

         nova = {v: k for k, v in Listatelefonica.items()}

         Listatelefonica = excluir_telefone(nova)

         print(Listatelefonica)
         
    elif opcao == '4':
         pass
    elif opcao == '5':
         pass
    elif opcao == '6':
        print('Saindo....')
        break
    else:
        print('Opção inválida')