a = float(input())
b = float(input())
c = float(input())

if a > b and a > c:
    print(f"MAIOR DISTANCIA = {a:.2f}")
elif b > c:
    print(f"MAIOR DISTANCIA = {b:.2f}")
else:
    print(f"MAIOR DISTANCIA = {c:.2f}")