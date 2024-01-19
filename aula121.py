# Métodos em instâncias de classse Python
# Hard coded - É algo que foi escrito diretamente no código

class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def acelerar(self):
        print(f"{self.marca} {self.modelo} {self.cor} {self.ano} está pisando fundo!")

carro1 = Carro('Ford', 'Escort Zetec 1.8 16v', 'Prata', 2000)

print(carro1.marca, carro1.modelo, carro1.cor, carro1.ano)

carro2 = Carro("Volkswagen", "Fusca 1600", "Branco", 1990)

print(carro2.marca, carro2.modelo, carro2.cor, carro2.ano)

print()
carro1.acelerar()
print()
carro2.acelerar()
print()
