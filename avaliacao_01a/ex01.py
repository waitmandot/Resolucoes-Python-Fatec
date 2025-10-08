idade = int(input("Digite a idade: "))

if idade < 5:
    print('Ingresso gratuito')

elif idade <= 17 or idade > 60:
    print('Ingresso meia-entrada')

else:
    print('Ingresso inteiro')