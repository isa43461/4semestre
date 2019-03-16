from collections import deque
from sys import stdin

def toposort(letra):
    global resul, Grafo, visitados
    visitados[ord(letra) - 65] = 1
    ady = Grafo[ord(letra) - 65]
    for i in ady:
        if not (visitados[ord(i) - 65] != 0):
            toposort(i)
    resul.append(letra)

def main():
    global visitados, resul, Grafo
    resul, lista, palabras = [], [], []
    lista = stdin.readline().strip()
    visitados = [0 for i in range(26)]
    indeg = [-1 for _ in range(26)]
    while lista != "":
        if lista != "#":
        	palabras.append(lista)
        else:
            for i in range(len(palabras)):
                for j in range(len(palabras[i])):
                    indice = ord(palabras[i][j]) - 65 
                    indeg[indice] = 0 
            Grafo = [[] for _ in range(26)] 
            for i in range(len(palabras)-1):
                if len(palabras[i ]) <len(palabras[i+1]):
                    lim = len(palabras[i])
                else:
                    lim = len(palabras[i + 1])
                comp = palabras[i][:0]
                comp2 = palabras[i+1][:0]
                iter = 0
                while(comp == comp2):
                    iter += 1
                    comp = palabras[i][:iter]
                    comp2 = palabras[i+1][:iter]
                    if(iter <= lim): 
                        if comp != comp2:
                            indeg[ord(comp2[len(comp)-1])-65] += 1
                            Grafo[ord(comp[len(comp)-1])-65].append(comp2[len(comp) - 1])
            for i in range(len(indeg)):
                if (indeg[i] == 0):
                    src = chr(i + 65)
            toposort(src)
            resul = resul[::-1]
            for i in resul:
                print(i, end = "")
            print()
            resul = []
            indeg = [-1 for _ in range(26)]
            visitados = [0 for i in range(26)]
            palabras =[]
        lista = stdin.readline().strip()
main()
