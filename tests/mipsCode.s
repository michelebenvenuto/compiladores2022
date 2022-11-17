addi $sp, $sp, -20
jal mainMain
innitFactorial:
   sw $ra 0($sp)
   li $t0, 0
   sw $t0, 4($sp)
factorialFactorial:
   sw $ra 0($sp)
   lw $t0, 4($sp)
   beq $t0, 0, IF0True
   j IF0False
IF0True:
   li $t1, 0
   sw $t1, 8($sp)
   move $t0, $t1
   j Next0
IF0False:
   beq $t0, 1, IF1True
   j IF1False
IF1True:
   li $t2, 1
   sw $t2, 8($sp)
   move $t1, $t2
   j Next1
IF1False:
   addi $sp, $sp, -12
   sub $t3, $t0, 1
   sw $t3, 4($sp)
   addi $sp, $sp , -16
   sw $t0, 0($sp)
   sw $t1, 4($sp)
   sw $t2, 8($sp)
   sw $t3, 12($sp)
   addi $sp, $sp , 16
   jal factorialFactorial
   addi $sp, $sp , -16
   lw $t0, 0($sp)
   lw $t1, 4($sp)
   lw $t2, 8($sp)
   lw $t3, 12($sp)
   addi $sp, $sp, 16
   addi $sp, $sp, 12
   mult $t3, $v0
   mflo $t2
   sw $t2, 8($sp)
   move $t1, $t2
Next1:
   move $t0, $t1
Next0:
   add $v0, $t0, $zero
   lw $ra, 0($sp)
   jr $ra
mulFactorial:
   sw $ra 0($sp)
   lw $t1, 4($sp)
   lw $t2, 8($sp)
   mult $t1, $t2
   mflo $t0
   add $v0, $t0, $zero
   lw $ra, 0($sp)
   jr $ra
innitMain:
   sw $ra 0($sp)
mainMain:
   sw $ra 0($sp)
   li $t0, 3
   sw $t0, 4($sp)
   addi $t9, $sp, 5
   li $t1, 4
   sw $t1, 8($sp)
   li $a0, 4
   li $v0, 9
   syscall
   sw $v0, 12($sp)
   addi $sp, $sp, -12
   sw $t0, 4($sp)
   sw $t1, 8($sp)
   addi $sp, $sp , -8
   sw $t0, 0($sp)
   sw $t1, 4($sp)
   addi $sp, $sp , 8
   jal mulFactorial
   addi $sp, $sp , -8
   lw $t0, 0($sp)
   lw $t1, 4($sp)
   addi $sp, $sp, 8
   addi $sp, $sp, 12
   sw $v0, 16($sp)
   addi $sp, $sp, -12
   sw $t0, 4($sp)
   addi $sp, $sp , -8
   sw $t0, 0($sp)
   sw $t1, 4($sp)
   addi $sp, $sp , 8
   jal factorialFactorial
   addi $sp, $sp , -8
   lw $t0, 0($sp)
   lw $t1, 4($sp)
   addi $sp, $sp, 8
   addi $sp, $sp, 12
   li $v0, 10
   syscall
