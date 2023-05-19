"""Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final informe a
média de idade do grupo, o nome do homem mais velho e quantas mulheres têm menos de 20
anos."""
import re
maiorn = 0
menorn = float("inf")
qtdmulheres = 0
idades = []  
for i in range(2):
    nome =  input('digite o nome \n')
    idade = input('digite a idade \n')
    sexo  = input('digite o sexo "M" ou "F" \n').upper()
    if re.match(r'[+]?^\d+$',idade) and re.match(r'^[a-zA-Záéíãõêô]+$', nome) and re.match(r'^[a-zA-Záéíãõêô]+$', sexo):
        idade = int(idade)
        idades.append(idade)
        sexo, nome = str(sexo), str(nome)
        if idade > maiorn and sexo == "M":
            nomev = nome 
        else:
            nome = ''
            print('digite "M" ou "F"')       
        if idade < 20 and sexo == 'F':
            qtdmulheres += 1  
        else:
            print('digite "M" ou "F"')  
    else:
        print('digite coisas validas')
        break

print(nomev)
media = sum(idades)/len(idades)  
print('a media é {}'.format(media))
if len(nomev) != 0:
    print('o nome do homem mais velha é'.format(nomev))
else:
    print('nao tem homem na lista')
print('a quantidade de mulheres com menos de 20 anos é {}'.format(qtdmulheres))    