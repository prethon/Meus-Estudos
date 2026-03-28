linha1 = input().split()
codigo_1 = int(linha1[0])
numero_pecas_1 = int(linha1[1])
valor_unitario_1 = float(linha1[2])

linha2 = input().split()
codigo_2 = int(linha2[0])
numero_pecas_2 = int(linha2[1])
valor_unitario_2 = float(linha2[2])

total = (numero_pecas_1 * valor_unitario_1) + (numero_pecas_2 * valor_unitario_2)

print(f"VALOR A PAGAR: R$ {total:.2f}")