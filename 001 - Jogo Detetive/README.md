# Jogo Detetive
##### Python 3.7
Faça o programa (jogo de perguntas e respostas) abaixo:
Crie uma função que faça 5 perguntas para uma pessoa sobre um crime, armazene as respostas (sim ou não) em uma lista e retorne esta lista. As perguntas são:  
```
a) "Telefonou para a vítima?"  
b) "Esteve no local do crime?"  
c) "Mora perto da vítima?"  
d) "Devia para a vítima?"  
e) "Já trabalhou com a vítima?"
```
Crie uma função que receba a lista das respostas do usuário e, dependendo dos valores, ela retorna a classificação: se a pessoa responder positivamente a 2 questões ela deve ser classificada como `Suspeita`, entre 3 e 4 como `Cúmplice` e 5 como `Assassino`. Caso contrário, ele será classificado como `Inocente`.
O programa deve no final imprimir a classificação sobre a participação da pessoa no crime.
Ofereça o usuário a opção de repetir o jogo e, caso ele digite `Parar`, o programa deve ser encerrado.