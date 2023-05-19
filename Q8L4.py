"""Elabore um programa que solicite um número inteiro e verifique se ele é primo ou não."""

import re
numero = (input("Digite o numero: "))
if re.match(r'^\d+$',numero):
    numero = int(numero)
    if numero > 1:
        c = 2
        while c < numero:
            if numero %  c == 0:
                print('numero não é primo')
                break
            c += 1 
        else:
            print('é primo')
    else:
        print('digite numeros positivos e diferentes de 0')
else:
    print('digite numeros inteiros')
