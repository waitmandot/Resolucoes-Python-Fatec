# Exercício 01
NUMERO_SORTEADO = 7

while True:
    numero = int(input("Adivinhe o número: "))

    if numero == NUMERO_SORTEADO:
        print('Parabéns, você acertou')
        break

    elif numero > NUMERO_SORTEADO:
        print('Tente um número menor.')
    else:
        print('Tente um número maior.')
