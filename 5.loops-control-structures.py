"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecuón y la lógica de un algoritmo
"""

"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""
# Escribe tu código aquí
letra= str(input("Dame una letra para decirte si es una vocal o consonante: ")).lower()
if letra in("a", "e", "i", "o", "u"):
    print("Tu letra es una vocal")
else:
    print("Tu letra es una consonante")

"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si 
es una calificación de "A", "B", "C", "D" o "F".
"""
# Escribe tu código aquí
nota= float(input("Dame una nota entre 0 y 100 y te dire la calificación: "))
if (nota >= 0 and nota <= 20):
    print("Tu calificación es: F.")
elif (nota > 20 and nota <= 40):
    print("Tu calificación es: D.")
elif (nota > 40 and nota <= 60):
    print("Tu calificación es: C.")
elif (nota > 60 and nota <= 80):
    print("Tu calificación es: B.")
elif (nota > 80 and nota <= 100):
    print("Tu calificación es: A.")
else:
    print("Tu nota no es valida.")

"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y 
luego imprima la cuenta regresiva desde ese número hasta 1.
"""
# Escribe tu código aquí
Entero= int(input("Dame un número entero positivo para empezar la cuenta atras: "))
while Entero > 0:
    print(Entero)
    Entero -= 1

"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""
# Escribe tu código aquí
cadena= input("Escribe la palabra que quieras que yo la separo por letras: ")
for letra in cadena:
    print(letra)

"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""
# Escribe tu código aquí
for i in range(1, 11):
    print(f'El resultado de 5 * {i}= {5* i}')

"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y 
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""
# Escribe tu código aquí
list_minúsculas= []
list_majúsculas= []

for i in range(5):
    palabra= input(str("Dame 1 palabra diferente a la anterior: "))
    list_minúsculas.append(palabra)
    list_majúsculas.append(palabra.upper())

print(list_minúsculas)
print(list_majúsculas)

"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y 
si es un perro, que imprima en la consola "Tengo un perro", 
si es un gato, que imprima en la consola "Tengo un gato", 
si es un pájaro, que imprima en la consola "Tengo un pájaro" y 
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""
# Escribe tu código aquí
while True:
    mascota= input(str("Dame el nombre de una mascota: ")).lower()

    if mascota == "":
        print("Escribe el nombre de una mascota.")
        continue

    if mascota == "perro":
        print("Tengo un perro")
    elif mascota == "gato":
        print("Tengo un gato")
    elif mascota == "pájaro":
        print("Tengo un pájaro")
    else:
        print("No tengo una mascota convencional")

    break