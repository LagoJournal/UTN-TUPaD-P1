# 1)
def multiplos_4():
    multiplos_de_4 = list(range(4, 101, 4))
    print("Multiplos de 4:", multiplos_de_4)

# 2) Mostrar el penultimo elemento de una lista personalizada
def penultimo_elemento():
    gustos = ["chocolate", "libros", "peliculas", "musica", "gatos"]
    print("Penultimo elemento:", gustos[-2])

# 3)
def append_3():
    lista_vacia = []
    lista_vacia.append("palabra1")
    lista_vacia.append("palabra2")
    lista_vacia.append("palabra3")
    print("Lista con palabras:", lista_vacia)

# 4) 
def replace_mascotas():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print("Lista de animales modificada:", animales)

# 5)
def explicacion_ej5():
    numeros = [8, 15, 3, 22, 7]  # Crea la lista
    numeros.remove(max(numeros)) # max()-> busca el maximo (22) y lo remueve
    print(numeros) # imprime la lista sin el elemento 22 -> [8, 15, 3, 7]


# 6) 
def lista_intervalo_5():
    saltos = list(range(10, 31, 5))
    print("6) Dos primeros elementos:", saltos[:2])

# 7) 
def replace_valores_intermedios():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1:3] = ["camioneta", "coupe"]
    print("Autos modificados:", autos)

# 8) 
def append_dobles():
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print("Lista de dobles:", dobles)

# 9) 
def mod_lista_anidadas():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print("Lista de compras modificada:", compras)

# 10)
def lista_anidada():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print("10) Lista anidada:", lista_anidada)
