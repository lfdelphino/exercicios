# -*- coding: utf-8 -*-
alunos = []


def MediaTurma(alunos):
    somaAltura = 0
    for aluno in alunos:
        somaAltura += aluno[1]
    return somaAltura / len(alunos)

	
def Conta_Baixinhos(alunos, media):
    total = 0
    for aluno in alunos:
        if aluno[0] > 13 and aluno[1] < media:
            total += 1
    return total

	
while True:
    aluno = []
    quantidadeAtual = len(alunos) + 1
    idade = input("Digite a idade do {} aluno: ".format(quantidadeAtual))
    aluno.append(idade)
    altura = input("Digite a altura do {} aluno em cm: ".format(quantidadeAtual))
    aluno.append(altura)
    alunos.append(aluno)
    media = MediaTurma(alunos)
    print("*****************************************\n")
    print("A media de altura da turma e: {}cm\n".format(media))
    print("Existe(m) {} alunos com mais de 13 anos abaixo da media\n".format(Conta_Baixinhos(alunos, media)))
    print("*****************************************")