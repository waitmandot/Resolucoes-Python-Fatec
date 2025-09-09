# Escreva um programa que leia o salário de um
# funcionário e calcule o seu aumento. Caso o 
# salário atual seja superior a R$ 1.000,00 
# calcule um aumento de 10%, caso contrário, 
# calcule um aumento de 15%.

salario = float(input('Digite o seu salário: '))

if salario > 1000:
    salario = salario + salario * 0.1
else:
    salario = salario + salario * 0.15

print(f'O seu salário atual é de {salario}')