# Gestion_Archivos

En los ejercicios tenemos de dos 3 tipos distintos, son los siguientes Archivos, Json y Exccepciones. 

#### Archivos

Tenemos los siguientes ejercicios para realizar a partir del archivo SalesJan2009.csv  el cual es un archivo con datos referentes a unas compras realizadas en distintos paises, distintos medios de pagos y ademas contienes fechas de compr, nombres, entre otros datos. Después de esta breve contextualización seguiremos con los ejercicios:

##### Ejercicio 1 y 2

Dado el archivo de texto les/SalesJan2009.csv, procese el archivo para obtener las compras realizadas en un pas dado.

Dado el archivo de texto les/SalesJan2009.csv, procese el archivo para obtener las compras realizadas con un medio de pago dado.

Podemos trabajar estos dos ejercicios juntos debido a que son muy parecidos y porque el segundo es un complemento o variante del primero 

###### Código

Empezamos descargando la libreria de pandas la cual nos permite trabajar en analisis de datos en este caso nos permite trabajar con el archivo .cvs (es un formato de archivo de texto sencillo que se utiliza para almacenar datos estructurados en forma de tabla).

Luego mediante esta linea <df = pd.read_csv("SalesJan2009.csv")> leemos el archivo .csv  y lo convertimos a un dataframe para poder trabajar con él, Creamos la función que busque en el archivo las compras realiozadas en el país mediante una variable que mas adelante introduciremos mediante el computador, para llevar el contador de las compras en el país que deseemos utilizamos la función .shape(0) la cual funciona recorriendo todo el archivo y cada ves que la comparación sea verdadera suma uno a su valor.

Para el segundo ejercicio utilizamos la misma estructura para el primero pero en al momento de comparar comparamos erl medio de pago.

