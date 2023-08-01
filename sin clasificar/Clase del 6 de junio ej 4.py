nombre = input("¿Cual es tu nombre?")
marvel_o_Capcom = input("Cual prefieres: Marvel o Capcom?")


if (nombre[0] <"M" and  marvel_o_Capcom.capitalize() == "Marvel") or ( nombre[0]>"N" and marvel_o_Capcom.capitalize() == "Capcom"):
    print (" Tu grupo es el A")
else:
    print("Tu grupo es el B")

    