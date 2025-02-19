####
#### 1 - Función que cuente la frecuencia de las letras en un string, exceptuar espacios:

texto1 = 'Cuantas letras tiene este texto'

def contar_frecuencia_letras (texto):
    """ Esta función cuenta la frecuencia de aparición de las letras en el texto pasado como argumento,
    sin contar los espacios y devuelto finalmente en forma de diccionario.

    Args:
        texto (str): Texto pasado a la función, únicamente usando letras y espacios.
                     Otros caracteres pueden generar errores.
    """
    
    # Mediante esta list comprehension guardamos cada tipo de letra distinto en un set
    set_letras_texto = set()
    [set_letras_texto.add(letra) for letra in texto.lower() if letra != ' ']

    # Mediante una list comprehension creamos cada par de clave valor y convertimos la lista en diccionario
    diccio_frecuencia_letras = dict([(letra, texto.lower().count(letra)) for letra in set_letras_texto])

    return diccio_frecuencia_letras

solucion_1 = contar_frecuencia_letras(texto1)
print('1 - Solución:', solucion_1)

####
#### 2 - De una lista de números, obtener una con el doble de cada valor usando map():

lista_numeros2 = [0, 1, 2, 5, 8, 9, 6, 6, 14]

solucion_2 = list(map(lambda x: x*2, lista_numeros2))
print('2 - Solución:', solucion_2)

####
#### 3 - Crear una función que dada una lista de palabras y un parámetro palabra, devuelva una lista con
# las palabras que contegan la palabra objetivo:

lista_palabras3 = ['fiesta', 'aguado', 'calor', 'paraguas', 'agudo', 'aguafiestas']

def listar_palabras_objetivo (lista_palabras, palabra_objetivo):
    """Esta función comprueba si la palabra objetivo está en alguno de los valores de la lista dada

    Args:
        lista_palabras (str): lista de palabras random
        palabra_objetivo (str): palabra objetivo a buscar en cada uno de los elementos de la lista
    """

    lista_filtrada = [palabra for palabra in lista_palabras if palabra_objetivo in palabra ]
    return lista_filtrada

solucion_3 = listar_palabras_objetivo(lista_palabras3, 'agua')
print('3 - Solución:', solucion_3)

####
#### 4 - Función que calcula la diferencia entre los valores de dos listas usando map():

lista_x_numeros4 = [0, 5, -2, 3, 1, 24]
lista_y_numeros4 = [52, 6, 8, -11, -9, 7]

solucion_4 = list(map(lambda x, y: x - y, lista_x_numeros4, lista_y_numeros4))
print('4 - Solución:', solucion_4)

####
#### 5 - Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

lista_numeros5 = [4, 6, 5.5, 6.9, 7.25, 5]

def calcular_media_aprobado (lista_numeros, nota_aprobado=5):
    """Esta función comprueba la media de la lista de números y comprueba si es mayor o igual a la nota_aprobado.

    Args:
        lista_numeros (list): Lista de números de la que se extrae la media.
        nota_aprobado (int, optional): Nota de aprobado definible, que por defecto es 5.
    """

    media = sum(lista_numeros) / len(lista_numeros)
    if media >= nota_aprobado:
        estado = 'aprobado'
    else:
        estado = 'suspenso'
    return (round(media, 2), estado)

solucion_5 = calcular_media_aprobado(lista_numeros5)
print('5 - Solución:', solucion_5)

####
#### 6 - Función que calcula el factorial de un número de manera recursiva:

def factorial_def_recursiva (n):
    """Esta funcion devuelve el factorial del un número.

    Args:
        n (int): Un número entero cualquiera.

    Returns:
        int: Resultado de realizar el factorial de un número
    """
    if n > 1:
        resultado = n * factorial_def_recursiva(n-1)
        return resultado
    else:
        #es necesario este else para que cuando llegue al valor 1 devuelva el valor del número,
        # sino devuleve error al no poder devolver resultado, porque resultado no tendróia valor asignado
        return n

solucion_6 = factorial_def_recursiva(5)
print('6 - Solución:', solucion_6)

####
#### 7 - Convertir lista de tuplas en lista de strings.

lista_tuplas7 = [(5, 'camello'), ('Hola', 'Python!'), (3.14159, ['manzana', 3])]

solucion_7 = list(map(lambda x: str(x), lista_tuplas7))
print('7 - Solución:', solucion_7)

####
#### 8 - Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa
# un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate
# de mostrar un mensaje indicando si la división fue exitosa o no.

# try:
#     numero_x_8 = int(input('Escriba un número: '))
#     numero_y_8 = int(input('Escriba otro numero por el que quiera dividir el primero: '))
#     solucion_8 = numero_x_8 / numero_y_8
#     print('Operación realizada con éxito!\n8 - Solución:', solucion_8)
# except ValueError:
#     print('División no realizada. No es posible operar ese valor. Por favor, debe introducir un número.')
# except ZeroDivisionError:
#     print('División no realizada. No es posible dividir entre 0.')

