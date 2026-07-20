tempoGasto = int(input())
velocidadeMedia = int(input())

distanciaPerco = velocidadeMedia * tempoGasto
litrosNec = distanciaPerco / 12

print(f"{litrosNec:.3f}")