"""Elabore um programa que solicite 6 números inteiros e calcule a soma dos que forem pares
e dos que forem ímpares e apresente na tela."""

import re
pares = 0
impares = 0
a = 0

for indice in range(6):
    n = (input("Digite um número inteiro: "))
    if re.match(r'^\d+$',n):
        n = int(n)
        if n % 2 == 0:
            pares += n
        else:
            impares += n
    else:
        ('digite numeros inteiros')
        a = 1
        break
        
if a == 1:
    print('digite numeros inteiros')
    
else:
    print("A soma dos números pares é:", pares)
    print("A soma dos números ímpares é:", impares)