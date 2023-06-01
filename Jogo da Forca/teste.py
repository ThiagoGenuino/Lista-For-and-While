import random
import re
import PySimpleGUI as sg

lista_palavras = ('avestruz', 'cavalo')

def palavra_escolhida(lista):
    secreta = random.choice(lista)
    return secreta

def lugar_certo(palavra_certa, letra):
    posicao = []
    for n in range(0, len(palavra_certa)):
        if palavra_certa[n] == letra:
            posicao.append(n)
    return posicao

palavra = palavra_escolhida(lista_palavras)
palavra_montada = list('_' * len(palavra))
tentativas = 0

layout = [
    [sg.Text('A palavra tem {} letras'.format(len(palavra)))],
    [sg.Text('Palavra: '), sg.Text(' '.join(palavra_montada), key='palavra')],
    [sg.Text('Digite uma letra: '), sg.Input(key='letra')],
    [sg.Button('Enviar')],
    [sg.Text('', key='resultado')]
]

window = sg.Window('Jogo da Forca', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Enviar':
        letra = values['letra'].lower()
        if re.match(r'^[a-zA-ZáéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ]+$', letra):
            if letra in palavra:
                localizacao = lugar_certo(palavra, letra)
                for n in localizacao:
                    palavra_montada[n] = letra
                window['palavra'].update(' '.join(palavra_montada))
                if '_' not in palavra_montada:
                    sg.popup('Parabéns! Você venceu!')
                    break
            else:
                tentativas += 1
                if tentativas >= 6:
                    window['resultado'].update('Você perdeu. A palavra correta era {}'.format(palavra))
                    break
        else:
            sg.popup('Digite apenas letras.')
    
window.close()