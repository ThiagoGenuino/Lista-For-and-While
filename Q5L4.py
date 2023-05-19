"""Elabore um programa que realize a operação de potenciação de dois números inteiros e
positivos apenas utilizando a operação de multiplicação."""
import re
primeiro_n = (input("Digite o numero: "))
potencia = (input("Digite a potencia "))
multi = 1
if re.match(r'^\d+$',primeiro_n) and re.match(r'^\d+$',potencia):
    primeiro_n, potencia = int(primeiro_n), int(potencia)

    if primeiro_n >= 0 and potencia >= 0: 
        for i in range(potencia):
            multi *= primeiro_n 
        print('a potenciação é {}'.format(multi))
    else:
        print('digite numeros positivos e inteiros')
else:
    print('digite numeros inteiros')