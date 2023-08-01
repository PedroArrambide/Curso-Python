import datetime 
fecha_actual = datetime.datetime.now()
fecha_de_nacimiento_str = input("ingresa tu fecah de cumpleaños dd/mm/yyyy: ")
fecha_de_nacimiento = datetime.datetime.strptime(fecha_de_nacimiento_str,"%d/%m/%Y")
edad = fecha_actual.year - fecha_de_nacimiento.year

print(edad)

fecha_de_cumpleanos = datetime.datetime(fecha_actual.year, fecha_de_nacimiento.month, fecha_de_nacimiento.day)

if fecha_actual > fecha_de_cumpleanos:
    fecha_de_cumpleanos = datetime.datetime(fecha_actual.year+1, fecha_de_nacimiento.month, fecha_de_nacimiento.day)
diferencia = fecha_de_cumpleanos - fecha_actual
segundos_faltantes = diferencia.total_seconds()

print("faltan",int(segundos_faltantes)," Segundos para tu proximo cumpleaños")