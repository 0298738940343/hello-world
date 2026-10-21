; xa hello_6502.s -o hello.prg  (load with LOAD"HELLO",8,1 then SYS 49152)
        * = $c000
chrout  = $ffd2
        ldx #0
loop    lda msg,x
        beq done
        jsr chrout
        inx
        bne loop
done    rts
msg     .asc "HELLO, WORLD!", 13, 0
