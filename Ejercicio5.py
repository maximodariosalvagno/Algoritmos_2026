def pasar_a_decimal(texto_romano, posicion):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }

    if posicion >= len(texto_romano):
        return 0

    if posicion == len(texto_romano) - 1:
        return valores[texto_romano[posicion]]


    actual = valores[texto_romano[posicion]]
    siguiente = valores[texto_romano[posicion + 1]]

    if actual < siguiente:
        return (siguiente - actual) + pasar_a_decimal(texto_romano, posicion + 2)
    
    else:
        return actual + pasar_a_decimal(texto_romano, posicion + 1)

romano_elegido = input('Escribi el numero romano en mayúsculas que deseas pasar a decimal (ej: XIV): ')

rta = pasar_a_decimal(romano_elegido, 0)

print("El resultado es:", rta)