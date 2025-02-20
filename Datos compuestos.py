#Listas de datos
#Para hacer listas con[]
nombre_personas=["juan","carlos","jose","julio","maria"]
print(nombre_personas[2])
print(nombre_personas[4])

#Tuplas
#Para hacer tuplas con()
nombre_personas=("juan","carlos",25)
print(nombre_personas)
#print(nombres_personas[2])
#print(nombres_personas[4])

#Lista es un tipo de dato compuesto
#Los valores de las listas, puedenser modificados
nombre_personas=["jose","pereira","juna","carlos",25,7,4,True]
print(nombre_personas[2])
nombre_personas[2]="pedro"
print(nombre_personas[2])

#Tuplas igual que las listas, almacenan valores, pero no pueden
#modificados, sus valores son inmutables.
frutas_tropicales=("mango","naranja","coco")
frutas_tropicales=("piña","mango")
#frutas_tropicales=("piña")
print(frutas_tropicales) 

#Los conjuntos en python omiten los valores que son duplicados
#Para hacer conjuntos con{}
apellidos={"juan","carlos","julio","juan"}
print(apellidos)

numeros={2,6,7,2}
print(numeros)

#Diccionarios en python otro tipo de dato compuesto

datos_personales={
    'nombre':'jose',
    'apellido':'pereira',
    'edad':15,
    'persona':True
}

print(datos_personales['apellido'])
print(datos_personales['nombre'])
