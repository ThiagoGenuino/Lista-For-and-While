"""Elabore um programa que apresente o resultado da multiplicação de dois números inteiros
apenas utilizado a operação de soma."""

import re

primeiro_n = (input("Digite o numero 1: "))
segundo_n = (input("Digite o numero 2: "))
multi = 0
if re.match(r'^\d+$',primeiro_n) and re.match(r'^\d+$',segundo_n):
    primeiro_n, segundo_n = int(primeiro_n), int(segundo_n)
    for i in range(segundo_n):
        multi += primeiro_n 


    print('a multiplicação é {}'.format(multi))
else:
    print('digite numeros inteiros')

