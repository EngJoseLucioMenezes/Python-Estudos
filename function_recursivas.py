###Fatorial de um numero:
###3 -> 3*2*1
###5 -> 5*4*3*2*1


def factorial(num):
    if num ==1:
        return 1
    else:
        return (num * factorial(num -1))


number = int(input("digite o numero para o fatoria"))
print (f"o fatorial do {number} é: {factorial (number)}")

