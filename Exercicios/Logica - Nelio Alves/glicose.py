glicose = float(input())

if glicose <= 100.00:
    print("Classificacao: normal")
elif glicose > 100.00 and glicose <= 140.00:
    print("Classificacao: elevado")
else:
    print("Classificacao: diabetes")
