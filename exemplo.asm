addi $s0, $zero, 0
addi $s6, $zero, 6
addi $s1, $zero, 1
nop
nop
LOOP: beq $s0, $s6, EXIT
addi $s7, $s7, 2
nop
nop
add $s1, $s1, $s1
addi $s0, $s0, 1
nop
nop
j LOOP
nop
EXIT: addi $s6, $s6, 1
nop
sub $s6, $s6, $s1
