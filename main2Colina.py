import json

from Grafos2.Grafos import Grafo

g = Grafo()
with open("Grafos2/grafo2.json", "r") as read_file:
    data = json.load(read_file)
    for padre in data:
        for hijo in data[padre]:
            g.agregarArista(padre, hijo, data[padre][hijo])

for v in g:
    for w in v.obtenerConexiones():
        print("( %s , %s ) %s" % (v.obtenerId(), w.obtenerId(), v.conectadoA[w]))


g.bsc(g.listaVertices["A"], g.listaVertices["M"])