####
#### 9 - Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva
# lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache",
# "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter():

lista_mascotas9 = ["Perro", "Gato", "Serpiente", "Hámster", "tigre"]

def filtrar_mascotas_prohibidas_España(lista_mascotas):
    mascotas_prohibidas_España = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    def filtrar_mascota(mascota):
        """Función que itera sobre cada mascota en la lista dada, comparando si se encuentra
        entre las mascotas prohibidas en España (previamente definidas)

        Args:
            mascota (str): Cada mascota de la lista

        Returns:
            str: Mascota que no está prohibida
        """
        if mascota.title() not in mascotas_prohibidas_España:
            return mascota
    lista_filtrada = list(filter(filtrar_mascota, lista_mascotas))
    return lista_filtrada

solucion_9 =  filtrar_mascotas_prohibidas_España(lista_mascotas9)
print('9 - Solución:', solucion_9) #el resultado devuelve 'serpiente' porque es distinto a 'serpiente pitón'

####
#### 10 - Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía,
# lanza una excepción personalizada y maneja el error adecuadamente:

lista_numeros10 = [5, 8, 6, -6, 22, 10, 1]

def calcular_promedio_lista_numeros (lista_numeros):
    """Función para cacluclar el valor promedio de una lista de números

    Args:
        lista_numeros (list): lista de números de la que calcular la media

    Returns:
        float: media
    """
    try:
        media = sum(lista_numeros) / len(lista_numeros)
        return round(media, 3)
    except ZeroDivisionError:
        return ('No se puede calcular la media de una lista vacía.')

solucion_10 = calcular_promedio_lista_numeros(lista_numeros10)
print('10 - Solución:', solucion_10)

####
#### 11 -  Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no
# numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excep-
# ciones adecuadamente.

# try:
#     edad_usuario = int(input('Por favor, introduzca su edad: '))
#     if edad_usuario < 0 or edad_usuario > 120:
#         print('La edad ingresada debe ser un número válido')
# except ValueError:
#     print('La edad ingresada debe ser un número válido')

####
#### 12 - Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa
# la función map():

frase12 = "Me está encantando estudiar Data Science"

def listar_len_palabras_en_frase (frase):
    """Esta función divide la frase por palabras, y luego pasa esa lista por un map() para que pase la len()
    por cada palabra de la lista

    Args:
        frase (str): Frase cuyas palabras queremos transformar en una lista de numeros que indiquen la
        longitud de las palabras

    Returns:
        list: lista de numeros indicando la longitud de cada palabra
    """
    lista_palabras = frase.split(' ')
    lista_len_palabras = list(map(len, lista_palabras))
    return lista_len_palabras

solucion_12 = listar_len_palabras_en_frase(frase12)
print('12 - Solución:', solucion_12)

####
#### 13 -  Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada
# letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map():

caracteres13 = 'kcgwusncoisbhc'

def listar_caracteres_may_min (texto):
    """Esta función itera sobre los caracteres de un texto, y devuelve una tupla con los valores
    (Mayuscula, minuscula) de cada letra iterada. Los guarda como un set para evitar valores duplicados, 
    que posteriormente se transforma en lista

    Args:
        texto (str): caracteres a iterar

    Returns:
        list: lista con valores de letras en formato de tupla (Mayuscula, minuscula) sin valores repetidos
    """
    lista_tuplas_may_min = list(set(map(lambda x: (x.upper(), x.lower()), texto)))
    return lista_tuplas_may_min

solucion_13 = listar_caracteres_may_min(caracteres13)
print('13 - Solución:', solucion_13)

####
#### 14 - Crea una función que retorne las palabras de una lista de palabras que comience con una letra en
# especifico. Usa la función filter():

lista_palabras14 = ['amigo', 'trabajo', 'Comida', 'tesoro', 'cámara', 'crear']

def filtrar_empieza_por (lista_palabras, letra):
    """Esta función itera por cada palabra de la lista, comprueba si empieza por la letra especificada y solo
    devuelvelos valores verdaderos

    Args:
        lista_palabras (list): lista de strings
        letra (str): letra especificada por la que comprobar si empiezan las palabras de la lista

    Returns:
        list: lista filtrada
    """
    lista_filtrada = list(filter(lambda x: x.lower().startswith(letra.lower()), lista_palabras))
    return lista_filtrada

solucion_14 = filtrar_empieza_por(lista_palabras14, "C")
print('14 - Solución:', solucion_14)

####
#### 15 - Crea una función lambda que sume 3 a cada número de una lista dada:

lista_numeros15 = [-5, 8, 6, -6, 22, 10, 1]

solucion_15 = list(map(lambda x: x+3, lista_numeros15))
print('15 - Solución:', solucion_15)

####
#### 16 - 

print('FALTA QUITAR COMENTARIO DEL 8, 11')