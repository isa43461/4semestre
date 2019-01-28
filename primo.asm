.data
	Sies: .asciiz "Si es primo"
.text
     main:
	addi $s1, $zero, 0 #a donde guardo suma = 0
	addi $s2, $zero, 18 #primo
	addi $s3, $zero, 2 # cantidad de veces que debe estar el ac
	addi $t0, $zero, 1 #i = 1
	
	while:
		bgt $t0, $s2, exit # cuando i sea mayor que el numero primo o no
		div $s2, $t0 #division n/i
		mfhi $t2 #residuo
		bne $t2, $0, jum #if(mod != 0) jump
		add $s1, $s1, 1  #a++
		add $t0, $t0, 1 #i++
		j while
	jum:
		add $t0, $t0, 1 #i++		
		j while
		
	exit:
		beq $s1, $s3, numbersEq	
		#finaliza el main
		li $v0, 10
		syscall
  	numbersEq:
     		li $v0, 4
     		la $a0, Sies
     		syscall
