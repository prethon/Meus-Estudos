salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000.00:
    novoSalario = salario * 1.20
    print(f"Novo salario = R$ {novoSalario:.2f}")
    print(f"Aumento = R$ {novoSalario - salario:.2f}")
    print("Porcentagem = 20%")
elif salario > 1000.00 and salario <= 3000.00:
    novoSalario = salario * 1.15
    print(f"Novo salario = R$ {novoSalario:.2f}")
    print(f"Aumento = R$ {novoSalario - salario:.2f}")
    print("Porcentagem = 15%")
elif salario > 3000.00 and salario <= 8000.00:
    novoSalario = salario * 1.10
    print(f"Novo salario = R$ {novoSalario:.2f}")
    print(f"Aumento = R$ {novoSalario - salario:.2f}")
    print("Porcentagem = 10%")
else:
    novoSalario = salario * 1.05
    print(f"Novo salario = R$ {novoSalario:.2f}")
    print(f"Aumento = R$ {novoSalario - salario:.2f}")
    print("Porcentagem = 5%")