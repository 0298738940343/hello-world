org 100h

    mov dx, msg
    mov ah, 9           ; DOS print string
    int 21h
    mov ax, 4C00h       ; exit
    int 21h

msg db "Hello, World!", 13, 10, "$"
