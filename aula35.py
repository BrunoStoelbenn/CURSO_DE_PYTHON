"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
# tabuada = 0
# multiplicando = 1

# while tabuada < 10:
#     tabuada += 1
#     print(f"***************TABUADA DO {tabuada}***************")
#     multiplicando = 1
#     while multiplicando <= 10:
#         resultado = tabuada * multiplicando
#         print(f"{tabuada} * {multiplicando} = {resultado}")
#         multiplicando += 1

condicao = True
        
while condicao:
    nome = input("Qual o seu nome: ")
    if nome == 'sair':
        break
    print(f"Seu nome é {nome}")

print("Acabou")