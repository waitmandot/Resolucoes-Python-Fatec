# Escreva um programa que leia a velocidade de um carro. 
# Se esta velocidade for maior que 80Km/h o programa deverá
# escrever uma mensagem na tela avisando que o usuário levou
# uma multa e o valor a ser pago. Considere R$ 7 reais por
# cada Km acima do limite.

LIMITE = 80
VALOR_MULTA = 7

velocidade = float(input('Digite a velocidade de um carro em Km/h: '))

if velocidade > LIMITE:
    print('Você levou uma multa por excesso de velocidade!')
    multa = (velocidade - LIMITE) * VALOR_MULTA
    print(f'Sua multa é de R${multa}')