# crie uma funcao que recebe dois argumentos: o primeiro nome e o segundo nome

def full_name(Fname, lname):
    print(f"nome completo:{Fname}{lname}")

full_name("jose", "Neto")

#### Crieando função de conta

def sum(a, b):
    return a+ b
print(sum(10,50))

#avaliacao de jogo

def rating_game(qtdratiing):
    game_name = input("digite o nome do jogo \n")
    sum = 0
    for i in range(qtdratiing):
        note = float(input("digite a nota para o jogo\n"))
        sum += note ## sum = sum + note
        print(F'media de valiação de jogo {game_name} é : {sum/qtdratiing}')


rating = int(input("digite quantas avaliaçoes deseja realizar no jogo"))

rating_game(rating)
rating_game(rating)
rating_game(rating)