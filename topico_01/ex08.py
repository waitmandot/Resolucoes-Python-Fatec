# Peça para o usuário digitar o seu ano de nascimento. O programa deve calcular
# e mostrar a idade atual dele, considerando que o ano atual é 2025

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano = 2025

idade = ano - ano_nascimento

print(f'Considerando que estamos em {ano}, você tem {idade} anos')