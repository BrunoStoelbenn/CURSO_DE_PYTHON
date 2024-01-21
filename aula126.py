# __dict__ e vars para atributos de instância

import json

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

# Criando uma instância da classe Pessoa
dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

# p1.nome = 'EITA'
# print(p1.idade)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)
# print(vars(p1))
# print(p1.nome)

# Salvando os dados da instância em um arquivo JSON
with open('pessoa.json', 'w', encoding='utf8') as arquivo_json:
    json.dump(vars(p1), arquivo_json)

# Lendo os dados do arquivo JSON
with open('pessoa.json', 'r', encoding='utf8') as arquivo_json:
    dados_salvos = json.load(arquivo_json)

# Criando uma nova instância da classe com os dados salvos
p2 = Pessoa(**dados_salvos)

# Verificando os atributos da nova instância
print(vars(p2))
print(p2.nome)