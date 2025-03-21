from functools import reduce
import datetime
from math import pi

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
    texto_analizar = texto.lower()

    # Mediante este set comprehension guardamos cada tipo de letra distinto en un set
    set_letras_texto = set(letra for letra in texto_analizar if letra != ' ')

    # Mediante un dictionary comprehension creamos cada par de clave-valor en el diccionario
    diccio_frecuencia_letras = {letra: texto_analizar.count(letra) for letra in set_letras_texto}

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

def dividir_dos_numeros ():
    try:
        numero_x = int(input('Escriba un número: '))
        numero_y = int(input('Escriba otro numero por el que quiera dividir el primero: '))
        solucion = numero_x / numero_y
        return (f'Operación realizada con éxito! Solución: {solucion}')
    except ValueError:
        return 'División no realizada. No es posible operar ese valor. Por favor, debe introducir un número.'
    except ZeroDivisionError:
        return 'División no realizada. No es posible dividir entre 0. Por favor, debe introducir un número válido.'

solucion_8 = dividir_dos_numeros()
print(f'8 - {solucion_8}')

####
#### 9 - Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva
# lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache",
# "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter():

lista_mascotas9 = ["Perro", "Gato", "Serpiente", "Hámster", "tigre"]

def filtrar_mascotas_prohibidas_España(lista_mascotas):
    mascotas_prohibidas_España = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    set_mascotas_prohibidas = set(mascota.lower() for mascota in mascotas_prohibidas_España)
    def filtrar_mascota(mascota):
        """Función que itera sobre cada mascota en la lista dada, comparando si se encuentra
        entre el set de mascotas prohibidas en España (previamente definidas)

        Args:
            mascota (str): Cada mascota de la lista

        Returns:
            str: Mascota que no está prohibida
        """
        if mascota.lower() not in set_mascotas_prohibidas:
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
    if len(lista_numeros) > 0:
        media = sum(lista_numeros) / len(lista_numeros)
        return round(media, 3)
    else:
        return ValueError ('No se puede calcular la media de una lista vacía.')

solucion_10 = calcular_promedio_lista_numeros(lista_numeros10)
print('10 - Solución:', solucion_10)

####
#### 11 -  Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no
# numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excep-
# ciones adecuadamente.

def introduzca_edad ():
    try:
        edad_usuario = int(input('Por favor, introduzca su edad: '))
        if edad_usuario < 0 or edad_usuario > 120:
            return 'La edad ingresada debe ser un número válido'
    except ValueError:
        return 'La edad ingresada debe ser un número válido'
    return edad_usuario

