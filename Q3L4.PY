"""Elabore um programa que solicite o primeiro termo e a razão de uma PA (Progressão
Aritmética) e apresente na tela os 10 primeiros termos."""

import re
primeirot = (input("Digite o primeiro termo da PA: "))
razao = (input("Digite a razão da PA: "))

if re.match(r'^\d+$',primeirot) and re.match(r'^\d+$',razao):
    for indice in range(10):
        primeirot = int(primeirot)
        razao = int(razao)
        termos = primeirot + (indice * razao)
        print(termos)
else:
    print('digite numeros inteiros')