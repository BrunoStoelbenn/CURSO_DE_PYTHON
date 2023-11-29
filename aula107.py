# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
    # Use a função zip para combinar as duas listas
    # e use a função min para determinar o número de elementos a serem combinados
    return list(zip(lista1, lista2))

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

resultado = zipper(cidades, estados)
print(resultado)

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
# lista_soma = []
# tam_min = len(min(lista_a, lista_b))
# print(tam_min)

# i = 0
# while i < tam_min:
#     lista_soma.append(lista_a[i] + lista_b[i])
#     i+=1

# print(lista_soma)

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
