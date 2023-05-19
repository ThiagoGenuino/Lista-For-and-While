"""Elabore um programa que solicite um número natural e apresente o fatorial deste
número. (sem usar a função math.factorial)"""

import re
natural =  input('digite um numero natural \n')
n = 1
if re.match(r'[+]?^\d+$',natural):
    natural = int(natural)
    for i in range(1,natural + 1):
        n *= i
    
print(n)