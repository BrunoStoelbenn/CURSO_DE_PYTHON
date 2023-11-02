import os

palavra_secreta = "paralelepipedo".lower()
nova_palavra = list("*" * len(palavra_secreta))
contador = 0
print("".join(nova_palavra))
while True:
    letra_digitada = input("Digite uma letra ou digite 2 para tentar chutar a palavra: ").lower()

    contador += 1

    if letra_digitada == '2':
        adivinhar_palavra_secreta = input("Qual você acha que é a palavra secreta? ")
        if adivinhar_palavra_secreta == palavra_secreta:
            os.system("cls")
            print(f"Parabéns, você adivinhou a palavra '{palavra_secreta}' em {contador} tentativas!")
            break
        else:
            print("Essa não é a palavra.")
    i = 0
    
    if len(letra_digitada) > 1:
        print("Por favor, digite apenas uma letra.")
    
    elif len(letra_digitada) == 0:
        print("Por favor, digite uma letra.")
    else:
        for i in range(len(palavra_secreta)):
            if letra_digitada == palavra_secreta[i]:
                nova_palavra[i] = letra_digitada
                i += 1
            else:
                i += 1
        print("".join(nova_palavra))

        if "".join(nova_palavra) == palavra_secreta:
            os.system("cls")
            print(f"Parabéns, você adivinhou a palavra '{palavra_secreta}' em {contador} tentativas!")
            break
            
