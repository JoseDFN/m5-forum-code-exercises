def greet(nombre):
    """
    Función que muestra un saludo por pantalla.

    Parámetros:
    nombre (str): Nombre del usuario.

    Devuelve:
    Saludo personalizado con el formato ¡Hola <nombre>!.

    >>> greet("alf")
    '¡Hola Alf!'
    >>> greet("Python")
    '¡Hola Python!'
    >>> greet("")
    '¡Hola !'
    >>> greet("   ")
    '¡Hola    !'
    """
    return f'¡Hola {nombre}!'

# Pruebas Automáticas
if __name__ == '__main__':
    import doctest
    doctest.testmod()
