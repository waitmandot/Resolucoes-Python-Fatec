# Faça um programa que faça a entrada de um texto. 
# Se for um e-mail, retorne "E-mail válido", caso contrário,
# retorne "E-mail inválido". Para tanto, verifique se o texto
# possui o símbolo @

email = input('Digite o seu email: ')

for caracter in email:
    if caracter == '@':
        print('Seu email é válido')
        break
else:
    print('Seu email não é válido')