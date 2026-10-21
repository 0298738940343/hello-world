    .data
msg: .ascii "Hello, World!\n"
len = . - msg

    .text
    .globl _start
_start:
    mov r0, #1
    ldr r1, =msg
    mov r2, #len
    mov r7, #4          @ sys_write
    swi #0
    mov r0, #0
    mov r7, #1          @ sys_exit
    swi #0
