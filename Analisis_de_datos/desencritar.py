import json

# Mapeo de símbolos a vocales
sustituciones = {
    '$': 'a',
    '#': 'e',
    '*': 'i',
    '¬': 'o',
    '+': 'u'
}

def desencriptar(cadena):
    resultado = ""
    for caracter in cadena:
        if caracter in sustituciones:
            resultado += sustituciones[caracter]
        else:
            resultado += caracter
    return resultado

# Leer archivo JSON original
with open("mensajes_encriptados.json", "r", encoding="utf-8") as archivo:
    codificados = json.load(archivo)

# Desencriptar
descifrados = {
    clave: desencriptar(texto)
    for clave, texto in codificados.items()
}

# Guardar nuevo archivo con desencriptado
with open("mensajes_desencriptados.json", "w", encoding="utf-8") as salida:
    json.dump(descifrados, salida, indent=4, ensure_ascii=False)

print("Archivo 'mensajes_desencriptados.json' creado con éxito.")
