larguraTerreno = float(input("Digite a largura do terreno: "))
comprimentoTerreno = float(input("Digite o comprimento do terreno: "))
valorMetroQuadrado = float(input("Digite o valor do metro quadrado: "))

areaTerreno = larguraTerreno * comprimentoTerreno
preco = areaTerreno * valorMetroQuadrado

print(f"Area do terreno = {areaTerreno:.2f}")
print(f"Preco do terreno = {preco:.2f}")