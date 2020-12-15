import random

from Grafos2.Cola import *


class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = 0
        self.predecesor = 0
        self.color = "blanco"

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerDistancia(self):
        return self.distancia

    def asignarDistancia(self, d):
        self.distancia = d

    def obtenerPredecesor(self):
        return self.predecesor

    def asignarPredecesor(self, p):
        self.predecesor = p

    def obtenerColor(self):
        return self.color

    def asignarColor(self, c):
        self.color = c

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]


class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0
        self.tiempo = 0

    def agregarVertice(self, clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.listaVertices

    def agregarArista(self, de, a, costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

    def clearColor(self):
        for unVertice in self:
            unVertice.asignarColor('blanco')

    def bea(self, verticeInicio, dato):
        if verticeInicio.obtenerId() == dato:
            return True
        colaVertices = Cola()
        colaVertices.agregar(verticeInicio)
        print(str(verticeInicio.id) + " => ", end="")
        while (colaVertices.tamano() > 0):
            verticeActual = colaVertices.avanzar()
            verticeActual.asignarColor('gris')
            for vecino in verticeActual.obtenerConexiones():
                if vecino.obtenerColor() == 'blanco':
                    print(str(vecino.id) + " => ", end="")
                    if vecino.obtenerId() == dato:
                        return True
                    vecino.asignarColor("gris")
                    colaVertices.agregar(vecino)
            verticeActual.asignarColor("negro")
        return False

    def bep(self, verticeInicio, dato, ban=False):
        print(str(verticeInicio.id) + " => ", end="")
        if ban:
            return ban
        if verticeInicio.obtenerId() == dato:
            return True
        verticeInicio.asignarColor('gris')
        for siguienteVertice in verticeInicio.obtenerConexiones():
            if siguienteVertice.obtenerColor() == 'blanco':
                ban = self.bep(siguienteVertice, dato, ban)
        verticeInicio.asignarColor('negro')
        return ban

    def bsc(self, verticeInicio, verticeFin):
        print(verticeInicio.id + " => ", end="")
        verticeMenor =None
        verticesMenores = []
        for vecino in verticeInicio.obtenerConexiones():
            if verticeMenor is None:
                verticeMenor = vecino
            else:
                if verticeInicio.conectadoA[verticeMenor] == verticeInicio.conectadoA[vecino]:
                    if not verticesMenores:
                        verticesMenores.append(verticeMenor)
                        verticesMenores.append(vecino)
                    else:
                        verticesMenores.append(vecino)
                if verticeInicio.conectadoA[verticeMenor] > verticeInicio.conectadoA[vecino]:
                    verticeMenor = vecino
                    verticesMenores.clear()
        if verticesMenores:
            verticeMenor = random.choice(verticesMenores)
        if verticeFin == verticeMenor:
            print("Acabo Busqueda")
        else:
            self.bsc(verticeMenor, verticeFin)
