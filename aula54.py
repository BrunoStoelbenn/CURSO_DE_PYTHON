import os
lista = []
while True:
    print("Selecione uma opção")
    opção = input("[i]nserir [a]pagar [l]istar [s]air: ").lower()

    try:
        if opção == 'i':
            os.system("cls")
            inserir_valor = input("Valor: ")
            lista.append(inserir_valor)
        elif opção == 'a':
            if len(lista) > 0:
                apagar_valor = int(input("Escolha o índice para apagar: "))
                lista.pop(apagar_valor)
            else:
                print("A lista está vazia. Insira um item na lista primeiro digitando 'i'")
        elif opção == 'l': 
            if len(lista) > 0:
                os.system("cls")
                for indice, item in enumerate(lista):
                    print(indice, item)
            else:
                print("A lista está vazia. Insira um item na lista primeiro digitando 'i'")
        elif opção == 's':
            os.system("cls")
            break
        else:
            print("Por favor, digite algo válido.")
    except:
        print("Não foi possível apagar este índice")