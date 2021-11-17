segundos = input("Entre com o número de segundos:")
segundos = int(segundos)

dias = segundos // (24*3600)
segundos_res1 = segundos % (24*3600)
horas = segundos_res1 // 3600
segundos_res2 = segundos_res1 % 3600
minutos = segundos_res2 // 60
segundos_fin = segundos_res2 % 60

print("Equivale a", dias, "dias e", horas, "horas e", minutos, "minutos e", segundos_fin, "segundos")
