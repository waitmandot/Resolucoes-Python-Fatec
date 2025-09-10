# Faça um programa para jogar Jokenpô (clássico pedra, papel 
# e tesoura) com você. Você deverá informar uma das opções, 
# o programa deverá então sortear uma das três opções possíveis
# e mostrar quem ganhou na tela.
import random

computador = random.choice(['pedra', 'papel', 'tesoura'])
usuario = input('pedra\npapel\ntesoura\nDigite a sua escolha: ')

usuario = usuario.lower()

if computador == usuario:
    print(f'Empate! Computador jogou {computador}')
elif computador == 'pedra' and usuario == 'tesoura' or computador == 'papel' and usuario == 'pedra' or computador == 'tesoura' and usuario == 'papel':
    print(f'Perdeu! Computador jogou {computador}')
else:
    print(f'Ganhou! Computador jogou {computador}')