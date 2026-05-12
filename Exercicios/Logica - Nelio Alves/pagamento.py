nome = input("Nome: ")
valorHora = float(input("Valor por hora: "))
horasTrab = int(input("Horas trabalhadas: "))

pagamento = valorHora * horasTrab

print(f"O pagamento para {nome} deve ser {pagamento:.2f}")