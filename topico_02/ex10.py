# Crie um programa para uma empresa de energia que cobra tarifas
# progressivas com base no consumo mensal em kWh, de acordo com a
# seguinte tabela:
#  Até 50 kWh: R$ 0,30 por kWh
#  De 51 a 150 kWh: R$ 0,40 por kWh
#  De 151 a 300 kWh: R$ 0,50 por kWh
#  Acima de 300 kWh: R$ 0,70 por kWh
# O programa deverá receber a quantidade de kWh e mostrar o valor total
# a ser pago pelo cliente.

consumo = float(input('Digite o seu consumo de kWh: '))

if consumo <= 50:
    tarifa = 0.3
elif consumo <= 150:
    tarifa = 0.4
elif consumo <= 300:
    tarifa = 0.5
elif consumo > 300:
    tarifa = 0.7

preco = consumo * tarifa

print(f'O valor a ser pago é R${preco:.2f}')