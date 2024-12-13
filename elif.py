num1 = float(input("digite o numero 1 : \n"))
num2 = float(input("digite o numero 2 : \n"))
operation = input ("digite a operação a ser realida (+ - * / ): \n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("operação invalida")
    result = 0

print(f"Resultado é:{result}")

### pode ser realizado com a func Def################

def calcular(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else:
        return None

num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação a ser realizada (+ - * / ): ")

resultado = calcular(num1, num2, operacao)

if resultado is not None:
    print(f"Resultado é: {resultado}")
else:
    print("Operação inválida")
