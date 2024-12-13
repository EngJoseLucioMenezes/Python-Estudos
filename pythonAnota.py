import pprint

gamesDict = {
    "resident evil 4":{
        "yearLaunch":2023,
        "classification":9.8,
        "genre": ["acao","aventura"]

    },
    "Mario":{
        "yearLaunch":2024,
        "classification":8,
        "genre": ["fantazia","aventura"]
        }
}

pp = pprint.PrettyPrinter(depth = 4)
pp.pprint (gamesDict)


#buscar informacao dentro do dicionario

print(gamesDict["Mario"]["genre"])

#adicionar novo item

gamesDict["Mario"]["players"] = 1
print(gamesDict['Mario'])

#Excluir dicionario
del gamesDict["resident evil 4"]
print(gamesDict)