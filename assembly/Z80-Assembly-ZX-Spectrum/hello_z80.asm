; z80asm hello_z80.asm  -> run at 32768 on a ZX Spectrum
        org 32768
        ld a, 2             ; upper screen
        call 5633           ; open channel
        ld hl, msg
loop:   ld a, (hl)
        or a
        ret z
        rst 16              ; print char
        inc hl
        jr loop
msg:    defm "Hello, World!"
        defb 13, 0
