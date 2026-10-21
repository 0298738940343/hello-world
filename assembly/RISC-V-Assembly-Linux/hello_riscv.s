    .data
msg: .ascii "Hello, World!\n"

    .text
    .globl _start
_start:
    li a0, 1            # stdout
    la a1, msg
    li a2, 14
    li a7, 64           # sys_write
    ecall
    li a0, 0
    li a7, 93           # sys_exit
    ecall
