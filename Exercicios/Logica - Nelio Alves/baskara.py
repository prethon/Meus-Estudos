import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente b: "))

delta = b**2 - 4 * a * c

if a == 0:
    print("O coeficiente 'a' deve ser diferente de zero.")
elif delta < 0:
    print("A equação não possui raízes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")