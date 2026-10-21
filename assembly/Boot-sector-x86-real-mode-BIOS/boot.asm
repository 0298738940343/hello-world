; nasm -f bin boot.asm -o boot.bin && qemu-system-x86_64 boot.bin
bits 16
org 0x7c00

    mov si, msg
.next:
    lodsb
    or al, al
    jz .done
    mov ah, 0x0e        ; BIOS teletype
    int 0x10
    jmp .next
.done:
    hlt
    jmp .done

msg db "Hello, World!", 0
times 510 - ($ - $$) db 0
dw 0xaa55
