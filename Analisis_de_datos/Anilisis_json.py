import json

with open('Personas.json', 'r', encoding='utf-8') as archivo:  #Abrimos el archivo json, en modo lectura con 'r' y con encoding= 'utf-8' es un unicode que permite leer tildes y la ñ
    datos = json.load(archivo)   #Mediante json.load convertimos el json a un diccionario de python 

def persons_deport(deporte):
    return [
        f"{info['nombres']} {info['apellidos']}"
        for usuario, info in datos.items()
        if deporte.lower() in [d.lower() for d in info['deportes']]
    ]

def rango_edades(edad_min,edad_max):
    return [
        f"{info['nombres']} {info['apellidos']}"
        for usuario, info in datos.items()
        if edad_min <= info['edad'] <= edad_max
    ]
#Creamos un menú con opciones para movernos entre los ejercicios

option = int(input("1. Cuantas personas realizan el deporte que desee ingresar \n" \
"2. Cuantas personas estan dentro del rango de edades que ingresas \n" \
"otro número opción incorrecta \n" \
"Ingrese la opción que desea realizar \n"))

if option == 1:
    deport = input("Escribe qué deporte quieres consultar: ")
    print(f"Las personas que practican {deport} son: {persons_deport(deport)}")

if option == 2:
    edad_min = int(input("Ingrese la edad miníma del rango que desea buscar \n"))
    edad_max = int(input("Ingrese la edad maxíma del rango que desea buscar"))
    print(f"Las personas que se encuentran dentro del rango de edades ({edad_min},{edad_max}) son: {rango_edades(edad_min,edad_max)}")

else:
    print("Opción invalidad")

