#tabuada de umero
Numero1 = int(input("tabuada de : \n"))
Numero2 = int (input("De: \n"))
FinalTabu = int(input("Até: \n"))

ValorNumero2 = Numero2

while ValorNumero2 <= FinalTabu:
    print(f"tabuada de {Numero1} x {ValorNumero2} = {Numero1 * ValorNumero2}")
    ValorNumero2 = ValorNumero2 + 11