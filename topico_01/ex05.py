# Implemente um programa que tenha como entrada o valor em uma reais e mostre o valor correspondente em dólar.

ValorReais = int(input('Escreva um valor em reais: R$'))

ValorDolar = round(ValorReais / 5.51, 2)

print(f'Esse valor em dolares é ${ValorDolar}')