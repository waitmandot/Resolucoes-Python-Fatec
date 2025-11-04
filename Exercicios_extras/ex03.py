# ================================================
# DESAFIO 3 – ESTRUTURAS DE DADOS
# -----------------------------------------------
# Peça ao usuário que digite o nome e a nota de 5 alunos.
# - Armazene os dados em um dicionário, onde a chave é o nome e o valor é a nota.
# - Depois, exiba:
#   - A média da turma;
#   - Os nomes dos alunos acima da média;
#   - Um conjunto com todas as notas únicas (sem repetição).
# ================================================

media = 0
notas = []
dados_alunos = {}
for n in range (1, 6):
    aluno = input(f"Digite o nome do aluno {n}: ")
    nota = float(input(f"Digite a nota do aluno {n}: "))
    dado_aluno = {aluno: nota}
    dados_alunos.update(dado_aluno)
    media += nota

media = media / 5

print(f"A média da turma foi {media}\nAlunos acima da media:")

for key, value in dados_alunos.items():
    if value > media:
        print(key)
    notas.append(value)

print("Todas as notas sem repetições:")

print(set(notas))