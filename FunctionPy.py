# def cadastrar_produto():
#     produto= input("digite o nome do produto que deseja cadastrar")
#     produto = produto.casefold()
#     produto = produto.strip()
#     print(f'produto {produto} foi cadastrado')
#     return produto

# cadastrar_produto()

# Var_produto = cadastrar_produto()
# print (Var_produto)


# #### Argumentos/Paramentros da funcao
# def minha_soma(num1, num2, num3):
#     return num1 + num2 + num3

# soma = minha_soma(10, 20, 0)
# print (soma)


# #fun soma 
# def sum():
#     return 5 + 4

# sum()

# print(sum())

# #print de cadastro

def nota_game():
    gameName = input("digite o nome do jogo\n")
    gameRating = int(input("digite quantas avaliacoes deseja fazer no game\n"))
    sum = 0
    for i in range(gameRating):
        note = float(input("digite a nota para o jogo \n"))
        sum += note
    print(f"media de avaliacao do jogo {gameName} é {sum/gameRating}")

nota_game()
