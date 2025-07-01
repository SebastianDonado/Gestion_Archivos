import json

# Paso 1: Cargar archivos
with open('Personas.json', 'r', encoding='utf-8') as archivo1:
    datos_personas = json.load(archivo1)

with open('deportes.json', 'r', encoding='utf-8') as archivo2:
    datos_deportes = json.load(archivo2)

# Paso 2: Buscar coincidencias exactas
coincidencias = {
    clave: valor
    for clave, valor in datos_personas.items()
    if clave in datos_deportes and datos_deportes[clave] == valor
}

# Paso 3: Guardar resultado
with open('coincidencias.json', 'w', encoding='utf-8') as salida:
    json.dump(coincidencias, salida, indent=4, ensure_ascii=False)

print("Archivo 'coincidencias.json' creado con éxito.")
