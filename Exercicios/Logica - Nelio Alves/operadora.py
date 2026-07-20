minutos = int(input())

valorPagar = 50.00

if minutos > 100:
    valorPagar = valorPagar + 2 * (minutos - 100)
else:
    valorPagar = valorPagar

print(f"Valor a pagar: R$ {valorPagar:.2f}")