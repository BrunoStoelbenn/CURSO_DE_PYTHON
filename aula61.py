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
cpf_enviado_e_formatado = cpf_formatado_sem_ponto.replace("-", "")
nove_digitos = cpf_enviado_e_formatado[:9]
contador_regressivo_1 = 10
resultado_1 = 0
contador_regressivo_2 = 11
resultado_2 = 0

for digito_1 in nove_digitos:
    resultado_1 += (int(digito_1) * contador_regressivo_1)
    contador_regressivo_1 -= 1
    resultado_2 += (int(digito_1) * contador_regressivo_2)
    contador_regressivo_2 -= 1
print(resultado_1)

digito_1 = (resultado_1 * 10) % 11
digito_1=0 if digito_1 > 9 else digito_1 
digito_2 = ((resultado_2 + (digito_1 * 2)) * 10) % 11
digito_2=0 if digito_2 > 9 else digito_2
print(f"O primeiro dígito do cpf é {digito_1}")
print(f"O segundo dígito do cpf é {digito_2}")
cpf_gerado_calculo = f"{nove_digitos}{digito_1}{digito_2}"
if cpf_enviado_e_formatado == cpf_gerado_calculo:
    print(f"{cpf_enviado_e_formatado} é válido!")

else:
    print(f"{cpf_enviado_e_formatado} é inválido!")



