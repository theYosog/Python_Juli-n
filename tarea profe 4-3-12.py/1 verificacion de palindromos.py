#Descripcion:pide al usuario una palabra y verifica si es
#un palindromo(se lee igual al derecho y al reves)
#Requisitos:.Usar input() para recibir la palabra.
           #.Convertir la palabra a minusculas.
           #.Usar un condicional para verificar si la palabra
           #es igual a su version invertida.
           #.Mostrar un mensaje indicando si es o no un palindromo.

palabra=input("Ingresa una palabra: ")

palabra=palabra.lower()

if palabra==palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
