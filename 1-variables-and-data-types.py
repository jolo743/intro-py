"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
# Escribe tu código aquí
mensaje = "¡Hola, Mundo!"
print(mensaje)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
# Escribe tu código aquí
mensaje = "Hello, World!"
print(mensaje)

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
# Escribe tu código aquí
string = "string"

print(string)
print(type(string))

int = 10

print(int)
print(type(int))

float = 123.356

print(float)
print(type(float))

bool = True

print(bool)
print(type(bool))

list = [1, 6, 0]

print(list)
print(type(list))

tuple = ("apple", "banana", "cherry")

print(tuple)
print(type(tuple))

dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(dictionary)
print(type(dictionary))

set = {"lemon", "kiwi", "pineapple"}

print(set)
print(type(set))
