# Uma técnica muito comum para apresentar uma Word Cloud é
# contar a frequência de palavras em um texto para destacar
# a fonte de cada palavra. Para isso, crie um programa que
# leia uma string, por exemplo "Python é incrível e Python
# é simples", e retorne o dicionário: {'Python': 2, 'é': 2,
# 'e': 1, 'incrível': 1, 'simples': 1}.

input = input('Digite uma frase: ').lower()

dicionario = {}

frase = input.split()

for palavra in frase:
    quantidade = frase.count(palavra)
    nova_palavra = {palavra : quantidade}
    dicionario.update(nova_palavra)

print(dicionario)