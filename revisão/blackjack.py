# Implemente em Python um jogo de cartas 21 (Blackjack simplificado),
# utilizando as estruturas de dados dict e list. O jogo
# deve permitir que o jogador dispute contra o computador, somando valores
# de cartas até chegar o mais próximo possível de 21 pontos, sem ultrapassar
# esse valor. Cada carta deve ser representada como um dicionário contendo
# o número e o naipe, e o baralho deve ser uma lista embaralhada de cartas.
# O jogador e o computador devem receber duas cartas iniciais, e novas cartas
# podem ser retiradas do sempre do final do baralho. O programa deve
# exibir as cartas e pontuações finais, indicando o vencedor. Utilize o
# código abaixo como base para a definição dos naipes:

import random

# Set up the constants:
HEARTS = chr(9829)    # Character 9829 is '♥'
DIAMONDS = chr(9830)  # Character 9830 is '♦'
SPADES = chr(9824)    # Character 9824 is '♠'
CLUBS = chr(9827)     # Character 9827 is '♣'

numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
naipes = [HEARTS, DIAMONDS, SPADES, CLUBS]

baralho = []
deck_computador = []
deck_jogador = []

input('Bem vindo ao Dezanis BET\nPara jogar o BlackJack simplificado aperte enter')

for naipe in naipes:
    for numero in numeros:
        carta = {'numero': numero, 'naipe': naipe}
        baralho.append(carta)

print('\n* Baralho montado. *\n')

print('Computador entrou, ele será o Dealer.\n')

random.shuffle(baralho)

print('* O computador embaralhou o baralho *\n')

deck_computador.append(baralho.pop())

deck_computador.append(baralho.pop())

pontos_computador = 0

for carta in deck_computador:
    if carta.get('numero') == 'A':
        pontos_computador += 1
    else:
        pontos_computador += int(carta.get('numero'))

print('* O computador tira as duas ultimas cartas do baralho *\n')

deck_jogador.append(baralho.pop())

deck_jogador.append(baralho.pop())

pontos_jogador = 0

for carta in deck_jogador:
    if carta.get('numero') == 'A':
        pontos_jogador += 1
    else:
        pontos_jogador += int(carta.get('numero'))

print('* O computador te entrega as duas ultimas cartas do baralho *\n')
print('Esse é seu deck e sua pontuação nessa rodada\n')
print(f'Sua pontuação: {pontos_jogador}')
print(f'Seu Deck: {deck_jogador}')

while True:
    comprar = input('\nDeseja comprar cartas?\n1 - Sim\n2 - Não\n')
    if comprar == '1':
        qntd_cartas = int(input(f'Quantas cartas quer comprar? (max: {len(baralho)} cartas): '))
        if qntd_cartas <= len(baralho):
            for index in range(qntd_cartas):
                deck_jogador.append(baralho.pop())
                carta = deck_jogador[len(deck_jogador) - 1]
                if carta.get('numero') == 'A':
                    pontos_jogador += 1
                else:
                    pontos_jogador += int(carta.get('numero'))
                print(f'Você retirou a carta {carta}')
                if pontos_jogador > 21:
                    print('\nVocê perdeu! Seu deck ultrapassou o número 21')
                    print(f'Sua pontuação: {pontos_jogador}')
                    print(f'Seu Deck: {deck_jogador}')
                    print(f'Pontuação do computador: {pontos_computador}')
                    print(f'Deck do computador: {deck_computador}')
                    print(f'Cartas restantes no baralho: {len(baralho)}')
                    break
            print('\nEsse é seu deck e sua pontuação nessa rodada\n')
            print(f'Sua pontuação: {pontos_jogador}')
            print(f'Seu Deck: {deck_jogador}')
        elif qntd_cartas > len(baralho):
            print(f'Você não pode tirar mais de {len(baralho)} cartas!')
            continue
        else:
            continue
    elif comprar == '2':
        while pontos_computador <= 17:
            deck_computador.append(baralho.pop())
            carta = deck_computador[len(deck_computador) - 1]
            if carta.get('numero') == 'A':
                pontos_computador += 1
            else:
                pontos_computador += int(carta.get('numero'))
            print('O computador pegou uma carta')
            if pontos_computador > 21:
                print('\nVocê ganhou! O Deck do computador ultrapassou o número 21')
                print(f'Sua pontuação: {pontos_jogador}')
                print(f'Seu Deck: {deck_jogador}')
                print(f'Pontuação do computador: {pontos_computador}')
                print(f'Deck do computador: {deck_computador}')
                print(f'Cartas restantes no baralho: {len(baralho)}')
                break
        else:
            if pontos_computador > pontos_jogador:
                print('\nVocê perdeu! O Deck do computador é mais próximo de 21')
                print(f'Sua pontuação: {pontos_jogador}')
                print(f'Seu Deck: {deck_jogador}')
                print(f'Pontuação do computador: {pontos_computador}')
                print(f'Deck do computador: {deck_computador}')
                print(f'Cartas restantes no baralho: {len(baralho)}')
                break
            elif pontos_computador < pontos_jogador:
                print('\nVocê ganhou! O seu Deck é mais próximo de 21')
                print(f'Sua pontuação: {pontos_jogador}')
                print(f'Seu Deck: {deck_jogador}')
                print(f'Pontuação do computador: {pontos_computador}')
                print(f'Deck do computador: {deck_computador}')
                print(f'Cartas restantes no baralho: {len(baralho)}')
                break
            else:
                print(f'\nVocê empatou! Ambos pararam na pontuação {pontos_jogador}')
                print(f'Sua pontuação: {pontos_jogador}')
                print(f'Seu Deck: {deck_jogador}')
                print(f'Pontuação do computador: {pontos_computador}')
                print(f'Deck do computador: {deck_computador}')
                print(f'Cartas restantes no baralho: {len(baralho)}')
    else:
        continue