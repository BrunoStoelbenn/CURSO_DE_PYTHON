import re
#Gerador de CPF

entrada = input("Digite os primeiros nove dígitos que você quer ter no seu cpf: ")
cpf_enviado = re.sub(
    r"[^0-9]",
    "",
    entrada
)
if len(cpf_enviado) > 9:
    print("Por favor, digite apenas nove números")
elif len(cpf_enviado) < 9:
    print("Você tem que digitar os primeiros nove números do cpf para nós gerarmos o resto")
else:
    entrada_e_sequencial = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)
    nove_digitos = cpf_enviado[:9]
    contador_regressivo_1 = 10
    resultado_1 = 0
    contador_regressivo_2 = 11
    resultado_2 = 0

    for digito_1 in nove_digitos:
        resultado_1 += (int(digito_1) *     contador_regressivo_1)
        contador_regressivo_1 -= 1
        resultado_2 += (int(digito_1) *     contador_regressivo_2)
        contador_regressivo_2 -= 1

    digito_1 = (resultado_1 * 10) % 11
    digito_1=0 if digito_1 > 9 else digito_1 
    digito_2 = ((resultado_2 + (digito_1 * 2)) * 10) % 11
    digito_2=0 if digito_2 > 9 else digito_2
    cpf_gerado_calculo = f"{nove_digitos}{digito_1}{digito_2}   "
    print(cpf_gerado_calculo)


