# -*- coding: utf-8 -*-

letras = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def traduzir(frase):
    nova_frase = []
    frase_lista = frase.split(',')
    for letra in frase_lista:
        nova_frase.append(letras[int(letra)])
    return ''.join(nova_frase)

	
while True:
    frase = raw_input("Digite a mensagem codificada:\n")
    print(traduzir(frase))