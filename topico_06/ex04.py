# Dadas duas lista que são duplicadas uma da
# outra, exceto por um elemento, ou seja, um 
# elemento de uma das listas está faltando. 
# Mostre-o usando conjuntos.

lista1 = input("Digite a primeira lista: ")
lista2 = input("Digite a segunda lista: ")

lista1 = lista1.split()
lista2 = lista2.split()

diferentes = set(lista1) ^ set(lista2)


print(diferentes)