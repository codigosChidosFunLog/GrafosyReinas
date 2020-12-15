import json

from Grafos2.Grafos import Grafo

g = Grafo()
with open("Grafos2/grafo1.json", "r") as read_file:
    data = json.load(read_file)
    for padre in data:
        for hijo in data[padre]:
            g.agregarArista(int(padre), hijo)

for v in g:
    for w in v.obtenerConexiones():
        print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))

print("Busqueda en Profundidad")
g.clearColor()
if g.bep(g.listaVertices[10], 26):
    print("El dato Existe")
else:
    print("El dato no  Existe")
print()
######################################
print("Busqueda en Anchura")
g.clearColor()
if g.bea(g.listaVertices[10], 14):
    print("El dato Existe")
else:
    print("El dato no  Existe")