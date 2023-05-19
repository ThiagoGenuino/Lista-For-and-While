"""Dado um limite inferior e superior, elabore um programa que calcule a soma de todos os
números pares contidos neste intervalo."""

import re
inferior = (input("Digite o limite inferior: "))
superior = (input("Digite o limite superior "))
if re.match(r'^\d+$',inferior) and re.match(r'^\d+$',superior):
    inferior, superior = int(inferior),int(superior)
    soma_pares = 0
    for i in range(inferior, superior + 1 ):
        if i % 2 == 0:
            soma_pares += i
    print('a soma final é {}'.format(soma_pares))

else:
    print('digite numeros inteiros')