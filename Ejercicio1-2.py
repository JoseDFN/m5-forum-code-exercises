def check_age(nombre, edad):
    """
    Función que evalúa si una persona es mayor o menor de edad y muestra un
    mensaje personalizado.

    Parámetros:
    nombre (str): Nombre de la persona.
    edad (int): Edad de la persona.

    Devuelve:
    Un mensaje indicando si la persona es mayor o menor de edad.

    >>> check_age("Ana", 20)
    'Hola Ana, eres mayor de edad.'
    >>> check_age("Luis", 16)
    'Hola Luis, eres menor de edad.'
    >>> check_age("Pedro", -5)
    'Error: La edad debe ser un número positivo.'
    """
    if edad < 0:
        return 'Error: La edad debe ser un número positivo.'
    elif edad >= 18:
        return f'Hola {nombre}, eres mayor de edad.'
    else:
        return f'Hola {nombre}, eres menor de edad.'

# Pruebas Automáticas
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    nombre = input("Ingrese un nombre: ")
    edad = int(input("Ingrese su edad: "))
    print(check_age(nombre, edad))