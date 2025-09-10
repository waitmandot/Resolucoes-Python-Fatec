# Faça um programa para aprovar o empréstimo bancário para
# a compra de uma casa. O usuário deverá informar o valor
# da casa, a quantidade de parcelas que deseja pagar e seu
# salário. O empréstimo deverá ser negado caso o valor da
# parcela exceda 30% do salário.

valor_casa = float(input('Digite o valor do imóvel: '))
qntd_parcelas = int(input('Digite a quantidade de parcelas: '))
salario = float(input('Digite o valor do seu salário: '))

valor_parcelas = valor_casa / qntd_parcelas

if valor_parcelas > salario * 0.30:
    print('Você não pode fazer o financeamento!')
else:
    print('Você pode fazer o financeamento')