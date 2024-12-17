# # liste valores de 0 a 10 que sejam menor do que 4
# for i in range(10):
#     if i <4:
#         print (i)

# listNumbers = [i for i in range(10) if i <4]
# print (listNumbers)


# For

GamesList = ["mario","dragonB", "luigis Mans", "Kirby"]
newList = []
for x in GamesList:
    if "a" in x:
        newList.append(x)
print(newList)



#list Comprehesion

newList = [x for x in GamesList if "a" in x]
print(newList)


# # jogos que eu zerei

# gamesFinished = [ x for x in GamesList if x != "Kirby"]
# # print(newList)


#for

# GamesList = ["mario", "dragonB", "luigis Mans", "Kirby"]
# gamesFinished = []
# for x in GamesList:
#     if x != "Kirby":
#         gamesFinished.append(x)
# print(gamesFinished)



# ## While
# GamesList = ["mario", "dragonB", "luigis Mans", "Kirby"]
# gamesFinished = []
# index = 0
# while index < len(GamesList):
#     if GamesList[index] != "Kirby":
#         gamesFinished.append(GamesList[index])
#     index += 1
# print(gamesFinished)






