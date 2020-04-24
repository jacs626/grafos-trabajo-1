
m1=[[1,2],[3,4],[5,6]]
m2=[[1,2,3],[4,5,6]]

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

def mostrarmatriz(m1):
    for fila in m1:
        print ("[", end= " ")
        for elemento in fila:
            print (elemento, end= " ")
        print ("]")

mostrarmatriz(m1)
mostrarmatriz(m2)
mostrarmatriz(multiplicamatrices(m1,m2))