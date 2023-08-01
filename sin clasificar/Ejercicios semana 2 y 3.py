ganadores = {
    1990: "Alemania",
    1994: "Brasil",
    1998: "Francia",
    2002: "Brasil",
    2006: "Italia",
    2010: "España",
    2014: "Alemania",
    2018: "Francia"
}

agno = int(input("Coloque el año que quiere saber quien fue el gandor de la compa del mundo: "))
ganador = ganadores.get(agno)

print(f"El ganador de la Copa Mundial de la FIFA en {agno} fue {ganador}")