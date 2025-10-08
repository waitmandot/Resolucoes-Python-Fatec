# Faça um programa que gere 10 números inteiros. 
# Em seguida, crie uma nova lista removendo os números
# repetidos. No final, mostre essa nova lista.

import random

numeros = []

for i in range(0, 11):
    numero_sorteado = random.randint(0, 11)
    numeros.append(numero_sorteado)

print(f"{numeros}")

for numero in numeros:
    repetitions = numeros.count(numero)
    if repetitions > 1:
        for i in range(repetitions-1):
            numeros.remove(numero)
    print(f"Analizando a '{numero}' ficou assim = '{numeros}'")

numeros.sort()

print(numeros)