solucion_11 = introduzca_edad()
print(f'11 - Solución: Su edad es de {solucion_11} años.')

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
    """Esta función itera por cada palabra de la lista, comprueba si empieza por la letra especificada y
    solo devuelve los valores verdaderos

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
#### 16 - Escribe una función que tome una cadena de texto y un número entero n como parámetros
# y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter():

cadena_texto16 = 'Érase una vez un tremendo texto escrito en Python' 

def filtrar_longitud_palabras (texto, n):
    """Esta función filtra por longitud de palabra dado un tamaño n y devuelve la lista filtrada

    Args:
        texto (str): cadena de texto cuyas longitud de palabras queremos comparar
        n (int): longitud de palabra a usar en el filtro
    """
    def comparar_len_palabra (palabra):
        if len(palabra) > n:
            return palabra
    lista_palabras = texto.split(' ')
    lista_filtrada = list(filter(comparar_len_palabra, lista_palabras))
    return lista_filtrada

solucion_16 = filtrar_longitud_palabras (cadena_texto16, 5)
print('16 - Solución:', solucion_16)

####
#### 17 - Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo,
# [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce():

lista_digitos17 = [8, 4, 6, 1]

def digitos_a_numero (lista_digitos):
    """Dada una lista de digitos los junta todos en un solo numero, sumando cada digito como str

    Args:
        lista_digitos (list): lista de numeros enteros de 1 digito
    """
    def str_y_join (digito1, digito2):
        nums = (str(digito1), str(digito2))
        num_total = ''.join(nums)
        return num_total
    numero_devuelto = reduce(str_y_join, lista_digitos)
    return int(numero_devuelto)

solucion_17 = digitos_a_numero(lista_digitos17)
print('17 - Solución:', solucion_17)

####
#### 18 - Escribe un programa en Python que cree una lista de diccionarios que contenga información de
# estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con
# una calificación mayor o igual a 90. Usa la función filter():

lista_datos18 = [("Pepito", 22, 85), ("Fulanita", 25, 75), ("Juanito", 26, 95), ("Menganita", 24, 90)]

def crear_dict_y_filtrar_nota_90 (lista):
    def crear_diccionario (tupla):
        #Esta función coge los valores de la tupla y los reorganiza para crear el diccionario
        x, y, z = tupla
        item_en_tupla = (x, (y, z))
        return item_en_tupla
    diccionario = dict(map(crear_diccionario, lista))
    def filtrar_nota_90 (item):
        #Esta función coge cada item del diccionario y los separa, para comparar únicamente la nota
        #Después devuelve únicamente los items cuya nota es igual o superior a 90
        nombre, valores = item
        edad, nota = valores
        if nota >= 90:
            return item
    diccio_filtrado = dict(filter(filtrar_nota_90, diccionario.items()))
    return diccio_filtrado

solucion_18 = crear_dict_y_filtrar_nota_90(lista_datos18)
print('18 - Solución:', solucion_18)

####
#### 19 - Crea una función lambda que filtre los números impares de una lista dada:

lista_numeros19 = [5, 2, 6, 7, 8, 3, 11]

solucion_19 = list(filter(lambda x: x % 2 != 0, lista_numeros19))
print('19 - Solución:', solucion_19)

####
#### 20 - Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los
# valores int. Usa la función filter():

lista_mixta20 = ["5", 2, '6', "7", 8, 3, "11"]

solucion_20 = list(filter(lambda x: isinstance(x, int), lista_mixta20))
print('20 - Solución:', solucion_20)


####
#### 21 - Crea una función que calcule el cubo de un número dado mediante una función lambda:

numero21 = 21

numero_al_cubo = lambda x: x**3

solucion_21 = numero_al_cubo(numero21)
print('21 - Solución:', solucion_21)

####
#### 22 - Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la
# función reduce():

lista_productos22 = [2, 5, 4, 6, 12]

solucion_22 = reduce(lambda x, y: x*y, lista_productos22)
print('22 - Solución:', solucion_22)

####
#### 23 - Concatena una lista de palabras. Usa la función reduce():

lista_palabras23 = ['amigo', 'trabajo', 'Comida', 'tesoro']

solucion_23 = reduce(lambda x, y: x+y, lista_palabras23)
print('23 - Solución:', solucion_23)

####
#### 24 - Calcula la diferencia total en los valores de una lista. Usa la función reduce():

lista_numeros24 = [8, 6, -4, 3, 23, -11, 7]

solucion_24 = reduce(lambda x, y: x-y, lista_numeros24)
print('24 - Solución:', solucion_24)

####
#### 25 - Crea una función que cuente el número de caracteres en una cadena de texto dada:

texto_25 = 'Esta es una cadena de texto'

def contar_caracteres (texto):
    numero_caracteres = 0
    for i in texto:
        if i.lower() in 'abcdefghijklmnñopqrstuwxyz':
            numero_caracteres += 1
        else:
            continue
    return numero_caracteres

solucion_25 = contar_caracteres(texto_25)
print('25 - Solución:', solucion_25)

####
#### 26 - Crea una función lambda que calcule el resto de la división entre dos números dados:

resto_division = lambda x, y: x % y

solucion_26 = resto_division(11, 4)
print('26 - Solución:', solucion_26)

####
#### 27 - Crea una función que calcule el promedio de una lista de números:

lista_numeros27 = [51, 56, 57, 49, 45, 55]

promedio_numeros = lambda x: round((sum(x) / len(x)), 3)

solucion_27 = promedio_numeros(lista_numeros27)
print('27 - Solución:', solucion_27)


####
#### 28 - Crea una función que busque y devuelva el primer elemento duplicado en una lista dada

lista_mixta28 = ['gato', 'conejo', 4, [9, 1], 4.25, 4.25, "HOLA"]

def encontrar_primer_duplicado (lista):
    """Función recursiva que compara todos los elementos de una lista con el primero, y devuelve el
    primer duplicado. En caso contrario, elimina el primer valor de la lista y repite el proceso
    hasta que la lista solo tenga un único valor.

    Args:
        lista (list): lista en la que buscar el duplicado

    Returns:
        any_type: primer elemento duplicado
    """
    set_comprobacion = set()
    for elemento in lista:
        #para evitar 'unhashable type' por si el elemento es otra lista
        if isinstance(elemento, list):
            elemento = tuple(elemento)
        if elemento not in set_comprobacion:
            set_comprobacion.add(elemento)
        else:
            primer_duplicado = elemento
            return primer_duplicado
    return 'No se encontraron elementos duplicados'

solucion_28 = encontrar_primer_duplicado(lista_mixta28)
print('28 - Solución:', solucion_28)

####
#### 29 - Crea una función que convierta una variable en una cadena de texto y enmascare todos
# los caracteres con el carácter '#', excepto los últimos cuatro:

pin29 = 6848695411

def enseñar_contarseña (pin):
    pin = str(pin)
    pin_enmascarado = pin[-4::1].rjust(len(pin), '#')
    return pin_enmascarado

solucion_29 = enseñar_contarseña(pin29)
print('29 - Solución:', solucion_29)


####
#### 30 - Crea una función que determine si dos palabras son anagramas, es decir, si están formadas
# por las mismas letras pero en diferente orden:

palabra30_1 = 'barco' 
palabra30_2 = 'cobra'

def check_anagrama (palabra1, palabra2):
    letras_palabra1 = contar_frecuencia_letras(palabra1)
    letras_palabra2 = contar_frecuencia_letras(palabra2)
    if letras_palabra1 == letras_palabra2:
        return (f'"{palabra1}" es un anagrama de "{palabra2}"')

    else:
        return (f'"{palabra1}" NO es un anagrama de "{palabra2}"')
    
solucion_30 = check_anagrama(palabra30_1, palabra30_2)
print('30 - Solución:', solucion_30)

####
#### 31 - Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite
# un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando
# que fue encontrado, de lo contrario, se lanza una excepción.

lista31 = "Pablo, Ana, María, Cristian, Paloma"
nombre31 = 'Ana'

def buscar_nombre ():
        lista = (input('Por favor, ingrese una lista de nombres: ')).split(', ')
        nombre = input('Por favor, ingrese el nombre que desea buscar: ')
        for nombres in lista:
            if nombre == nombres:
                return 'El nombre se encuentra en la lista'
        return 'Nombre no encontrado'
    
solucion_31 = buscar_nombre()
print('31 - Solución:', solucion_31)

####
#### 32 -  Crea una función que tome un nombre completo y una lista de empleados, busque el nombre
# completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario,
# devuelve un mensaje indicando que la persona no trabaja aquí:

lista32 = [('Pablo López Susarte', 'Gerente'), ('Ana González del Barrio', 'Supervisora'),
('Guillermo Paitán Carrasco', 'RRHH'), ('Hortensia Gómez Expósito', 'Secretaria')]
nombre32 = 'Ana González del Barrio'

def buscar_empleado (nombre_completo, lista_empleados):
    puesto_empleado = dict(lista_empleados).get(nombre_completo, 'La persona indicada no trabaja aquí')
    return puesto_empleado

solucion_32 = buscar_empleado(nombre32, lista32)
print('32 - Solución:', solucion_32)

####
#### 33 - Crea una función lambda que sume elementos correspondientes de dos listas dadas:

lista33_1 = [5, 6, 3, 7]
lista33_2 = [4, 2, 8, 11]

sumar_elementos_listas = lambda x, y: [x[i]+y[i] for i in range(len(x))]
solucion_33 = sumar_elementos_listas(lista33_1, lista33_2)
print('33 - Solución:', solucion_33)

####
#### 34 -  Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos.
# Los métodos disponibles son:

# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar
# estos métodos para manipular la estructura del árbol.

# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número
# de ramas y las longitudes de las mismas.

class Arbol:
    def __init__ (self, tronco=1, ramas=[]):
        self.tronco = tronco
        self.ramas = ramas

    def crecer_tronco (self):
        self.tronco += 1
        return self.tronco
    
    def nueva_rama (self, n=1):
        [self.ramas.append(1) for _ in range(n)]
        return self.ramas
    
    def crecer_ramas (self):
        self.ramas = [rama+1 for rama in self.ramas]
        return self.ramas
        
    def quitar_rama (self, posicion):
        self.ramas.pop(posicion)
        return self.ramas
    
    def info_arbol(self):
        def mostrar_ramas ():
            texto = ''
            for indice, rama in enumerate(self.ramas):
                texto +=(f'Número rama: {indice+1} - Longitud: {rama}\n')
            return str(texto)
        return print(f'''
Información del árbol:
----------------------
Longitud del tronco: {self.tronco}
Número de ramas: {len(self.ramas)}
Longitudes de las ramas:
{mostrar_ramas()}''')
    

# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

print('34 - Solución:')
arbol1 = Arbol()
arbol1.crecer_tronco()
arbol1.nueva_rama()
arbol1.crecer_ramas()
arbol1.nueva_rama(2)
arbol1.quitar_rama(2)
arbol1.info_arbol()

####
#### 36 -  Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo
# y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar
# dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True
# y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un
# error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario
# al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

class UsuarioBanco:
    def __init__ (self, nombre:str, saldo:int, cuenta_corriente:bool):
        self.nombre = nombre.title()
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero (self, cantidad_retirada):
        if cantidad_retirada <= self.saldo:   
            self.saldo -= cantidad_retirada
            print('Se ha retirado la cantidad indicada con éxito')
            return self.saldo
        else:
            print('No ha sido posible retirar la cantidad indicada. Saldo insuficiente.')
            return ValueError
    
    def transferir_dinero (self, cantidad_transferida:int, destinatario:object):
        if cantidad_transferida <= self.saldo:
            self.saldo -= cantidad_transferida
            destinatario.saldo += cantidad_transferida
            print('Se ha transferido la cantidad indicada con éxito')
            return self.saldo, destinatario.saldo
        else:
            print('No ha sido posible realizar la transferencia. Saldo insuficiente.')
            return ValueError

    def agregar_dinero (self, cantidad_añadida:int):
        self.saldo += cantidad_añadida
        print('Se ha agregado la cantidad indicada con éxito')
        return self.saldo
    
    def saldo_actual (self):
        return print(f'''
Nombre del usuario: {self.nombre}
Saldo actual: {self.saldo}''')


# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos
# con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".

print('36 - Solución:')
alicia = UsuarioBanco('alicia', 100, True)
bob = UsuarioBanco('bob', 50, True)
bob.agregar_dinero(20)
bob.transferir_dinero(80, alicia)
alicia.retirar_dinero(50)
bob.saldo_actual()
alicia.saldo_actual()

####
#### 37 - Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
# contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que
# tenemos que definir primero y llamar dentro de la función procesar_texto.

# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el
# texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una
# palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el
# texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar",
# "eliminar") y un número de argumentos variable según la opción indicada.

def procesar_texto (texto, opcion, *args):
    """Función para procesar un texto según la opción indicada.

    Args:
        texto (str): texto a editar
        opcion (str): Seleccionar una: 'contar', 'reemplazar' o 'eliminar'

    """
    def contar_palabras (texto): 
            #se crea un set con las palabras del texto
            set_palabras_texto = set()
            #creamos una lista de palabras, guardando en la variable solo las letras, cambiando los ' ' por '#'
            # y obviando el resto de caracteres
            simplificar_string = ''
            for c in texto:
                if c.lower() in 'aábcdeéfghiíjklmnñoópqrstuúvwxyz ':
                    simplificar_string += c
                else:
                    continue
            #dividimos el string partiendo por los espacios
            lista_palabras = simplificar_string.split(' ')
            #y guardamos cada palabra el un set, para que no estén repetidas
            [set_palabras_texto.add(palabra) for palabra in lista_palabras]
            #se cuentan cuantas veces aparecen repetidas cada palabra
            diccio_frecuencia_palabras = dict([(palabra, texto.count(palabra)) for palabra in set_palabras_texto])
            return print(f'\n--> CONTAR - Diccionario palabras:\n{diccio_frecuencia_palabras}')

    def reemplazar_palabras (palabra_antigua, palabra_nueva, texto):
        texto = texto.replace(palabra_antigua, palabra_nueva)
        print(f'\n--> REEMPLAZAR - La palabra "{palabra_antigua}" ha sido reemplazada por "{palabra_nueva}".')
        return print(texto)

    def eliminar_palabra (palabra_eliminada, texto):
        #primero dividimos el texto por la palabra a eliminar, porque no podemos cambiar un string
        nuevo_texto = texto.split(palabra_eliminada)
        #eliminamos posibles espacios
        nuevo_texto[1] = nuevo_texto[1].strip(' ')
        #reagrupamos el texto
        texto = ''.join(nuevo_texto)
        print(f'\n--> ELIMINAR - La palabra "{palabra_eliminada}" ha sido eliminada del texto.')
        return print(texto)

    if opcion == 'contar':
        contar_palabras(texto)
    elif opcion == 'reemplazar':
        palabra_antigua, palabra_nueva = args
        reemplazar_palabras(palabra_antigua, palabra_nueva, texto)
    elif opcion == 'eliminar':
        palabra_eliminada = args[0]
        eliminar_palabra(palabra_eliminada, texto)
    else:
        print('Seleccione una opción válida.')



# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

texto37 = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.'

print(f'\n37 - Solución:')
procesar_texto(texto37, 'contar')
procesar_texto(texto37, 'reemplazar', 'Mancha', 'España profunda')
procesar_texto(texto37, 'eliminar', 'hidalgo')

####
#### 38 - Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada
# por el usuario:

def momento_dia ():
    hora = datetime.datetime.now().time()
    if hora < datetime.time(5, 00, 00) or hora > datetime.time(21, 00, 00):
        return print('Ahora mismo es de noche.')
    elif hora < datetime.time(12,00,00):
        return print('Ahora mismo es por la mañana.')
    else:
        return print('Ahora mismo es por la tarde.')

print(f'\n38 - Solución:')
momento_dia()

####
#### 39 -  Escribe un programa que determine qué calificación en texto tiene un alumno en base a su 
# calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

def calificacion (nota):
    if nota < 70:
        return print('Insuficiente')
    elif nota < 80:
        return print('Bien')
    elif nota < 90:
        return print('Muy bien')
    else:
        return print('Excelente')

nota39 = 92

print('39 - Solución:')
calificacion(nota39)

####
#### 40 - Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo",
# "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura):

def calcular_area (figura, datos):

    if figura == 'rectangulo':
        base, altura = datos
        area = base * altura
        return print(f'Area del {figura}: {round(area, 2)}')

    elif figura == 'circulo':
        radio = datos[0]
        area = pi*radio**2
        return print(f'Area del {figura}: {round(area, 2)}')

    elif figura == 'triangulo':
        base, altura = datos
        area = base * altura / 2
        return print(f'Area del {figura}: {round(area, 2)}')

print('40 - Solución:')
calcular_area('rectangulo', (5, 6))
calcular_area('circulo', (4, ))
calcular_area('triangulo', (7, 2))

####
#### 41 -  En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales
# para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.
# El programa debe hacer lo siguiente:

# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido
# (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas
# acciones en tu programa de Python.

def compra_en_linea ():
    #pedimos que ingrese el valor original y gestionamos el posible error
    try:
        precio_original = int(input('Ingrese el precio original del artículo: '))
    except ValueError:
        return print('El valor del precio original debe ser un número válido.')
    #luego pedimos que ingrese si tiene cupón de descuento
    tiene_cupon = input('¿Tiene cupón de descuento? Escriba "SI" o "NO": ')
    if tiene_cupon.lower() == 'sí' or tiene_cupon.lower() == 'si':
        #y en caso afirmativo, pedimos añadir el valor del mismo y gestionamos posibles errores 
        try:    
            descuento = int(input('Ingrese el valor de descuento del cupón: '))
            if descuento > 0 and descuento < precio_original:
                precio_final = precio_original - descuento
            else:
                return print('El valor del cupón de descuento debe ser un número válido.')
        except ValueError:
            return print('El valor del cupón de descuento debe ser un número válido.')
    #si no tiene descuento el precio final es el original
    else:
        precio_final = precio_original
    #finalmenete devolvemos el valor final tras aplicar o no el descuento en cada caso
    return (f'El precio final es de {precio_final} €')

solucion_41 = compra_en_linea()
print(f'41 - Solución: {solucion_41}')