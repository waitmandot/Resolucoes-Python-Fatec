# Crie um programa que, dada a altura e peso de uma pessoa, 
# calcule o seu IMC (Índice de Massa Corporal) e indique sua 
# situação de acordo com a tabela abaixo. O cálculo do IMC é
# feito pela divisão do peso pela altura ao quadrado.
#  Abaixo de 17. Muito abaixo do peso
#  Entre 17 e 18,49 Abaixo do peso
#  Entre 18,5 e 24,99 Peso normal
#  Entre 25 e 29,99 Acima do peso
#  Entre 30 e 34,99 Obesidade I
#  Entre 35 e 39,99 Obesidade II (severa)
#  Acima de 40 Obesidade III (mórbida)

altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso em kg: '))

imc = peso / pow(altura, 2)

if imc < 17:
    print('Muito abaixo do peso')
elif imc >= 17 and imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso normal')
elif imc >= 25 and imc < 30:
    print('Acima do peso')
elif imc >= 30 and imc < 35:
    print('Obesidade I')
elif imc >= 35 and imc < 40:
    print('Obesidade II')
elif imc >= 40:
    print('Obesidade III')