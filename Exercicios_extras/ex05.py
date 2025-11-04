# ===================================================
# MINI DESAFIO: ANÁLISE DE TEXTO
# ---------------------------------------------------
#
# Peça ao usuário um texto (pode ser uma frase ou parágrafo curto).
#
# Tarefas:
# 1) Transforme o texto em minúsculas e separe em palavras (split()).
# 2) Mostre:
#    - Quantas palavras há no total.
#    - Quantas são únicas (use set()).
# 3) Mostre a palavra mais longa e seu tamanho.
# 4) Crie uma lista com as palavras que começam com vogal.
# 5) Mostre o texto com as palavras invertidas (mantendo a ordem das palavras).
#
# BÔNUS (opcional):
# - Peça ao usuário uma palavra e diga quantas vezes ela aparece no texto.
# ===================================================

vogais = ["a", "e", "i", "o", "u"]
maior_palavra = ""
palavras_vogais = []
texto_invertido = []
texto = input("Escreva um texto: ")

texto = texto.lower()
texto = texto.split()

print(f"O texto tem {len(texto)} palavras")
print(f"O texto tem {len(set(texto))} palavras únicas")

for word in texto:
    if len(word) > len(maior_palavra):
        maior_palavra = word

print(f"A maior palavra é '{maior_palavra}' com {len(maior_palavra)} letras")

for word in texto:
    palavra_decomposta = list(word)
    if palavra_decomposta[0] in vogais:
        palavras_vogais.append(word)

print(f"As palavras que começam com vogais são:\n{palavras_vogais}")

for word in texto:
    texto_invertido.append(word)

for index, word in enumerate(texto_invertido):
    word_invertida = word[::-1]
    texto_invertido[index] = word_invertida

texto_invertido = " ".join(texto_invertido)

print(f"Esse é o texto invertido:\n'{texto_invertido}'")

while True:
    palavra = input("Digite uma palavra do seu texto: ")
    palavra = palavra.lower()
    vezes = texto.count(palavra)

    print(f"A palavra '{palavra}' aparece {vezes} vezes no seu texto.")