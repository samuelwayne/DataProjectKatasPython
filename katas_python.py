# 1 - Función que cuente la frecuencia de las letras en un string, exceptuar espacios:
def contar_frecuencia_letras (texto):
    """ Esta función cuenta la frecuencia de aparición de las letras en el texto pasado como argumento,
    sin contar los espacios y devuelto finalmente en forma de diccionario.

    Args:
        texto (str): Texto pasado a la función, únicamente usando letras y espacios.
                     Otros caracteres pueden generar errores.
    """
    
    # Mediante esta list comprehension guardamos cada tipo de letra distinto en un set
    set_letras_texto = set()
    [set_letras_texto.add(letra) for letra in texto if letra != ' ']

    # Mediante una list comprehension creamos cada par de clave valor y convertimos la lista en diccionario
    diccio_frecuencia_letras = dict([(letra, texto.count(letra)) for letra in set_letras_texto])

    return diccio_frecuencia_letras

solucion_1 = contar_frecuencia_letras('Cuantas letras tiene este texto')
print('1 - Solución en forma de diccionario:', solucion_1)


# 2 - De una lista de números, obtener una con el doble de cada valor usando map()
print('2 - Solución en forma de lista usando una lista de números aleatoria y usando map():',
       list(map(lambda x: x*2, [0, 1, 2, 5, 8, 9, 6, 6, 14])))

# 3 - 