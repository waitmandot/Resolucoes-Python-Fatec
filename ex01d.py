# Faça um programa que leia o preço de um produto e mostre o valor com 5% de desconto.

PrecoAtual = int(input('Digite o valor atual do produto: '))

PrecoDesconto = PrecoAtual - PrecoAtual * 0.05

print(f'O valor do produto com desconto é R${PrecoDesconto}')