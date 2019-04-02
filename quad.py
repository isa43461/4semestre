from sys import stdin
import sys

def pixels(arbol, profundidad):
	global suma
	if(len(arbol) == 5):
		for i in range(1,5):
			pixels(arbol[i], profundidad-1)
	elif(arbol == ['f']):
		suma += 2**(2*profundidad)
	return suma

def sumTree(img1, img2):
	if(img1[0] == 'f' or img2[0] == 'f'):
		return ['f']
	elif(img1[0] == 'e'):
		return img2
	elif(img2[0] == 'e'):
		return img1
	else:
		return ['p',sumTree(img1[1],img2[1]),sumTree(img1[2],img2[2]),sumTree(img1[3],img2[3]),sumTree(img1[4],img2[4])]

def constructTree(preOrder):
    global cont
    arbol = 0
    if cont < len(preOrder):
    	cont += 1
    	if preOrder[cont] != 'p':
    		arbol = [preOrder[cont]]
    	else:
    		arbol = ['p',constructTree(preOrder),constructTree(preOrder),constructTree(preOrder),constructTree(preOrder)]
    return arbol
def main():
	global cont, suma
	cont = 0
	cases = int(stdin.readline())
	while(cases != 0):
		cont = -1
		img1 = stdin.readline().strip()
		#print(img1)
		x = constructTree(img1)
		#print(x)
		#print(cont)
		cont = -1
		img2 = stdin.readline().strip()
		y = constructTree(img2)
		#print(y)
		arbolito = sumTree(x,y)
		#print(arbolito)
		suma = 0
		resultado = pixels(arbolito, 5)
		print("There are",resultado,"black pixels.")
		cases -= 1
main()