"""
Faça uma lista de compras
O usuario deve ter a possibilidade de inserir, apagar
e listar os valores de sua lista.
Não permita que o programa quebre com erros de
índices inexistentes na lista

"""
import os

lista = []

while(True):
    
    print("\n")
    print("\tMenu\n")
    print("\t1- Inserir\n")
    print("\t2- Apagar item\n")
    print("\t3- Listar\n")
    print("\t4- Busca por indice\n")
    print("\t5- Sair\n")
    opcao = int(input("Escolha: "))
    print("\n")

    try: 
        if opcao == 1:
            os.system('cls')
            valor = input("Valor: ")
            lista.append(valor)
            continue

        if opcao == 2:
            os.system('cls')

            for indice, nome in enumerate(lista):
                print(indice, nome)

            excluir = int(input("Insira o indice para excluir: "))

            lista_enumerada = enumerate(lista)
            del lista[excluir]

            print("\nElemento '{}', excluído com sucesso. ".format(excluir))

            continue

        if opcao == 3:
            os.system('cls')
            for indice, nome in enumerate(lista):
                print(indice, nome)

        if opcao == 4:
            os.system('cls')
            
            pesquisa = int(input("Insira o indice de pesquisa: "))
            lista_enumerada = enumerate(lista)

            if pesquisa in lista_enumerada:
                pesquisa = lista_enumerada
                print(pesquisa)

    except:
        print("Erro ao executar. . .")