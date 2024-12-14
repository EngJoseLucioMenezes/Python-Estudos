"""Exercicio
Contagem Regressiva
Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
o programa deve imprimir 10, 9 , 8 .... 1, 0 e diparar um "beep"


Exercicio 2

Faca um programa que calcule a tabuada de um numero, com valores iniciais e finais informados pelo usuario
"""
# #lancamento do fogueteXD
# import winsound
# x = 10
# while x >= 0:
#     print(x)
#     x -= 1# x = x -1
# winsound.Beep(2500,500)


#tabuada de umero
number = int(input("tabuada de : \n"))
begin = int (input("De: \n"))
end = int(input("Até: \n"))

x = begin

while x <= end:
    print(f"tabuada de {number} x {x} = {number * x}")
    x = x + 1