"""O número 3025 possui a seguinte característica: 30 + 25 = 55 e 55^2 =3025. Faça um
programa que encontre os números > 0 e < 10000, que apresentam tal característica."""
import math as m
for n in range(10000):
    carac1 = (n // 100) # separa o 30 do exemplo, retirando o resto
    carac2 = (n % 100)  # separa o 25 do exemplo, pegando o resto
    soma = carac1 + carac2
    quadradodasoma = m.pow(soma,2)
    if quadradodasoma == n:
        print('os numeros com esse tipo sde caracteristicas são {}'.format(n)) 
