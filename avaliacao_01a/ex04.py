palavra = 'Fatec Rio Preto'
palavra = 'tecnologia'
palavra = 'aluno'

for p in palavra:
    if p.isupper():
        print('Found')
        break
else:
    print('Not Found')

# Found, Not Found, Not Found