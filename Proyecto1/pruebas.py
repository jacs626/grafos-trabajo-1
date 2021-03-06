import sys
import fileinput
from collections import defaultdict 


#grafo general
grafo = {
'vertices': ['a','b','c','d'],
'aristas': set([
    (5,'a','c'),
    (3,'a','d'),
    (2,'b','d'),
    (1,'c','d'),
    (1,'a','b'),
    ])
}



aristas = list(grafo['aristas'])
vertices = list(grafo['vertices'])
aristas.sort()
tipo=1

mvacia=[]
for i in range(len(grafo['vertices'])):
    mvacia.append([])
    for j in range(len(grafo['vertices'])):
        mvacia[i].append(0)

def buscarincid (a):
    i=0
    while(True):
        if a == vertices[i]:
            return i
        else:
            i=i+1

madyacente=[]
madyacente=mvacia

for e in aristas:
    peso, u, v = e
    madyacente[buscarincid(u)][buscarincid(v)]+=peso
    if tipo==1:
        madyacente[buscarincid(v)][buscarincid(u)]+=peso    




def multiplicamatrices(m1,m2):
    m3=[]
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2[0])):
            m3[i].append(0)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                m3[i][j] += m1[i][k]*m2[k][j]
    return m3

def sumar_matrices(m1,m2):
    m3=[]
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1[0])):
            m3[i].append(m1[i][j]+m2[i][j])
    return m3

def matriz_caminos(m1,n):
    m0=[]
    for i in range(len(m1)):
        m0.append([])
        for j in range(len(m1[0])):
            if i==j:
                m0[i].append(1)
            else:
                m0[i].append(0)
    for i in range(n):
        m0=multiplicamatrices(m0,m1)
    return m0

def matriz_conexa(m1):
    m3=[]
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1[0])):
            m3[i].append(0)
    for i in range(len(m1[0])):
        m3=sumar_matrices(m3,matriz_caminos(m1,i))
    return m3

def comprueba(m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j]==0:
                print ("No es conexa")
                return
    print ("es conexa")

def comprueba2(m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j]==0:
                return False
    return True


    
def mostrarmatriz(m1):
    for fila in m1:
        print ("[", end= " ")
        for elemento in fila:
            print (elemento, end= " ")
        print ("]")
    print (":::::::::::::::::::::::::::::::::::::::::::::::::::::::")










base = dict()
ord = dict()   

def Genera_Conjunto(v):
    base[v] = v
    ord[v] = 0


def Buscar(v):
    if base[v] != v:
        base[v] = Buscar(base[v])
    return base[v]

def union(u, v):
    v1 = Buscar(u)
    v2 = Buscar(v)
    if v1 != v2:
        if ord[v1] > ord[v2]:
            base[v2] = v1 
        else:
            base[v1] = v2
            if ord[v1] == ord[v2]: 
                ord[v2] += 1

def kruskal(grafo):

    mst = set()
   
    for v in grafo['vertices']:
        Genera_Conjunto(v)

    for e in aristas:
        peso, u, v = e
        if Buscar(u) != Buscar(v):
            union(u, v)
            mst.add(e)
    return mst 

def ComprobarHamilt(m1):
    aux=0
    aux2=97
    Grados=[]
    GradosVert=[]
    for fila in m1:
        aux=0
        for elemento in fila:
            if (elemento != 0):
                aux+=1      
        Grados.append(aux)
        GradosVert.append(chr(aux2))
        aux2=aux2+1
    aux=0
    aux2=0
    aux3=1
    Ayuda=0
    while aux2!=len(Grados)-1:
        while aux3!=len(Grados)-1:
            if m1[aux][aux3]==0:
                if len(m1)-1<= Grados[aux]+Grados[aux3]:
                    print (" ")
                    Ayuda=0
                else:
                    print ("El grafo no es hamiltoniano")
                    Ayuda=1
                    break
            aux3+=1
        if (Ayuda==1):
            break
        aux+=1
        aux2+=1
        aux3=0
    if Ayuda==0:
        print ("Es Hamiltoniano")

def Euleriano(m1):
    aux=0
    aux2=1
    AuxVerificador=0
    Grados=[]
    for fila in m1:
        aux=0
        for elemento in fila:
            if (elemento != 0):
                aux+=1      
        Grados.append(aux)
        aux2=aux2+1
    Impar=0
    for elem in Grados:
        if elem%2!=0:
            Impar+=1
    if Impar==2:
        if comprueba2(matriz_conexa(m1)):
            AuxVerificador=1
            print ("El grafo es euleriano")
            return
        else:
            AuxVerificador=0
    if comprueba2((matriz_conexa(m1))):
        AuxVerificador=1
        print ("El grafo es euleriano")
        return
    if AuxVerificador==0:
        print ("El grafo no es euleriano")
        return


