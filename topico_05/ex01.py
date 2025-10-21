# Uma tarefa comum em NLP é substituir palavras por
# sinônimos para simplificação de texto, padronização
# ou expansão semântica. Isso é útil em aplicações
# como geração de textos ou normalização de linguagem.
# Com base neste contexto, crie um programa em Python
# que receba como entrada uma frase e, com base no
# dicionário de sinônimos, onde a chave é uma palavra
# original e o valor é sua substituição, retorne a frase
# modificada com as substituições aplicadas.

sinonimos = {'estudante': 'aluno', 'feliz': 'contente', 'prova': 'exame'}

input = input("Digite uma frase: ")

output = input.split()

for index, palavra in enumerate(output):
    for key in sinonimos.keys():
        if palavra == key:
            output[index] = sinonimos.get(key)

output = " ".join(output)

print(output)

# Exemplo:
# Input: O estudante está feliz porque passou na prova 
# Output: O aluno está contente porque passou na exame