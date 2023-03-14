"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Clase Queue para el proyecto.
class Queue(object):

    # Constructor de la clase Queue.
    def __init__(self, initial_values=[]):
        self.__queue = initial_values

    # Override de la función len(), retorna la cantidad de objetos del queue.
    def __len__(self):
        return len(self.__queue)

    # Representación en string del queue, retorna la propiedad self.__queue.
    def __repr__(self):
        return str(self.__queue)

    # Función que retorna si el queue está vacío o no.
    def is_empty(self):
        return (len(self.__queue) == 0)

    # Función que agrega un elemento a la cima del queue.
    def push(self, item):
        self.__queue.append(item)

    # Función que retorna el último elemento agregado al queue.
    def peek(self):
        return (self.__queue[0] if (not self.is_empty()) else "")

    # Función que remueve el último elemento agregado al queue y lo retorna.
    def get(self):
        last_element = (self.__queue[0] if (not self.is_empty()) else "")
        try:
            self.__queue.pop(0)
        except:
            pass
        return last_element
