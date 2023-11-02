"""
Iterando strings com while
"""

nome = input("Digite o seu nome: ") # Iteráveis
novo_nome = ""

i = 0
while i < len(nome):
    novo_nome += "*" + nome[i]
    i += 1

print(novo_nome)