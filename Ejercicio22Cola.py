class Stack:
    def __init__(self):
        self.__elementos = []

    def push(self, dato):
        self.__elementos.append(dato)

    def pop(self):
        return self.__elementos.pop()

    def top(self):
        return self.__elementos[-1]

    def size(self):
        return len(self.__elementos)

    def is_empty(self):
        return len(self.__elementos) == 0

    def show(self):
        for e in reversed(self.__elementos):
            print(e)


class Queue:
    def __init__(self):
        self.__elementos = []

    def arrive(self, dato):
        self.__elementos.append(dato)

    def attention(self):
        return self.__elementos.pop(0)

    def on_front(self):
        return self.__elementos[0]

    def move_to_end(self):
        self.__elementos.append(self.__elementos.pop(0))

    def size(self):
        return len(self.__elementos)

    def is_empty(self):
        return len(self.__elementos) == 0

    def show(self):
        for e in self.__elementos:
            print(e)


class Personaje:
    def __init__(self, nombre_p, nombre_s, genero):
        self.nombre_p = nombre_p
        self.nombre_s = nombre_s
        self.genero = genero

    def __str__(self):
        return f"{self.nombre_p} - {self.nombre_s} - {self.genero}"




personajess = [
    ("Tony Stark",      "Iron Man",        "M"),
    ("Steve Rogers",    "Capitán América", "M"),
    ("Natasha Romanoff","Black Widow",     "F"),
    ("Bruce Banner",    "Hulk",            "M"),
    ("Thor Odinson",    "Thor",            "M"),
    ("Clint Barton",    "Hawkeye",         "M"),
    ("Peter Parker",    "Spider-Man",      "M"),
    ("Scott Lang",      "Ant-Man",         "M"),
    ("Hope van Dyne",   "Wasp",            "F"),
    ("T'Challa",        "Black Panther",   "M"),
    ("Shuri",           "Black Panther",   "F"),
    ("Wanda Maximoff",  "Scarlet Witch",   "F"),
    ("Vision",          "Vision",          "M"),
    ("Sam Wilson",      "Falcon",          "M"),
    ("Bucky Barnes",    "Winter Soldier",  "M"),
    ("Stephen Strange", "Doctor Strange",  "M"),
    ("Carol Danvers",   "Capitana Marvel", "F"),
    ("James Rhodes",    "War Machine",     "M"),
    ("Peter Quill",     "Star-Lord",       "M"),
    ("Gamora",          "Gamora",          "F"),
]




def cargar(cola: Queue):
    for nombre_p, nombre_s, genero in personajess:
        cola.arrive(Personaje(nombre_p, nombre_s, genero))


def capitana_marvel(cola: Queue):
    for _ in range(cola.size()):
        pj = cola.on_front()
        if pj.nombre_s == "Capitana Marvel":
            print(f"El personaje de Capitana Marvel es: {pj.nombre_p}")
        cola.move_to_end()


def mostrar_femeninos(cola: Queue):
    print("Superhéroes femeninos:")
    for _ in range(cola.size()):
        pj = cola.on_front()
        if pj.genero == "F":
            print(f"  {pj.nombre_s}")
        cola.move_to_end()


# c. Nombres de los personajes masculinos
def mostrar_masculinos(cola: Queue):
    print("Personajes masculinos:")
    for _ in range(cola.size()):
        pj = cola.on_front()
        if pj.genero == "M":
            print(f"  {pj.nombre_p}")
        cola.move_to_end()


def superheroe_scott_lang(cola: Queue):
    for _ in range(cola.size()):
        pj = cola.on_front()
        if pj.nombre_p == "Scott Lang":
            print(f"El superhéroe de Scott Lang es: {pj.nombre_s}")
        cola.move_to_end()


def nombres_con_s(cola: Queue):
    print("Personajes/superhéroes cuyo nombre empieza con 'S':")
    for _ in range(cola.size()):
        pj = cola.on_front()
        if pj.nombre_p[0] == "S" or pj.nombre_s[0] == "S":
            print(f"  {pj}")
        cola.move_to_end()


def buscar_carol_danvers(cola: Queue):
    encontrado = False
    for _ in range(cola.size()):
        pj = cola.on_front()
        if pj.nombre_p == "Carol Danvers":
            print(f"Carol Danvers está en la cola. Su superhéroe es: {pj.nombre_s}")
            encontrado = True
        cola.move_to_end()
    if not encontrado:
        print("Carol Danvers no se encuentra en la cola.")




cola = Queue()
cargar(cola)

print("=" * 50)
print("a. Personaje de Capitana Marvel:")
print("=" * 50)
capitana_marvel(cola)

print()
print("=" * 50)
print("b. Superhéroes femeninos:")
print("=" * 50)
mostrar_femeninos(cola)

print()
print("=" * 50)
print("c. Personajes masculinos:")
print("=" * 50)
mostrar_masculinos(cola)

print()
print("=" * 50)
print("d. Superhéroe de Scott Lang:")
print("=" * 50)
superheroe_scott_lang(cola)

print()
print("=" * 50)
print("e. Nombres que empiezan con S:")
print("=" * 50)
nombres_con_s(cola)

print()
print("=" * 50)
print("f. ¿Carol Danvers está en la cola?")
print("=" * 50)
buscar_carol_danvers(cola)

