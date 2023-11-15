# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
pessoa1 = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
pessoa2 = {
    "nome": "Bruno Cassiano",
    "sobrenome": "Stoelbenn",
    "idade": 21,
    "altura": 1.81,
    "endereços": [
        {'rua': 'tal tal', 'numero': 510},
        {'rua': 'outra rua', 'numero': 420}
    ],
}

# print(pessoa, type(pessoa))
print(pessoa1['nome'])
print(pessoa1['sobrenome'])

print()

for chave in pessoa1:
    print(f"{chave}: ", pessoa1[chave])

print()

for chave in pessoa2:
    print(f"{chave}: ", pessoa2[chave])