print("Digite as idades:")
soma = 0
contador = 0
a = int(input())


while a >= 0:
    contador += 1
    soma += a
    a = int(input())

if contador == 0:
    print("IMPOSSIVEL CALCULAR")
else:
    media = soma / contador
    print(f"MEDIA = {media:.2f}")

