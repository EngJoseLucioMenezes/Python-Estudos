salary = float(input("Salario do funcionario"))
perc_incease = 0.15

if salary > 1250:
    perc_incease = 0.10
incresase = salary * perc_incease
print(f"seu novo aumento é {incresase:.2f}")
