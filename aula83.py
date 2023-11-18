# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
    'arg5': 5,
}

mostro_argumentos_nomeados(configuracoes)
print()
mostro_argumentos_nomeados(**configuracoes)
print()
mostro_argumentos_nomeados(arg1=1, arg2=2, arg3=3, arg4=4, arg5=5)