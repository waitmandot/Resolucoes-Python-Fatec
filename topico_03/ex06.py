# Você recebe uma string e sua tarefa é trocar casos. 
# Em outras palavras, converta todas as letras minúsculas
# em maiúsculas e vice-versa.
# Input: Fatec Rio Preto
# Output: fATEC rIO pRETO

texto = input('Digite uma string: ')

for letra in texto:
    if letra != letra.upper():
        letra = letra.upper()
    else:
        letra = letra.lower()
    print(letra, end='')