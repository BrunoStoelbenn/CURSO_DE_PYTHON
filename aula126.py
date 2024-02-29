# __dict__ e vars para atributos de instância

import json

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#     def get_ano_nascimento(self):
#         return Pessoa.ano_atual - self.idade

# # Criando uma instância da classe Pessoa
# dados_1 = {'nome': 'João', 'idade': 35}
# dados_2 = {'nome' : 'Bruno', 'idade' : 21}
# p1 = Pessoa(**dados_1)
# p2 = Pessoa(**dados_2)

# # p1.nome = 'EITA'
# # print(p1.idade)
# # p1.__dict__['outra'] = 'coisa'
# # p1.__dict__['nome'] = 'EITA'
# # del p1.__dict__['nome']
# # print(p1.__dict__)
# # print(vars(p1))
# # print(p1.outra)
# # print(p1.nome)
# # print(vars(p1))
# # print(p1.nome)

# # Salvando os dados da instância em um arquivo JSON

# with open('pessoa1.json', 'w', encoding='utf8') as arquivo:
#     json.dump(p1.__dict__, arquivo)
#     # json.dump(vars(p1), arquivo)

# # Lendo os dados do arquivo JSON
    
# with open('pessoa1.json', 'r', encoding='utf8') as arquivo:
#     dados_salvos_1 = json.load(arquivo)

# # Salvando os dados da instância em um arquivo JSON

# with open('pessoa2.json', 'w', encoding='utf8') as arquivo:
#     json.dump(vars(p2), arquivo)
#     # json.dump(vars(p1), arquivo)

# # Lendo os dados do arquivo JSON
    
# with open('pessoa2.json', 'r', encoding='utf8') as arquivo:
#     dados_salvos_2 = json.load(arquivo)

# # Criando uma nova instância da classe com os dados salvos
# p1_novo = Pessoa(**dados_salvos_1)
# p2_novo = Pessoa(**dados_salvos_2)

# # Verificando os atributos da nova instância

# print(vars(p1_novo))
# print(p1_novo.nome)
# print()
# print(p2_novo.__dict__)
# print(p2_novo.nome)