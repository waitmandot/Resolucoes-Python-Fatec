# Faça um program que leia o ano de nascimento de uma
# pessoa e informe se ele ainda vai se alistar ao serviço 
# militar ou se ele está no período de se alistar ou se 
# ele perdeu o prazo para se alistar. Além disso, mostre 
# também a quantidade de anos que falta para se alistar 
# ou que passou do prazo.

ANO_ATUAL = 2025

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

idade = ANO_ATUAL - ano_nascimento

if idade == 18:
    print("Você precisa se alistar")
elif idade < 18:
    print(f"Você ainda não pode se alistar. Falta {18 - idade} anos.")
else:
    print(f"Você perdeu o prazo de alistamento em {abs(18 - idade)} anos.")