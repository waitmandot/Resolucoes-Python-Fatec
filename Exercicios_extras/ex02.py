# ================================================
# DESAFIO 2 – ESTRUTURAS CONDICIONAIS E REPETIÇÃO
# -----------------------------------------------
# Escreva um programa que leia a idade de várias pessoas
# (parando quando o usuário digitar um número negativo).
# Ao final, mostre:
# - Quantas pessoas têm menos de 18 anos;
# - Quantas têm entre 18 e 59 anos;
# - Quantas têm 60 ou mais.
# Dica: use while True e break quando o usuário digitar idade negativa.
# ================================================

menos18 = 0
entre18e59 = 0
maior60 = 0

while True:
    user = int(input("Digite a idade da pessoa (ou idade negativa para parar): "))

    if user < 0:
        break
    elif user < 18:
        menos18 += 1
    elif user < 60:
        entre18e59 += 1
    elif user >= 60:
        maior60 += 1
    else:
        continue

print(f"{menos18} pessoas tem menos de 18 anos\n{entre18e59} pessoas tem entre 18 e 59 anos\n{maior60} pessoas são maiores de 60 anos")