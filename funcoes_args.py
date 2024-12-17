# @args - Os argumentos não temos certeza de quantos argumentos queremos ter em uma função 
# os argumentos são passados como uma tuplas

# Kwargs - alem dos valores podemos passar tambem as recpecitava chaves como os argumentos, 
# os argumentos sao passados com um dicinario

def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n # sum_total = sum total +n
    print(f"soma é {sum_total}")


sum(7,9)
sum(3,8,9,11,85)


# @ 2 Apresentação de cursos

def presentation_curse (**data):
    for key, value in  data.items():
        print(f"{key} - {value}")


presentation_curse(name="python", category = "backend", level = "iniciante")
presentation_curse(name = "visão computacional", category = "avancade")