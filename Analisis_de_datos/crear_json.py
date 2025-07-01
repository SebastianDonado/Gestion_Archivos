import json

# 1. Leer los datos del archivo original
with open('Personas.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

# 2. Crear diccionario vacío para el nuevo formato
deportes_dict = {}

# 3. Recorrer los usuarios y asignar sus deportes
for usuario, info in datos.items():
    for deporte in info['deportes']:
        if deporte not in deportes_dict:
            deportes_dict[deporte] = []
        deportes_dict[deporte].append(usuario)

# 4. Guardar el nuevo JSON
with open('deportes.json', 'w', encoding='utf-8') as salida:
    json.dump(deportes_dict, salida, indent=4, ensure_ascii=False)

print("Archivo 'deportes.json' creado correctamente.")
