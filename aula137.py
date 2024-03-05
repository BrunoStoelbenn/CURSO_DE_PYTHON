# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None

    def inserir_motor(self, motor):
        self.motor = motor

    def inserir_fabricante(self, fabricante):
        self.fabricante = fabricante

    def imprimir_carro(self):
        print()
        print(f"O carro é um {self.nome}, tem um motor {self.motor.mostrar_motor()} e é da fabricante {self.fabricante.mostrar_fabricante()}")
        print()

class Motor:
    def __init__(self, nome_motor):
        self.nome_motor = nome_motor

    def mostrar_motor(self):
        return self.nome_motor

class Fabricante:
    def __init__(self, nome_fabricante):
        self.nome_fabricante = nome_fabricante

    def mostrar_fabricante(self):
        return self.nome_fabricante


# Restante do código permanece o mesmo...

carro_escort = Carro("Escort")
fabricante_ford = Fabricante("Ford")
motor_escort = Motor("Ford Zetec")
carro_escort.inserir_motor(motor_escort)
carro_escort.inserir_fabricante(fabricante_ford)
carro2 = Carro("Focus")
carro2.inserir_motor(motor_escort)
carro2.inserir_fabricante(fabricante_ford)
carro_escort.imprimir_carro()
carro2.imprimir_carro()
