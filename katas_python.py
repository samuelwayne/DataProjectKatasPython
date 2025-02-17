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
#### 8 - 