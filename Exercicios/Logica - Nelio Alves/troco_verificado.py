precoUnitario = float(input())
qtd = int(input())
dinheiroRec = float(input())

if dinheiroRec < precoUnitario * qtd:
    print(f"DINHEIRO INSUFICIENTE. FALTAM {(precoUnitario * qtd) - dinheiroRec:.2f}")
else:
    print(f"TROCO = {dinheiroRec - (precoUnitario * qtd):.2f}")