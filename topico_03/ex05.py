# Faça um programa que leia um número inteiro e mostre 
# na tela se é ou não um número primo.

numero = int(input('Digite um número inteiro: '))
is_primo = True


if numero <= 1:
    is_primo = False

for i in range(2, numero, 1):
    if numero % i == 0:
        is_primo = False
        print('Seu número não é primo')
        break
else:
    print('Seu número é primo')

