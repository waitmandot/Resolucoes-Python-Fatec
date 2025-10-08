# Faça um programa em que o usuário deverá digitar
# os nomes de dez alunos da sala de aula. Em seguida,
# caso o programa encontre nomes repetidos, ele deverá
# alterar o nome adicionando o número sequencial. Por
# exemplo, se na lista tivermos dois "José", após o
# processamento a lista deverá conter "José 1" e "José 2".

alunos = ["Lucas", "Maria", "João", "Ana", "Pedro", "Lucas", "Carla", "João", "Ana", "Ana"]
alunos_final = []

for aluno in alunos:
    total = 0
    for x in alunos:
        if x == aluno:
            total = total + 1

    if total == 1:
        alunos_final.append(aluno)
    else:
        ocorrencias = 0
        for anterior in alunos_final:
            if len(anterior) >= len(aluno):
                if anterior[:len(aluno)] == aluno:
                    if len(anterior) == len(aluno) or anterior[len(aluno)] == " ":
                        ocorrencias = ocorrencias + 1

        alunos_final.append(aluno + " " + str(ocorrencias + 1))

print(alunos_final)
