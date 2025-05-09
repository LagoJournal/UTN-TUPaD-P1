# TP 4

# 1) 
def print_0_to_100():
    for i in range(101):
        print(i)

# 2) 
def digitos():
    numero = input("Ingrese un numero entero: ")
    contador = 0
    for caracter in numero:
        if caracter.isdigit():
            contador += 1
    print(f"Cantidad de digitos: {contador}")

# 3) 
def suma_valores_intermedios():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    menor = min(a, b)
    mayor = max(a, b)
    total = 0
    for i in range(menor + 1, mayor):
        total += i
    print(f"Suma: {total}")

# 4)
def suma_hasta_cero():
    total = 0
    while True:
        num = int(input("Ingrese un numero (0 para terminar): "))
        if num == 0:
            break
        total += num
    print(f"Total: {total}")

# 5)
def adivinar_numero():
    import random
    objetivo = random.randint(0, 9)
    intentos = 0
    while True:
        intento = int(input("Adivina el numero (0-9): "))
        intentos += 1
        if intento == objetivo:
            print(f"¡Correcto, adivinaste en {intentos} intentos.")
            break

# 6) 
def pares_desc():
    for i in range(100, -1, -2):
        print(i)

# 7) 
def suma_desde_0_hasta_n():
    n = int(input("Ingrese un numero entero positivo: "))
    total = sum(range(n + 1))
    print(f"Suma: {total}")

# 8) 
def analizar_nums():
    pares = impares = negativos = positivos = 0
    for i in range(100):
        num = int(input("Ingrese un numero entero: "))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        if num < 0:
            negativos += 1
        elif num > 0:
            positivos += 1
    print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")

# 9)
def media():
    total = 0
    for i in range(100):
        num = int(input("Ingrese un numero entero: "))
        total += num
    media = total / n
    print(f"Media: {media}")

# 10)
def invertir_digitos():
    numero = int(input("Ingrese un numero: "))
    invertido = 0
    while numero != 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10
    print(f"Numero invertido: {invertido}")