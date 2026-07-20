a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print(f"MENOR = {a}")
elif b < c:
    print(f"MENOR = {b}")
else:
    print(f"MENOR = {c}")