from collections import deque

 
superheroes_simple = [
    "Spider-Man", "Iron Man", "Thor", "Hulk", "Captain America",
    "Black Widow", "Hawkeye", "Wolverine", "Cyclops", "Storm",
    "Deadpool", "Daredevil", "Black Panther", "Vision", "Scarlet Witch"
]
 
def buscar_capitan_america(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Captain America":
        return True
    return buscar_capitan_america(lista, indice + 1)
 
def listar_heroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(f"  - {lista[indice]}")
    listar_heroes(lista, indice + 1)
 
print("=" * 50)
print("EJERCICIO 1")
print("=" * 50)
 
print("\nListado de superhéroes (recursivo):")
listar_heroes(superheroes_simple)
 
encontrado = buscar_capitan_america(superheroes_simple)
if encontrado:
    print("\nCaptain America SÍ está en la lista.")
else:
    print("\nCaptain America NO está en la lista.")
