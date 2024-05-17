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
            valor = input("Item: ")
            lista.append(valor)
            continue

        if opcao == 2:
            os.system('cls')

            for indice, nome in enumerate(lista):
                print(indice, nome)

            excluir = int(input("Insira o indice para excluir: "))
            del lista[excluir]

            print("\nElemento '{}', excluído com sucesso. ".format(excluir))

            continue

        if opcao == 3:
            os.system('cls')
            for indice, nome in enumerate(lista):
                print(indice, nome)

        if opcao == 4:
            ...

        else:
            break

    except:
        print("Erro ao executar. . .")