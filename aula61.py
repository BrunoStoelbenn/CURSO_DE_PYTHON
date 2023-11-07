"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
digitar_cpf = input("Digite o cpf que você deseja validar: ")
cpf_formatado_sem_ponto = digitar_cpf.replace(".", "")
cpf_formatado = cpf_formatado_sem_ponto.replace("-", "")
multiplicar_cpf = 0
i = 10
j = 0
somar_cpf = 0

while i > 2:
    multiplicar_cpf = i * int(cpf_formatado[j])
    somar_cpf += multiplicar_cpf
    i -= 1
    j += 1
resultado = (somar_cpf * 10) % 11
resultado=0 if resultado > 9 else resultado
print(f"O primeiro dígito do cpf é {resultado}")