# TP 3

# 1)
def mayor_edad():
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad.")

# 2)
def aprobado():
    nota = float(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

# 3)
def numero_par():
    numero = int(input("Ingrese un numero par: "))
    if numero % 2 == 0:
        print("Ha ingresado un numero par")
    else:
        print("Por favor, ingrese un numero par")

# 4)
def categoria_edad():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

# 5) 
def password():
    contrasena = input("Ingrese una contraseña: ")
    if 8 <= len(contrasena) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6)
def estadisticas():
    import random
    from statistics import mode, median, mean

    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    m_media = mean(numeros_aleatorios)
    m_mediana = median(numeros_aleatorios)
    m_moda = mode(numeros_aleatorios)

    print(f"Media: {m_media}, Mediana: {m_mediana}, Moda: {m_moda}")

    if m_media > m_mediana > m_moda:
        print("Sesgo positivo o a la derecha")
    elif m_media < m_mediana < m_moda:
        print("Sesgo negativo o a la izquierda")
    elif m_media == m_mediana == m_moda:
        print("Sin sesgo")
    else:
        print("Distribucion mixta o indefinida")

# 7)
def ultima_vocal():
    texto = input("Ingrese una frase o palabra: ")
    if texto[-1].lower() in "aeiou":
        print(texto + "!")
    else:
        print(texto)

# 8)
def nombre():
    nombre = input("Ingrese su nombre: ")
    opcion = input("Ingrese 1 para mayusculas, 2 para minusculas, 3 para capitalizar: ")

    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opcion invalida")

# 9)
def magnitud_terremoto():
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud < 6:
        print("Fuerte (puede causar daños en estructuras debiles)")
    elif magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")

# 10) 
def estacion():
    hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
    mes = int(input("Ingrese el mes (1-12): "))
    dia = int(input("Ingrese el dia (1-31): "))

    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or mes in [10, 11] or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        estacion_norte = estacion_sur = "Fecha invalida"

    if estacion_norte == "Fecha invalida":
        print("Fecha no valida.")
    elif hemisferio == "N":
        print("Estacion:", estacion_norte)
    elif hemisferio == "S":
        print("Estacion:", estacion_sur)
    else:
        print("Hemisferio no valido.")
