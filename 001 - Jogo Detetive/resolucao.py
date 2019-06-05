# -*- coding: utf-8 -*-

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?",
             "Já trabalhou com a vítima?"]
julgamento = ["Inocente", "Inocente", "Suspeito(a)", "Cúmplice", "Cúmplice", "Assassino"]


while perguntas:
    culpado = 0
    for pergunta in perguntas:
        resposta = input(' '.join([pergunta, "(Y/n)"]))
        if "y" in resposta.lower():
            culpado += 1

    fim = input("Você é {}!\nDeseja recomeçar? (Y/n)".format(julgamento[culpado]))
    if "n" in fim.lower():
        perguntas = False
