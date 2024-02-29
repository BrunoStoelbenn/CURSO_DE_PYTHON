n = int(input(""))  # Digitar o número de valores que será lido
vetor = [int(x) for x in input().split()]  # Digitar os valores que serão armazenados dentro do vetor fornecendo sempre um espaço entre eles

menor_valor, posicao = vetor[0], 0  # Criação das variáveis menor_valor que já possui o vetor[0] dentro dela e posicao que já possui o 0 dentro dela
for n in range(1, n):  # Laço de repetição que começa no primeiro indíce e vai ser lido até o índice n fornecido na primeira linha do código
    if vetor[n] < menor_valor:  # Compara se o vetor da posição [n] é menor do que o menor_valor
        menor_valor, posicao = vetor[n], n  # Se o vetor da posição [n] for menor do que o menor_valor, então o menor_valor assume o vetor[n] e a posição fica o próprio n

print("Menor valor:", menor_valor)  #  Impressão do menor valor
print("Posicao:", posicao)  # Impressão da posição
