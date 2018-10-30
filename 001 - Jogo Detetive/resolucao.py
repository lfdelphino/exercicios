# -*- coding: utf-8 -*-

jogando = True
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?",
             "Já trabalhou com a vítima?"]


def julgamento(culpado):
    if culpado == 2:
        return "Suspeito(a)"
    elif culpado == 3 or culpado == 4:
        return "Cúmplice"
    elif culpado == 5:
        return "Assassino"
    else:
        return "Inocente"


while jogando:
    culpado = 0
    for pergunta in perguntas:
        resposta = input(' '.join([pergunta, "(Y/n)"]))
        if "y" in resposta.lower():
            culpado += 1

    fim = input("Você é {}!\nDeseja recomeçar? (Y/n)".format(julgamento(culpado)))
    if "n" in fim.lower():
        jogando = False