# Faça um programa que mostre a tabuada de um 
# número informado.

multiplicando = 10
numero = int(input('Digite um numero inteiro: '))

print(f'Tabuada do {numero}\n')

while multiplicando > 0:
    resultado = numero * multiplicando
    print(f'{numero}x{multiplicando} = {resultado}')
    multiplicando -= 1