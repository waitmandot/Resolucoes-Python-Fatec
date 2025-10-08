# Faça um programa que contenha duas listas com 5 posições.
# Na primeira lista, deverá ser inserido o nome dos alunos.
# Na segunda lista, na mesma posição, a nota do aluno. Em
# seguida, mostre o nome dos alunos com a maior e a menor nota.

alunos = []
notas = []
alunos_organizados = []

for index in range(5):
    nome_aluno = input(f'Digite o nome do {index + 1}º aluno: ')
    alunos.append(nome_aluno)

for index in range(5):
    nota_aluno = float(input(f'Digite a nota de {alunos[index]}: '))
    notas.append(nota_aluno)

notas_organizadas = sorted(notas, reverse=True)

for nota in notas_organizadas:
    for index in range(len(notas)):
        if nota == notas[index]:
            alunos_organizados.append(alunos[index])
            alunos.pop(index)
            notas.pop(index)
            break


print(f'\nAlunos: {alunos_organizados}\nNotas:  {notas_organizadas}')
