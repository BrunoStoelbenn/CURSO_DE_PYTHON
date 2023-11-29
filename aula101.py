# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

def divide(x, y):
    return x / y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

def criar_funcao_dividir(funcao, y):
    def interna(x):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
divide_por_dois = criar_funcao_dividir(divide, 2)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
print(divide_por_dois(50))