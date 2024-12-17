def check_caracter(text):
    type = {"Uppercase": 0, "Lowercase":0}
    for char in text:
        if char.isupper():
            type["Uppercase"] +=1
        elif char.islower():
            type["Lowercase"] += 1
    print("text original :", text)
    