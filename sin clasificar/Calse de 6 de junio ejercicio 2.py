Año_de_Nacimiento = int(input("¿En que año naciste?"))

if Año_de_Nacimiento >1920 and Año_de_Nacimiento <1940:
    print ("tu generacion es: La Generacion Silenciosa")
elif Año_de_Nacimiento >=1946 and Año_de_Nacimiento <= 1964:
    print("tu generacion es: Baby Boomer")
elif Año_de_Nacimiento <=1979:
    print("tu generacion es:  X")
elif Año_de_Nacimiento <=2000:
    print("tu generacion es:  y")
elif Año_de_Nacimiento <=2010:
    print("tu generacion es:  z")
else:
    print("No existe genreacion asociada")


