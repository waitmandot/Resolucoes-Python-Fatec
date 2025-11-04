# Dada uma lista de números inteiros, 
# imprima todos os elementos distintos.

lista_numeros = []

for index in range(5):
    numero = int(input(f"Digite o {index + 1}º número: "))

    lista_numeros.append(numero)

conjunto_numeros = set(lista_numeros)

print(conjunto_numeros)
