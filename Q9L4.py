"""Elabore um programa que solicite o peso de cinco pessoas e informe o maior e o menor
peso lido."""
import re
maior = 0
menor = float("inf")
for i in range(1,5 + 1):
    peso = (input("Digite o peso da uma pessoa {} ".format(i)))
    if re.match(r'^\d*\.?\d+$',peso):
        peso = int(peso)
        if peso > maior:
            maior = peso
           
        if peso <= menor:
            menor = peso
    else:
        print('digite numeros positivos')    

print('maior peso é {} e o menor peso é {}'.format(maior,menor))  