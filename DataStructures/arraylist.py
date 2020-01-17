"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Dario Correal
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo implementa una estructura de datos lineal, como una lista cuyos elementos 
  estan en posiciones coniguas en memoria.
"""


def newList ():
    """
    Crea una lista vacia
    """
    new_list = {'elements':[], 'size':0 }
    return (new_list)


def addFirst(lst, element):
    """
    Agrega un elemento en la primera posición de la lista
    """
    lst['elements'].insert (0,element)
    lst['size'] += 1



def addLast(lst, element):
    """
    Agrega un elemento en la última posición de la lista
    """
    lst['elements'].append (element)
    lst['size'] += 1



def isEmpty (lst):
    """
    Indica si la lista está vacía
    """
    return lst['size'] == 0


def size(lst):
    """
    Informa el número de elementos de la lista
    """
    return lst['size'] 


def firstElement (lst):
    """
    Retorna el primer elemento de la lista, sin eliminarlo. La lista no puede ser vacía
    """
    return lst['elements'][0]



def lastElement (lst):
    """
    Retorna el último elemento de la lista, sin eliminarlo. La lista no puede ser vacía
    """
    return lst['elements'][lst['size']-1]



def getElement (lst, pos):
    """
    Retorna el elemento en la posición pos de la lista sin eliminarlo
    pos debe ser mayor que cero y menor o igual al tamaño de la lista
    la lista no esta vacia
    """
    return lst['elements'][pos-1]


def removeFirst (lst):
    """
    Remueve el primer elemento de la lista y lo retorna. La lista no puede ser vacía
    """
    element = lst['elements'].pop(0)
    lst['size'] -= 1
    return element


def removeLast (lst):
    """
    Remueve el último elemento de la lista y lo retorna en caso de existir, de lo contrario retorna None
    """
    element = lst['elements'].pop(lst['size']-1)
    lst['size'] -= 1
    return element

def insertElement (lst, element, pos):
    """
    Inserta el elemento element en la posición pos de la lista. pos debe ser menor o igual al tamaño de la lista. 
    """
    lst['elements'].insert (pos-1,element) 
    lst['size'] += 1


def changeInfo (lst, pos, newinfo):
    """
    Cambia la informacion contenida en el nodo de la lista en la posicion pos
    """
    lst['elements'][pos-1] = newinfo

def exchange (lst, pos1, pos2):
    """
    Intercambia la informacion en las posiciones pos1 y pos2 de la lista
    """
    infopos1 = getElement (lst, pos1)
    infopos2 = getElement (lst, pos2)
    changeInfo (lst, pos1, infopos2)
    changeInfo (lst, pos2, infopos1)
