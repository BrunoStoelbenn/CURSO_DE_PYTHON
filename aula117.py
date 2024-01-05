import json

pessoa = {
    'nome': 'Bruno Cassiano',
    'sobrenome': 'Stoelbenn',
    'enderecos': [
        {'rua': 'Avenida Dom Alberto Etges', 'numero': 550},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.81,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])