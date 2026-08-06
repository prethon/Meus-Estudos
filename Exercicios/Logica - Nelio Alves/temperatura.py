escalaTemp = input("Voce vai digitar a temperatura em qual escala (C/F)? ").upper

if escalaTemp == "F":
    tempF = float(input("Digite a temperatura em Fahrenheit: "))
    TempC = (5 / 9) * (tempF - 32)
    print(f"Temperatura equivalente em Celsius: {TempC:.2f}")
else:
    TempC = float(input("Digite a temperatura em Celsius: "))
    tempF = (TempC * 1.8) + 32
    print(f"Temperatura equivalente em Fahrenheit: {tempF:.2f}")