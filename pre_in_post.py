from sys import stdin

def postorder(tree, L):
	if(type(tree) != list):
		if tree != None:
			L.append(tree)
	else:
		postorder(tree[1], L)
		postorder(tree[2], L)
		L.append(tree[0])
	return L

def arbol(listaIn, listaPre):
    if(len(listaIn) == 0):
        return None
    raiz = listaPre[0]
    i = listaIn.index(raiz)
    izq = arbol(listaIn[:i], listaPre[1:i+1])
    der = arbol(listaIn[i+1:], listaPre[i+1:])
    return [raiz,izq, der]

def main():
	global G
	cases = int(stdin.readline())
	while(cases != 0):
		lista = stdin.readline().strip().split()
		num, preorder, inorder = map(str,lista)
		num = int(num)
		nw = arbol(inorder, preorder)
		L = []
		pos = postorder(nw, L)
		cadena = ''.join(pos)
		print(cadena)
		cases -= 1
main()