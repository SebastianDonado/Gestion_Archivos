import json

# Leer el archivo con las notas de los estudiantes
with open('notas_estudiantes.json', 'r', encoding='utf-8') as archivo:
    notas_estudiantes = json.load(archivo)

# Calcular el promedio de cada estudiante
promedios = {}
for nombre, notas in notas_estudiantes.items():
    if notas:
        promedio = sum(notas) / len(notas)
        promedios[nombre] = round(promedio, 2)
    else:
        promedios[nombre] = 0.0

# Guardar el promedio en un nuevo archivo
with open('promedios.json', 'w', encoding='utf-8') as archivo_salida:
    json.dump(promedios, archivo_salida, indent=4, ensure_ascii=False)

#print("Archivo 'promedios.json' creado con éxito.")  Esta linea se utiliza para confirmar la creación del archivo
