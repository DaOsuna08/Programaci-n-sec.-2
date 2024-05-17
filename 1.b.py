cf_1=float(input('Ingrese una calificación'))
if cf_1<0:
    print('Calificación inválida')
elif cf_1>100:
    print('Calificación inválida')
elif cf_1==100:
    print('Calificación perfecta')
elif cf_1>90 or cf_1==90:
    print('Exelente')
elif cf_1>70 or cf_1==70:
    print('Bueno')
elif cf_1>50 or cf_1==50:
    print('Suficiente')
else:
    print('Insuficiente')