precoProd = float(input("Preço unitário do produto: "))
qtdComprada = int(input("Quantidade comprada: "))
dinheiroRec = float(input("Dinheiro recebido: "))

troco = dinheiroRec - (precoProd * qtdComprada)

print(f"TROCO = {troco:.2f}")