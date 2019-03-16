.data
genero: .asciiz "Ingrese 1 si es hombre, 2 si es mujer: "
peso: .asciiz "Ingrese su peso: "
tipoBebida: .asciiz "Digite el numero que este asignado para su bebida:\nAguardiente(1), Vino(2), Cerveza(3), Ron(4), Tequila(5), Whisky(6): "
cantidad: .asciiz "Ingrese el numero de cantidad que desea (Si es aguardiente, ron o tequila, se sirve en shots de 30ml\nSi es vino se sirve en copa de 150 ml. Si es whisky se sirve en vasos de 40 ml y si es cerveza se entrega en latas de 296 ml.): "
prueba1: .asciiz "Es aguardiente\n"
prueba2: .asciiz "Es vino\n"
prueba3: .asciiz "Es cerveza\n"
prueba4: .asciiz "Es ron\n"
prueba5: .asciiz "Es Tequila\n"
prueba6: .asciiz "Es Whisky\n" 
pruebaGenM: .asciiz "Es hombre\n"
pruebaGenF: .asciiz "Es mujer\n" 
apto: .asciiz "La persona se encuentra apta para conducir\n"
noApto: .asciiz "La persona no está apta para conducir\n"
.text

main:
	#Imprimir pregunta genero
	li $v0, 4
	la $a0, genero
	syscall
	
	#Ingresa usuario genero
	li $v0, 5
	syscall
	
	#Guardar el dato ingresado por el usuario
	add $t0, $0, $v0
	
	#Imprimir pregunta Peso
	li $v0, 4
	la $a0, peso
	syscall
	
	#Ingresa usuario peso
	li $v0, 5
	syscall
	
	#Guardar el dato ingresado por el usuario
	add $t1, $0, $v0
	
	#Imprimir pregunta Tipo de bebida
	li $v0, 4
	la $a0, tipoBebida
	syscall
	
	#Ingresa usuario tipo de Bebida
	li $v0, 5
	syscall
	
	#Guardar el dato ingresado por el usuario
	add $t2, $0, $v0
	
	#Imprimir pregunta cantidad
	li $v0, 4
	la $a0, cantidad
	syscall
	
	#Ingresa usuario cantidad
	li $v0, 5
	syscall
	
	#Guardar el dato ingresado por el usuario
	add $t3, $0, $v0
		
	addi $t4, $0, 1	 #Comprueban que lo que ingresó el usuario es aguardiente
	beq $t4, $t2, aguardiente

	addi $t4, $0, 2	#Comprueban que lo que ingresó el usuario es vino
	beq $t4, $t2, vino

	addi $t4, $0, 3	#Comprueban que lo que ingresó el usuario es cerveza
	beq $t4, $t2, cerveza

	addi $t4, $0, 4	#Comprueban que lo que ingresó el usuario es ron
	beq $t4, $t2, ron

	addi $t4, $0, 5	#Comprueban que lo que ingresó el usuario es tequila
	beq $t4, $t2, tequila

	addi $t4, $0, 6	#Comprueban que lo que ingresó el usuario es whisky
	beq $t4, $t2, whisky
	
aguardiente: 	
	addi $t4, $0, 870
	mul $t5, $t4, $t3 #870 * cantidad -> 870 = 29 * 30
	addi $t4, $0, 8
	mul $t5, $t5, $t4 # 870 * cantidad * 8

	j indGenero

vino:
	addi $t4, $0, 1950
	mul $t5, $t4, $t3 #1950 * cantidad -> 1950 = 13 * 150
	addi $t4, $0, 8
	mul $t5, $t5, $t4 # 1950 * cantidad * 8

	j indGenero

cerveza:
	addi $t4, $0, 1184
	mul $t5, $t4, $t3 #1184 * cantidad -> 1184 = 4 * 296
	addi $t4, $0, 8
	mul $t5, $t5, $t4 # 1184 * cantidad * 8

	j indGenero

ron:
	addi $t4, $0, 1170
	mul $t5, $t4, $t3 #1170 * cantidad -> 1184 = 39 * 30
	addi $t4, $0, 8
	mul $t5, $t5, $t4 # 1170 * cantidad * 8
l
	j indGenero

tequila:
	
	addi $t4, $0, 1140
	mul $t5, $t4, $t3 #1140 * cantidad -> 1140 = 38 * 30
	addi $t4, $0, 8
	mul $t5, $t5, $t4 # 1184 * cantidad * 8

	j indGenero

whisky:	
	addi $t4, $0, 1600
	mul $t5, $t4, $t3 #1600 * cantidad -> 1600 = 40 * 40
	addi $t4, $0, 8
	mul $t5, $t5, $t4 # 1600 * cantidad * 8

	j indGenero

indGenero:
	
	addi $t6, $0, 1
	beq $t6, $t0, alcoholimetroHombre #Si t6 = 1 se va ala etiqueta de alcoholimetroHombre donde se ingresan los datos a la formula especial para los hombres
	j alcoholimetroMujer #En caso contrario se utiliza la formula de la mujer
	
alcoholimetroMujer:
	
	addi $t8,$0,6
	mul $t7,$t1,$t8 #Peso * 6
	div $t5, $t7 #gramosAlcohol / (peso * 6)
	mflo $t9 #Mueve al registro t9 lo que se encontraba en lo
	addi $t8,$0,100
	div $t9,$t8
	addi $t8, $0, 40
	bge $t9,$t8,comprobacion #si t9 >= que 40 la persona no está apta
	li $v0, 4
	la $a0, apto
	syscall
		
	li $v0, 10
	syscall
	
alcoholimetroHombre:

	addi $t8,$0,7
	mul $t7,$t1,$t8 #peso * 7
	div $t5, $t7 #gramosAlcohol / (peso * 7)
	mflo $t9 #Mueve al registro t9 lo que se encontraba en lo
	addi $t8,$0,100
	div $t9,$t8
	addi $t8, $0, 40
	bge $t9,$t8,comprobacion #si t9 >= que 40 la persona no está apta
	li $v0, 4
	la $a0, apto
	syscall
	li $v0, 10
	syscall

comprobacion:
	li $v0, 4
	la $a0, noApto
	syscall
	
	
