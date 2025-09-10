# Faça um programa que leia um número inteiro
# N e mostre na tela os N primeiros números da 
# Sequência de Fibonacci.
# Por exemplo, N = 7
# Output: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

N = int(input('Digite o número da sequência de Fibonacci: '))
a, b = 0, 1
primeiro = True

while N > 0:
    if primeiro:
        print(a, end="")
        primeiro = False
    else:
        print(" ->", a, end="")
        
    a, b = b, a + b
    N -= 1

print()