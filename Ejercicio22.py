def usar_la_fuerza(mochila, indice):
  
    if indice >= len(mochila):
        return False, 0

    objeto_actual = mochila[indice]

    if objeto_actual == "sable de luz":
        return True, 1
    encontrado, cantidad = usar_la_fuerza(mochila, indice + 1)

    if encontrado:
        return True, cantidad + 1
    else:
        return False, 0

mochila_luke = ["comida", "binoculares", "mapa", "sable de luz", "capa", "linterna"]

lo_tiene, cuantos_saco = usar_la_fuerza(mochila_luke, 0)


if lo_tiene:
    print("¡Luke encontró su sable de luz!")
    print("Tuvo que sacar", cuantos_saco, "objetos para encontrarlo.")
else:
    print("El sable de luz no estaba en la mochila.")