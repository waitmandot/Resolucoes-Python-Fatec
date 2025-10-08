numero = int(input("Digite sua senha numérica: "))

soma = 0

for digito in str(numero):
    soma += int(digito)

if soma % 2 == 0:
    print('Abriu o cofre')
else:
    print('Senha inválida')

