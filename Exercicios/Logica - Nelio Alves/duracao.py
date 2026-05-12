totalSegundos = int(input("Digite a duracao em segundos: "))

horas = totalSegundos // 3600
segundosRestantes = totalSegundos % 3600
minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print(f"{horas}:{minutos}:{segundos}")