
m1=[[0,1,1,0],[1,0,0,1],[1,0,0,0],[0,1,0,0]]
m2=[[1,2,3,3],[4,5,6,3],[7,8,9,3],[2,3,4,1]]



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
    
def mostrarmatriz(m1):
    for fila in m1:
        print ("[", end= " ")
        for elemento in fila:
            print (elemento, end= " ")
        print ("]")
    print (":::::::::::::::::::::::::::::::::::::::::::::::::::::::")







mostrarmatriz(m1)
mostrarmatriz(m2)
mostrarmatriz(multiplicamatrices(m1,m2))
mostrarmatriz(sumar_matrices(m1,m1))
mostrarmatriz(matriz_caminos(m1,3))
mostrarmatriz(matriz_conexa(m1))
comprueba(matriz_conexa(m1))