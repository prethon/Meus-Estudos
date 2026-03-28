linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

maior_ab = (a + b + abs(a - b)) // 2
parcial = (maior_ab + c + abs(maior_ab - c)) // 2

if maior_ab > parcial:
    print(f"{maior_ab} eh o maior ")
else:
    print(f"{parcial} eh o maior")