num1 = input("digite o numero 1 \n")
num2 = input("digite o numero 2 \n")
operacao = input(" digite a operacao  + - * / \n")

if operacao == '+':
    print(num1 + num2)
elif operacao == "-":
    print (num1 - num2)
elif operacao == "*":
    print (num1 * num2)
elif operacao == "/":
    print (num1 / num2)
else:
    print("operacao incorreta!")
