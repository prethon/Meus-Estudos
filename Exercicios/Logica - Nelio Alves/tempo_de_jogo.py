horaInicial = int(input())
horaFinal = int(input())

if horaFinal > horaInicial:
    horas = horaFinal - horaInicial
else:
    horas = (24 - horaInicial) + horaFinal

print(f"O JOGO DUROU {horas} HORAS(S)")