# Peça ao usuário para informar o raio de um círculo e calcule a sua área. A fórmula da área do círculo é:
# 𝐴 = 𝜋 × 𝑟2
# Onde 𝑟 é o raio e 𝜋 é aproximadamente 3.14159.

import math

valor_pi = math.pi
raio = float(input('Digite o valor do raio do círculo em metros: '))

area = valor_pi * pow(raio, 2)

print(f'A área do círculo é {area :.2f} m2')