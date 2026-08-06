codP = int(input("Codigo do produto comprado: "))
qtd = int(input("Quantidade comprada: "))

if codP == 1:
    print(f"Valor a pagar: R$ {5.00 * qtd:.2f}")
elif codP == 2:
    print(f"Valor a pagar: R$ {3.50 * qtd:.2f}")
elif codP == 3:
    print(f"Valor a pagar: R$ {4.80 * qtd:.2f}")
elif codP == 4:
    print(f"Valor a pagar: R$ {8.90 * qtd:.2f}")
elif codP == 5:
    print(f"Valor a pagar: R$ {7.32 * qtd:.2f}")