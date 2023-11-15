# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam 
# o número recebido como parâmetro.

def fazer_potencia(potencia):
    def potenciar(num):
        num_aux = num
        i = 1
        while i < potencia:
            num *= num_aux
            i += 1
        return num
    return potenciar

def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)
ao_quadrado = fazer_potencia(2)
ao_cubo = fazer_potencia(3)
quarta_potencia = fazer_potencia(4)
print(ao_quadrado(10))
print(ao_cubo(10))
print(quarta_potencia(10))
print(ao_cubo(16))

