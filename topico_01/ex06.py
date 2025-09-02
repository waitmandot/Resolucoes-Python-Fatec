# Crie um programa que leia dois números e uma operação (soma, subtração, multiplicação ou divisão)
# do usuário. Realize a operação correspondente e mostre o resultado.

numero_1 = float(input('Digite o primeiro operando: '))
numero_2 = float(input('Digite o segundo operando: '))
operador = int(input('1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\nDigite o operando: '))

if operador == 1:
    resultado = numero_1 + numero_2
elif operador == 2:
    resultado = numero_1 - numero_2
elif operador == 3:
    resultado = numero_1 * numero_2
elif operador == 4:
    resultado = numero_1 / numero_2

print(f'O resultado é {resultado}')