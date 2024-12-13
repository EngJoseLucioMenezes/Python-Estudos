gameName = input("digite o nome do jogo\n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0

while(rating!= -1):
    rating = float(input("informe a nota do jogo \n"))
    if(rating != -1):
        totalRating += rating #totalRating = TotalRating + rating
        qtdRating += 1 #qtdRating = qtdrating +1
        average = totalRating / qtdRating
print(f"Media das avaliaçoes do jogo {gameName} é {average:.2f}")

