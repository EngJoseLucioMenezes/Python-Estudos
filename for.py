### laço de repeticao


gamesList  = ['Fifa','Dragon','Borut','lol','Cs']
## iterando valores da lista comun
for game in gamesList:
    print(game)

# Quando a condicao for atendida, o loop sera encerrado
for game in gamesList:
    if game == "lol":
        break
    print(game)


#quando a condiçao for atendida, o loop vai para a proxima iteracao

for game in gamesList:
    if game == "lol":
        continue
    print(game)

#Avaliacao do jogo

for i in range(5):
    print("Ola mundo")

gameName = input("digite o nome do jogo\n")
gameRating = int(input("digite quantas avaliacoes deseja fazer no game\n"))
sum = 0
for i in range(gameRating):
    note = float(input("digite a nota para o jogo \n"))
    sum += note
print(f"media de avaliacao do jogo {gameName} é {sum/gameRating}")

