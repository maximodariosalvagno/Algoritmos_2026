import sys
sys.path.insert(0, '/mnt/user-data/uploads')
from super_heroes_data import superheroes
 
print("\n" + "=" * 50)
print("EJERCICIO 2")
print(f"Total de personajes: {len(superheroes)}")
print("=" * 50)
 
print("\n1. Listado ordenado por nombre (ascendente):")
ordenados_nombre = sorted(superheroes, key=lambda x: x["name"])
for h in ordenados_nombre:
    print(f"  - {h['name']}")
 
print("\n2. Posición de The Thing y Rocket Raccoon en la lista original:")
for i, h in enumerate(superheroes):
    if h["name"] in ["The Thing", "Rocket Raccoon"]:
        print(f"  {h['name']} -> posición {i} (índice {i})")
 
print("\n3. Villanos de la lista:")
villanos = [h for h in superheroes if h["is_villain"]]
for v in villanos:
    print(f"  - {v['name']}")
 
print("\n4. Villanos en cola y los que aparecieron antes de 1980:")
cola_villanos = deque()
for v in villanos:
    cola_villanos.append(v)
 
print("  Villanos anteriores a 1980:")
temp = deque()
while cola_villanos:
    v = cola_villanos.popleft()
    if v["first_appearance"] < 1980:
        print(f"    - {v['name']} ({v['first_appearance']})")
    else:
        temp.append(v)
cola_villanos = temp
 
print("\n5. Personajes que empiezan con Bl, G, My o W:")
prefijos = ("Bl", "G", "My", "W")
for h in superheroes:
    if h["name"].startswith(prefijos):
        print(f"  - {h['name']}")
 
print("\n6. Personajes ordenados por nombre real:")
ordenados_real = sorted(superheroes, key=lambda x: x["real_name"] if x["real_name"] else "zzz")
for h in ordenados_real:
    print(f"  - {h['real_name']} ({h['name']})")
 
print("\n7. Personajes ordenados por fecha de aparición:")
ordenados_fecha = sorted(superheroes, key=lambda x: x["first_appearance"])
for h in ordenados_fecha:
    print(f"  - {h['name']} ({h['first_appearance']})")
 
print("\n8. Modificando nombre real de Ant Man:")
for h in superheroes:
    if h["name"] == "Ant Man":
        print(f"  Antes: {h['real_name']}")
        h["real_name"] = "Scott Lang"
        print(f"  Después: {h['real_name']}")
        break
 
print("\n9. Personajes con 'time-traveling' o 'suit' en su biografía:")
for h in superheroes:
    bio = h["short_bio"].lower()
    if "time-traveling" in bio or "suit" in bio:
        print(f"  - {h['name']}")
 
print("\n10. Eliminando a Electro y Baron Zemo:")
a_eliminar = ["Electro", "Baron Zemo"]
i = 0
while i < len(superheroes):
    if superheroes[i]["name"] in a_eliminar:
        eliminado = superheroes.pop(i)
        print(f"  Eliminado: {eliminado['name']} | Nombre real: {eliminado['real_name']} | Aparición: {eliminado['first_appearance']}")
    else:
        i += 1
 
print(f"\n  Total de personajes después de eliminar: {len(superheroes)}")