class Grafos: 
   
    def __init__(self,graph): 
        self.grafos = grafos
        self.fila = len(grafos) 
    def encontrarcamino(self,s, t, padre): 
        visitado =[False]*(self.fila) 
        cola=[] 
        cola.append(s) 
        visitado[s] = True
        while cola: 
            u = cola.pop(0) 
            for ind, val in enumerate(self.grafos[u]): 
                if visitado[ind] == False and val > 0 : 
                    cola.append(ind) 
                    visitado[ind] = True
                    padre[ind] = u 
        return True if visitado[t] else False
              
    def FordFulkerson(self, salida, llegada): 
  
        padre = [-1]*(self.fila)   
        max_flujo = 0 
        while self.encontrarcamino(salida, llegada, padre):
            camino_flujo = float("Inf") 
            s = llegada
            while(s !=  salida): 
                camino_flujo = min (camino_flujo, self.grafos[padre[s]][s]) 
                s = padre[s]
            max_flujo +=  camino_flujo
            v = llegada
            while(v !=  salida): 
                u = padre[v] 
                self.grafos[u][v] -= camino_flujo
                self.grafos[v][u] += camino_flujo
                v = padre[v] 
  
        return max_flujo

grafos = [[0,9,12,0,0,0,0],
[0,0,6,9,4,3,0],
[0,0,0,2,6,3,0],
[0,0,0,0,2,0,7],
[0,0,0,0,0,2,8],
[0,0,0,0,0,0,5],
[0,0,0,0,0,0,0]]

g=Grafos(grafos)


k = kruskal(grafo)


from collections import deque, namedtuple


# usaremos infinito como distancia para los nodos.
inf = float('inf')
Arista = namedtuple('Arista', 'start, end, peso')


def make_Arista(start, end, peso=1):
  return Arista(start, end, peso)


class Graph:
    def __init__(self, Aristas):
        # verifiquemos que los datos sean correctos
        wrong_Aristas = [i for i in Aristas if len(i) not in [2, 3]]
        if wrong_Aristas:
            raise ValueError('Wrong Aristas data: {}'.format(wrong_Aristas))

        self.Aristas = [make_Arista(*Arista) for Arista in Aristas]

    @property
    def vertices(self):
        return set(
            sum(
                ([Arista.start, Arista.end] for Arista in self.Aristas), []
            )
        )
###funciones de agregar y quitar.
    def get_nodo_pares(self, n1, n2, both_ends=True):
        if both_ends:
            nodo_pares = [[n1, n2], [n2, n1]]
        else:
            nodo_pares = [[n1, n2]]
        return nodo_pares

    def remove_Arista(self, n1, n2, both_ends=True):
        nodo_pares = self.get_nodo_pares(n1, n2, both_ends)
        Aristas = self.Aristas[:]
        for Arista in Aristas:
            if [Arista.start, Arista.end] in nodo_pares:
                self.Aristas.remove(Arista)

    def add_Arista(self, n1, n2, peso=1, both_ends=True):
        nodo_pares = self.get_nodo_pares(n1, n2, both_ends)
        for Arista in self.Aristas:
            if [Arista.start, Arista.end] in nodo_pares:
                return ValueError('Arista {} {} already exists'.format(n1, n2))

        self.Aristas.append(Arista(start=n1, end=n2, peso=peso))
        if both_ends:
            self.Aristas.append(Arista(start=n2, end=n1, peso=peso))

####################################  vecinos para cada nodo:
    @property
    def vecinos(self):
        vecinos = {vertice: set() for vertice in self.vertices}
        for Arista in self.Aristas:
            vecinos[Arista.start].add((Arista.end, Arista.peso))

        return vecinos

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source nodo doesn\'t exist'
        distancia = {vertice: inf for vertice in self.vertices}
        previo_vertices = {
            vertice: None for vertice in self.vertices
        }
        distancia[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            actual_vertice = min(
                vertices, key=lambda vertice: distancia[vertice])
            vertices.remove(actual_vertice)
            if distancia[actual_vertice] == inf:
                break
            for vecino, peso in self.vecinos[actual_vertice]:
                alternative_route = distancia[actual_vertice] + peso
                if alternative_route < distancia[vecino]:
                    distancia[vecino] = alternative_route
                    previo_vertices[vecino] = actual_vertice

        recorrido, actual_vertice = deque(), dest
        while previo_vertices[actual_vertice] is not None:
            recorrido.appendleft(actual_vertice)
            actual_vertice = previo_vertices[actual_vertice]
        if recorrido:
            recorrido.appendleft(actual_vertice)
        return recorrido

#grafo para dijkstra
graph = Graph([
    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
    ("e", "f", 9)])


print("matriz de caminos con indice 1")
mostrarmatriz(matriz_caminos(madyacente,1))
comprueba(matriz_conexa(madyacente))
print("Dijkstra:")
print(graph.dijkstra("a", "f"))
ComprobarHamilt(madyacente)
Euleriano(madyacente)
print("flujo max de salida 0 y llegada 6 es: %d " %g.FordFulkerson(0,6))
print ("subgrafo camino menos peso con kruskal:")
print (k)

