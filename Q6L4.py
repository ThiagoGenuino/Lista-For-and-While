"""Elabore um programa que realize a operação de potenciação de dois números inteiros e
positivos apenas utilizando a operação de soma."""
import re
base = (input("Digite o numero: "))
potencia = (input("Digite a potencia "))
if re.match(r'^\d+$',base) and re.match(r'^\d+$',potencia):
    base, potencia = int(base), int(potencia)
    if base >= 0 and potencia >= 0:
        valor = base
        if potencia == 0:
            valor = 1
        else:    
            for i in range(potencia - 1):
                temp = valor
                for i in range(base - 1):
                    valor += temp
            
            
        print('a potenciação é {}'.format(valor))    
    else:
        print('digite numeros positivos e inteiros')
else:
    print('digite numeros inteiros')
