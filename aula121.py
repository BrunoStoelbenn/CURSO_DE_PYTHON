# Métodos em instâncias de classse Python

class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('Ford', 'Escort', 'Prata', 2000)

print(carro1.marca, carro1.modelo, carro1.cor, carro1.ano)