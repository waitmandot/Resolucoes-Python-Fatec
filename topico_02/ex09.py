# Escreva um programa que receba três valores numéricos representando
# os lados de um triângulo e determine se os valores podem formar um
# triângulo válido (a soma de dois lados deve ser sempre maior que o
# terceiro). Se for válido, classifique-o como: Equilátero: todos os 
# lados iguais; Isósceles: dois lados iguais; ou Escaleno: todos os 
# lados diferentes.

a = int(input('Digite o valor do lado a: '))
b = int(input('Digite o valor do lado b: '))
c = int(input('Digite o valor do lado c: '))

if a + b > c and c + b > a and a + c > b:
    if a == b and b == c:
        print('O triângulo é Equilátero')
    elif a == b or b == c or a == c:
        print('O triângulo é Isósceles')
    else:
        print('O triângulo é Escaleno')
else:
    print('Não é um triângulo')