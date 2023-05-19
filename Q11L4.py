"""Elabore um programa que solicite um número natural e apresente a soma e a média de
todos os números menores ou iguais a ele."""

import re
natural =  input('digite um numero natural \n')
n = 0
if re.match(r'[+]?^\d+$',natural):
    natural = int(natural)
    for i in range(natural + 1):
        n += i
    media = n / i    
    print('a soma de todos os numeros {}'.format(n))
    print('a media de todos os numeros {}'.format(media))
else:
    print('digite numeros naturais')