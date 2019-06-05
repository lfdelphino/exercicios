# -*- coding: utf-8 -*-

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
julgamento = ["Inocente", "Inocente", "Suspeito(a)", "Cúmplice", "Cúmplice", "Assassino"]

while perguntas:
	culpado = 0
	for pergunta in perguntas.lower():
		resposta = str(input(' '.join([pergunta, "(S/n) "])))
		if "s" in resposta.lower():
			culpado += 1

	fim = str(input("Você é {}!\nDeseja recomeçar? (Y/n)".format(julgamento[culpado])))
	perguntas = False if "n" in fim.lower() else perguntas
