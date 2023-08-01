edad = int(input("edad?"))
antiguedad = int(input("¿antiguedad en el sistema finaciero?"))
ingreso = float(input("Ingresos?"))

if (edad >= 18 and antiguedad >3 and ingreso >2500) or  ( edad > 18 and ingreso >= 4000):
    print("se aprueba el credito")
else:
    print("No se aprueba el credito")