![image](https://github.com/user-attachments/assets/9a8d8147-4f84-40d2-8d89-7056d0f8620f)


*Importante:* Hay que tener en cuenta al momento de generar los comparadores saber como se llama ese parametro en el archivo .csv para esto puedes utilizar la linea <print(df.head())> la cual imprime las primeras lineas del archivo y así conoceras de forma exacta los parametros.

*Para entender:* Cree un menú, ya lo he explicado en aanteriores trabajos, pero consiste en una serie de if que comparan si elegiste la opción uno o dos.

###### Ejecución

Ejercicio 1

![image](https://github.com/user-attachments/assets/3ff9f336-6120-4d3e-919f-b9e3d3a10c60)

Ejercicio 2

![image](https://github.com/user-attachments/assets/b4004e2a-7459-4d50-99fb-141fa5d07c04)

#### JSON

##### Ejercicios 1 y 2

Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.

Imprima los nombres completos (nombre y apellidos) de las personas que estén en un rango de edades dado por el usuario.

###### Código

Para este código importamos json para trabajar con este tipo de archivos, luego con esta linea <with open('Personas.json', 'r', encoding='utf-8') as archivo:> Abrimos el archivo json, en modo lectura con 'r' y con encoding= 'utf-8' es un unicode que permite leer tildes y la ñ, luego con la siguiente linea <datos = json.load(archivo)> Mediante json.load convertimos el json a un diccionario de python.

También creamos la función que pasandole el parametro "deporte" para que lo busque en el diccionario y cada vez que coincida nos imprimirá los nombres y los apellidos mediante el siguiente for:

![image](https://github.com/user-attachments/assets/84f220c1-15f8-401a-a50b-7ef1637040c8)

Para el segundo ejercicio realizamos lo mismo lo único distinto es que hacemos que la comparación se encuentre dentro de un rango de edades ingresadas desde el teclado, código del rango:

![image](https://github.com/user-attachments/assets/d2d746af-e75d-45f2-b08f-e41b0659239a)

Código completo:

![image](https://github.com/user-attachments/assets/73c78926-512f-4316-b633-dabdf5baa00c)

*Importante:* Con .lower hacemos que la comparación no sea sensible a mayuscúlas.

*Para entender:* Cree un menú, ya lo he explicado en aanteriores trabajos, pero consiste en una serie de if que comparan si elegiste la opción uno o dos.

###### Ejecución

![image](https://github.com/user-attachments/assets/5c55c496-4868-43b2-98ad-eb4a6b270f8e)

![image](https://github.com/user-attachments/assets/e3f5c914-64cb-47cf-9a95-59854c54337f)

###### Ejercicio 3

Cree un JSON de deportes como sigue:

![image](https://github.com/user-attachments/assets/dfa7326a-40e3-4e8b-bca1-0fc9ad23f7d7)

###### Código

Aquí iniciamos igual que en los ejercicios anteriores pero creamos un diccionario vacio con la siguiente linea <deportes_dict = {}> y usando el archivo de personas.json creamos el archivo deportes.json donde recorre cada deporte y guarda en el nuevo diccionaria las personas que practiquen cada deporte,de esta manera una persona puede pertenecer a varios deportes:

![image](https://github.com/user-attachments/assets/a4671b78-a67b-45ea-a290-136a1cf5db45)}

*Importante:* Para crear el nuevo archivo json se debe realizar el mismo paso pero en lugar de abrirlo en modo lectura 'r' lo abrimos en escritura 'w'

###### Ejecución

Mensaje de exito:

![image](https://github.com/user-attachments/assets/b6dc8fae-4948-415a-a279-954dc904151a)

Archivo Json:

![image](https://github.com/user-attachments/assets/8b068772-7f2b-477b-8a6c-1ad814f6bdd4)

##### Ejercicio 4

Desarrolle un programa que lea dos archivos JSON, y encuentre los componentes clave:valor que son iguales en ambos. Genere un nuevo archivo JSON con las coincidencias exactas entre los dos archivos.

###### Código

Iniciamos abriendo los dos archivos que tenemos como ya sabemos hacerlo, para luego compararlos mediante la siguiente función que compara las claves iguales:

![image](https://github.com/user-attachments/assets/57ab78de-4dde-43f1-a5b4-43fcd96d3e46)

Código completo:

![image](https://github.com/user-attachments/assets/5808340d-ff48-4378-8637-d1f8f96521b6)

###### Ejecución

![image](https://github.com/user-attachments/assets/033485fd-29b3-47c3-b715-df6314bd2f4b)

Archivo Json:

 ![image](https://github.com/user-attachments/assets/6f2c0748-b80a-40ab-a771-0107d451201d)

 Quiere decir que no hay coincidencias exactas entre mis archivos

##### Ejercicio 5

Desarrolle un programa que lea un archivo JSON, en el cual se encuentran las notas de los estudiantes del curso. Cada llave corresponde al c ́odigo de cada estudiante, y su valor es una lista con las notas obtenidas en las actividades del curso. Se debe generar un nuevo archivo JSON que para uno de los estudiantes solo guarde el promedio de las notas obtenidas.

###### Código 

Creamos un archivo json con las notas de cada estudiante:

![image](https://github.com/user-attachments/assets/fcbd39f4-1be8-401a-80dd-eac2d0a1120e)

Luego hacemos lo mismo que hemos venido realizando con los anteriores ejercicios:

![image](https://github.com/user-attachments/assets/0c10b216-224d-402b-8a98-e59d1019cc99)

###### Ejecución

![image](https://github.com/user-attachments/assets/4367acdb-d263-4725-8506-9dd764ea1745)

##### Ejercicio 5

Desarrollar un programa que lea un archivo JSON que contiene una serie de cadenas de caracteres en min ́uscula, cada una con su propia llave. Estas llaves tienen una codificaci ́on, a forma de encriptaci ́on, en donde las vocales est ́an descritas como otros s ́ımbolos: $ en vez de a, '#' en vez de e, * en vez de i, ¬ en vez de o, y + en vez de u. Una vez
le ́ıdo el archivo, realice una desencriptaci ́on de todas las cadenas, es decir, convierta los s ́ımbolos a sus vocales correspondientes (si la cadena de entrada es ”h¬l$”, la cadena resultante ser ́ıa ”hola”), y guarde el resultado en un nuevo archivo JSON.

###### Código





