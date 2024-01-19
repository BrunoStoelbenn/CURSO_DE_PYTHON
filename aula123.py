# Escopo da classe e de métodos da classe
# class Animal:
#     # nome = 'Leão'

#     def __init__(self, nome):
#         self.nome = nome

#         variavel = 'valor'
#         print(variavel)

#     def acao(self, acao):
#         print(f"{self.nome} está {acao}")
    
#     def comendo(self, alimento):
#         return f'{self.nome} está Comendo um {alimento}'

# leão = Animal('Leão')
# print(leão.nome)
# leão.acao("Caçando um Veado")
# print(leão.comendo("Veado"))

# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))