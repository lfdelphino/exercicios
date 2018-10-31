signos = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]
familiares = []
 
while True:
    nascimento = input("Digite o ano de nascimento da {}º pessoa (XXXX): ".format((len(familiares) + 1)))
    if int(nascimento) > 0:
        familiares.append(nascimento)
    elif familiares and int(nascimento) == -1:
        for ordinal, nascimentoFamiliar in enumerate(familiares):
            print("{}º pessoa -> {} : {}"
                  .format(ordinal, nascimentoFamiliar, signos[int(nascimentoFamiliar) % 12]))
