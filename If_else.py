name = input("Digite o nome do game\n")
yearLaunch = int(input("digite o ano do jogo\n"))
classification = float(input("ditie a nota da classificação do game"))

if classification > 8 or yearLaunch > 2015:  #se uma das condiçoes for verdedeira pode ser and para testar as duas
    print(F"pode jogar o jogo {name}! vai na fé! ")
else:
    print(f"O jogo {name} ainda está com nota baixa, nem jogue") 

