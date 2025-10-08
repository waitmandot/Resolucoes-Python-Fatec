# Faça um programa que crie uma lista vazia. Em seguida,
# o usuário deverá informar as notas de trabalhos obtidas
# (pode variar de 0 até quantos trabalhos forem informados).
# Por fim, mostre a média aritmética das notas obtidas.

notas = []
media = 0

while True:
    print(f'Notas = {notas}')
    print('1 - Adicionar nota de trabalho\n2 - Gerar média das notas')
    option = input('Digite uma das opções: ')
    if option == '1':
        nota_inserida = float(input('Digite o valor da nota: '))
        notas.append(nota_inserida)
    elif option == '2':
        break
    else:
        continue

for nota in notas:
    media += nota

if len(notas) != 0:
    media = media / len(notas)

print(f'A média das notas {notas} é {media}')