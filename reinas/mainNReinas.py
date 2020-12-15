import copy
import random

tablero = []
nReinas = 4
posDesbloqueada = []


def marcarSeleccion(s):
    y = int(s / 4)
    x = (s % 4)
    tablero[y][x] = 1
    desbloqueadaLocal.remove(s)
    marcarBloqueos(x, y)


def marcarBloqueos(x, y):
    # bloquear horizontal
    for i in range(nReinas):
        if i != x:
            bloquearPosicion(i, y)
    # bloquear vertical
    for i in range(nReinas):
        if i != y:
            bloquearPosicion(x, i)
    # bloquear los diagonales
    x1 = x - y
    x2 = x + y
    for i in range(nReinas):
        if i != y:
            bloquearPosicion(x1, i)
            bloquearPosicion(x2, i)
        x1 += 1
        x2 -= 1
    print(tablero)
    print(desbloqueadaLocal)


def bloquearPosicion(x, y):
    if -1 < x < nReinas and -1 < y < nReinas:
        if tablero[y][x] != 2:
            tablero[y][x] = 2
            pos = (y * nReinas) + x
            if pos in desbloqueadaLocal:
                desbloqueadaLocal.remove(pos)


def llenasPosiciones():
    k = 0
    for i in range(nReinas):
        for j in range(nReinas):
            posDesbloqueada.append(k)
            k += 1

############Inicio
k = 0
for i in range(nReinas):
    filas = []
    for j in range(nReinas):
        filas.append(0)
        posDesbloqueada.append(k)
        k += 1
    tablero.append(filas)

tablerocopia = copy.deepcopy(tablero)
soluciones = []
n = nReinas
while len(soluciones) != 2:
    if not posDesbloqueada:
        llenasPosiciones()

    desbloqueadaLocal = copy.deepcopy(posDesbloqueada)
    sel = []
    print()
    print(desbloqueadaLocal)
    print()
    while n < 0 or desbloqueadaLocal:
        seleccion = random.choice(desbloqueadaLocal)
        if n == 4:
            posDesbloqueada.remove(seleccion)
        print(seleccion)
        sel.append(seleccion)
        marcarSeleccion(seleccion)
        n -= 1
    if n == 0:
        if not soluciones:
            sel.append(tablero)
            soluciones.append(sel)
        else:
            con = 0
            for w in soluciones:
                if w in sel:
                    con += 1
            if con != 4:
                sel.append(tablero)
                soluciones.append(sel)
    tablero = copy.deepcopy(tablerocopia)
    n = nReinas

##imprimir resultados final
for w in soluciones:
    print()
    tablero = w[4]
    for d in tablero:
        print(d)
