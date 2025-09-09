# Faça um programa em que ele sorteie um número entre 0 e 5. 
# O usuário deverá então adivinhar este número e o programa
# deverá escrever na tela se ele acertou ou não.

import random

numero_sorteado = random.randint(0, 5)

numero_usuario = int(input('Escolha um número de 0 à 5: '))

if numero_sorteado == numero_usuario:
    print(f'Você acertou! O número sorteado foi {numero_sorteado}')
else:
    print(f'Você errou. O número sorteado foi {numero_sorteado}')