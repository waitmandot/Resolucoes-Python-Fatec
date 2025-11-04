# ================================================
# DESAFIO 1 – FUNDAMENTOS
# -----------------------------------------------
# Crie um programa que peça ao usuário dois números inteiros e exiba:
# - a soma, subtração, multiplicação e divisão entre eles;
# - se o primeiro número é maior, menor ou igual ao segundo.
# ==============================================

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado_soma = numero1 + numero2
resultado_sub = numero1 - numero2
resultado_multi = numero1 * numero2
resultado_divi = numero1 / numero2

print(f"{numero1} + {numero2} = {resultado_soma}\n{numero1} - {numero2} = {resultado_sub}\n{numero1} * {numero2} = {resultado_multi}\n{numero1} / {numero2} = {resultado_divi}")

if numero1 > numero2:
    print(f"O numero {numero1} é maior que {numero2}")
elif numero1 < numero2:
    print(f"O numero {numero1} é menor que {numero2}")
else:
    print(f"Os dois numeros são {numero1}, portanto iguais!")