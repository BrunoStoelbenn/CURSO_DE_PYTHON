# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ').lower()
    letras.add(letra)

    if 'l' in letras:
        print('PARABÉNS, VOCÊ GANHOU! ')
        break

    print(letras)
