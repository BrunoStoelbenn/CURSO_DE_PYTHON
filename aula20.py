primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if float(primeiro_valor) > float(segundo_valor):
    print(f'{primeiro_valor=} é maior do que {segundo_valor=}')

elif float(segundo_valor) > float(primeiro_valor):
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')

elif float(primeiro_valor) == float(segundo_valor):
    print(f'{segundo_valor=} é igual ao {primeiro_valor=}')

else:
    print('Digite um número, não uma letra!')