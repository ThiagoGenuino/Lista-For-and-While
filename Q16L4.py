import re

entrada = 0

while True:
    print('1 – Média aritmética')
    print('2 – Média ponderada')
    print('3 – Sair')
    entrada = input('digite uma opção do menu acima: ')

    if re.match(r'[+]?^\d+$',entrada):
        entrada = int(entrada)
        if entrada == 1:
            n1 = input('digite numero 1: ')
            n2 = input('digite numero 2: ')
            if re.match(r'^\d*\.?\d+$',n1) and re.match(r'^\d*\.?\d+$',n2):
                n1, n2 = float(n1), float(n2)
                media_aritmetica = (n1 +n2)/2
                print('a media é {}'.format(media_aritmetica))
            else:
                print('digite numeros positivos')
        elif entrada == 2:
            n1 = input('digite numero 1: ')
            n2 = input('digite numero 2: ')
            peso1 = input('digite peso 1: ')
            peso2 = input('digite peso 2: ')
            if re.match(r'^\d*\.?\d+$',n1) and re.match(r'^\d*\.?\d+$',n2) and re.match(r'^\d*\.?\d+$',peso1) and re.match(r'^\d*\.?\d+$',peso2):
                n1, n2, peso1 , peso2 = float(n1), float(n2) , float(peso1), float(peso2)
                media_ponderada = (n1+n2)/(peso1+peso2)
                print('a media é {}'.format(media_ponderada))
            else:
                print('digite numeros positivos')
                
        elif entrada == 3:
            print('menu encerrado, obrigado por utilizar')
            break
        else:
            print('invalido, digite uma opção do menu valida')
    else:
        print('digite numeros validos')
                
                        
