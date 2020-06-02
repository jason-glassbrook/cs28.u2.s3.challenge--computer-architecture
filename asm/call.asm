; Demonstrate calls
;
; Expected output:
; 20
; 30
; 36
; 60

; MAIN

    LDI R1,MultiplyBy2AndPrint  ; Load R1 with the subroutine address

    ; multiply a bunch of numbers by 2 and print them
    LDI R0,10
    CALL R1

    LDI R0,15
    CALL R1

    LDI R0,18
    CALL R1

    LDI R0,30
    CALL R1

    HLT

; MultiplyBy2AndPrint
;
; Multiply a number in R0 by 2 and print it out

MultiplyBy2AndPrint:
    ADD R0,R0  ; or fake it by adding it to itself
    PRN R0
    RET
