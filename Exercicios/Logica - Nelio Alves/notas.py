n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

nfinal = n1 + n2
print(f"NOTA FINAL = {nfinal:.1f}")

if nfinal > 60.00:
    print("APROVADO!!!")
else:
    print("REPROVADO!!!")