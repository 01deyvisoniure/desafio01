hora1=15
minuto1=1
hora2=92
minuto2=8
hora_final=hora1+hora2
minuto_final=minuto2+minuto1
if hora_final>=12:
    hora_final=hora_final-(hora_final//12)*12
if minuto_final>=60:
    hora_final=hora_final+(minuto_final//60)
    minuto_final=minuto_final-(minuto_final//60*60)
    if minuto_final >=10:
        print(f"hora final= {hora_final}:{minuto_final}h")
    else:
        print(f"hora final= {hora_final}:0{minuto_final}")
else:
    if minuto_final >=10:
        print(f"hora final= {hora_final}:{minuto_final}")
    else:
        print(f"hora final= {hora_final}:0{minuto_final}")







