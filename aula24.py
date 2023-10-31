# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4
#  B R U N O
# -5-4-3-2-1
# def imprimir_cabecalho(sep):
#     print(10 * sep)

# nome = 'Bruno'
# # print(nome[2])
# # print(nome[-4])
# print('uno' in nome)
# print('zero' in nome)
# imprimir_cabecalho('-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

