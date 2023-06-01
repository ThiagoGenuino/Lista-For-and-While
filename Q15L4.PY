import re

numeros = []
entrada = 1
while True:
    entrada = input('digite um numero:\n')
    if re.match(r'[+]?^\d+$',entrada):
        entrada = int(entrada)
        
        if entrada == 0:
            break
        else:
            numeros.append(entrada)
    else:
        print('digite numeros e positivos')
print('o maior numero é do conjunto é: {}'.format(max(numeros)))
print('o maior numero é do conjunto é: {}'.format(min(numeros)))