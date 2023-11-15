# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor 
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

numeros = 4, 6, 76, 9
print(multiplica(*numeros))

def par_ou_impar(n):
    if n % 2 == 0:
        return "É par"
    return "É ímpar"

def pares_ou_impares(*args):
    for numero in args:
        if numero % 2 == 0:
            print(f"{numero} é par")
        else:
            print(f"{numero} é ímpar")

print(par_ou_impar(10))
print(par_ou_impar(11))
print(par_ou_impar(13))
print(par_ou_impar(1102567))
print(par_ou_impar(110258))
ns = 10, 20, 30, 43, 57, 63, 71
pares_ou_impares(*ns)