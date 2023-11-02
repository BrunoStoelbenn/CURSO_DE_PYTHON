""" Calculadora com while """

while True:
    n1 = (input("Digite um numero: "))
    n2 = (input("Digite outro numero: "))
    operador = input("Digite o operador (+-/*): ")
    try:
        n1 = float(n1)
        n2 = float(n2)
        if operador == '+': 
            print(n1 + n2)
        elif operador == '-': 
            print(n1 - n2)
        elif operador == '*': 
            print(n1 * n2)
        elif operador == '/': 
            print(n1 / n2)
        else:
            print("Por favor, digite o operador certo e digite apenas um operador por vez + - * /")

    except:
        print("Por favor, digite apenas números!.")
    
    sair = input("Quer sair: [s]im: ").lower().startswith('s')

    if sair is True:
        break