import os

lista = []

while(True):
    
    print("\n")
    print("\tMenu", '-' * 10)
    print("\t[1]- Inserir\n")
    print("\t[2]- Apagar item\n")
    print("\t[3]- Listar\n")
    print("\t[4]- Editar item\n")
    print("\t[5]- Sair\n")
    opcao = input("Escolha: ").strip()
    print("\n")

    try: 
        if opcao == '1':
            os.system('cls')
            valor = input("Item: ").strip()
            lista.append(valor)
            print("\nO item '{}' foi adicionado com sucesso.".format(valor))
            continue

        if opcao == '2':
            os.system('cls')

            print("-"*50)
            print('\t', 'Indice','\t', 'Item', '\n')
            print("-"*50)

            for indice, nome in enumerate(lista, 1):
                print('\t', indice, '\t\t', nome, '\n')

            print("\n")
            excluir = int(input("Insira o indice para excluir: ").strip())

            if excluir < 0 or excluir > len(lista):
                print("\nIndice invalido. \n")
                continue
             
            print("\n")
            confirmacao = input("Tem certeza que deseja excluir o item '{}' da lista? \n[S]im\n[N]ão \n\nEscolha: ".format(lista[excluir -1])).strip().upper()
            

            if confirmacao == 'S':
                del lista[excluir -1]
                print("\nO elemento '{}' foi excluído com sucesso. ".format(excluir))
                continue

            else: 
                print("\nExclusão cancelada.")
                continue

        if opcao == '3':
            os.system('cls')
            print("-"*50)
            print('\t', 'Indice','\t', 'Item', '\n')
            print("-"*50)

            for indice, nome in enumerate(lista):
                print('\t', indice, '\t\t', nome, '\n')
                
            continue
        
        if opcao == '4':

            os.system('cls')

            print("-"*50)
            print('\t', 'Indice','\t', 'Item', '\n')
            print("-"*50)

            for indice, nome in enumerate(lista, 1):
                print('\t', indice, '\t\t', nome, '\n')

            print("\n")
            editar = int(input("Insira o indice do item para editar: ").strip())

            if editar < 0 or editar > len(lista):
                print("\nIndice invalido. \n")
                continue

            else:
                item_antigo = lista[editar - 1]
                novo_item = input("\nDigite o novo item: ")
                lista[editar -1] = novo_item
                print("\nO item '{}' foi editado com sucesso para '{}'.".format(item_antigo, novo_item))
                continue

        else:
            break

    except:
        os.system('cls')
        print("\nErro ao executar. . .")
        continue