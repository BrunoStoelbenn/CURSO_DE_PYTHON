# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string_First_Name = 'Bruno'  # str
# string_Last_Name = 'Stoelbenn'  # str
# print(string_First_Name.upper())
# print(string_Last_Name.upper())
# print(isinstance(string_First_Name, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Bruno', 'Stoelbenn')
# p1.nome = 'Bruno'
# p1.sobrenome = 'Stoelbenn'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print()

print(p2.nome)
print(p2.sobrenome)
