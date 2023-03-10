"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Clase Stack para el proyecto.
class Stack(object):

    # Constructor de la clase Stack.
    def __init__(self, initial_values=[]):
        self.__stack = initial_values

    # Override de la función len(), retorna la cantidad de objetos del stack.
    def __len__(self):
        return len(self.__stack)

    # Representación en string del stack, retorna la propiedad self.__stack.
    def __repr__(self):
        return str(self.__stack)

    # Función que retorna si el stack está vacío o no.
    def is_empty(self):
        return (len(self.__stack) == 0)

    # Función que agrega un elemento a la cima del stack.
    def push(self, item):
        self.__stack.append(item)

    # Función que retorna el último elemento agregado al stack.
    def peek(self):
        return (self.__stack[-1] if (not self.is_empty()) else "")

    # Función que remueve el último elemento agregado al stack y lo retorna.
    def pop(self):
        last_element = (self.__stack[-1] if (not self.is_empty()) else "")
        try:
            self.__stack.pop(-1)
        except:
            pass
        return last_element
