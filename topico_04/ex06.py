# Implemente o jogo da forca. Um usuário deverá entrar 
# com uma palavra. Em seguida, outro usuário deverá 
# indicar as letras dessa palavra. Caso exista, deverá 
# ser mostrada as letras e as suas posições na palavra. 
# Caso não exista, o usuário perderá uma chance. No total, 
# o usuário terá 6 chances para acertar.

palavra = input('Digite a palavra para ser adivinhada: ')
chances = 6
forca = []

letras_palavra = list(palavra)

for i in range(len(palavra)):
    forca.append('_')

while chances >= 1:
    if forca.count('_') == 0:
            print(f'Parabéns você acertou! A palavra era {palavra}')
            break
    print(f'Chances {chances}')
    print(forca)
    tentativa = input('Digite uma letra ou palavra: ')

    if len(tentativa) == 1:
        ocorrencias = letras_palavra.count(tentativa)
        if ocorrencias >= 1:
            for index, letra in enumerate(letras_palavra):
                if letra == tentativa:
                    forca[index] = letra
        else:
            chances -= 1
    elif len(tentativa) > 1:
        if tentativa == palavra:
            print(f'Parabéns você acertou! A palavra era {palavra}')
            break
        else:
            chances -= 1
else:
    print(f'Suas chances acabaram, você perdeu! A palavra era {palavra}')


