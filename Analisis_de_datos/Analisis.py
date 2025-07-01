import pandas as pd

df = pd.read_csv("SalesJan2009.csv")

print(df.head()) #Con esta linea podemos ver las primeras filas del archivo, esta linea es mas que todo para verificar la conexión con el archivo

def compras_pais(pais):
    return df[df['Country'] == pais].shape[0] # la función de la libreria pandas .shape cuenta cuantas filas cumple la condición planteada

def medios_pagos(medios):
    return df[df['Payment_Type'] == medios].shape[0]

option = int(input("1. Cuantas compras se realizaron por el país ingresado \n" \
"2. Cuantas compras se realizaron por el medio de pago ingresado \n" \
"otro número opción incorrecta \n" \
"Ingrese la opción que desea realizar \n"))

if option == 1:
    pais_input = input("Escribe el pais que quieres investigar cuantas compras se han realizado en él \n")
    print(f"En {pais_input} se realizaron {compras_pais(pais_input)}")

if option == 2:
    medio_input = input("Escribe el metodo de pago que quieres investigar cuantas compras se han realizado en él \n")
    print(f"Por el medio de pago {medio_input} se realizaron {medios_pagos(medio_input)}")

else:
    print("Opción invalidad")

