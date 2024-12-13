## calculo de distancia por valor

distance = float(input("Digite a distancia a percorrer "))
if distance <= 200:
    tickt = 0.5 * distance
else:
    tickt = 0.35 * distance
print(f"Preço da passagem é {tickt:.2f}")

