addi $sp, $sp, -16
jal mainMain
innitMain:
mainMain:
   add $t0, $t0, 4
   sw $t0, 0($sp)
   add $t1, $t1, 5
   sw $t1, 8($sp)
   add $t2, $t2, 6
   sw $t2, 12($sp)
   blt $t0, 5, IF0True
   j IF0False
IF0True:
   add $t3, $t3, $t1
   sw $t3, 4($sp)
   add $t0, $t3, $zero
   j Next0
IF0False:
   add $t4, $t4, $t2
   sw $t4, 4($sp)
   add $t0, $t4, $zero
Next0:
   add $v0, $t0, $zero
