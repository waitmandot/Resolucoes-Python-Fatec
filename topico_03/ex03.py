# Escreva um programa que leia um número inteiro
# qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite o numero inteiro a ser fatorado: '))
resultado = 1
multiplicando = numero
print(f'{numero}! = {numero} x ', end='')

while multiplicando > 1:
    resultado = resultado * multiplicando
    multiplicando -= 1

    print(f'{multiplicando} ', end='')

    if multiplicando != 1:
        print('x ', end='')

print(f'= {resultado}', end='')