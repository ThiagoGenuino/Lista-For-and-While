import re
idade_todos = 0
idade_mulheres = 0
idade_homens = 0
qtd_mulheres = 0
qtd_homens = 0

for i in range(7):
    idade = int(input('Digite a idade da pessoa {}: '.format(i+1)))
    sexo = input('Digite o sexo da pessoa {} "m" para homem e "f" para mulher: '.format(i+1))
    if re.match(r'[+]?^\d+$',idade) and re.match(r'^[a-zA-ZáéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ]+$',sexo):
        idade = int(idade)
        sexo = str(sexo)
        if sexo.lower() == 'm':
            idade_homens += idade
            qtd_homens += 1
        elif sexo.lower() == 'f':
            idade_mulheres += idade
            qtd_mulheres += 1
        else:
            print('Sexo inválido, Digite "m" para masculino ou "f" para feminino.')
        idade_todos += idade
    else:
        print('digite valores validos')    

media_grupo = idade_todos / 7
if qtd_mulheres > 0:
    media_mulheres = idade_mulheres / qtd_mulheres 
else:
    media_mulheres = 0
if qtd_homens:
    media_homens = idade_homens / qtd_homens  
else:
    media_homens = 0

# Exibindo os resultados
print('Média de idade do grupo: {:.2f}'.format(media_grupo))
print('Média de idade das mulheres: {:.2f}'.format(media_mulheres))
print('Média de idade dos homens: {:.2f}'.format(media_homens))