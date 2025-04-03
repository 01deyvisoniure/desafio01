#o primeiro  horario recebe em 24h
hora_1=int(input("hora: "))
minuto_1=int(input("minnuto: "))

if minuto_1 == 60:
    hora_1= hora_1+1
    minuto_1=minuto_1-60
else:
    if minuto_1 > 60:
        hora_1 = hora_1 + 1
        minuto_1=minuto_1-60
print(f"{hora_1}:{minuto_1}")


