// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
@0
D=M
@2
M=0
//if R[1]=0, jump to end
(LOOP)
@1
D=M
@END
D; JEQ
//else, we got here - add @0 to @2
@0
D=M
@2
M=M+D
@1
M=M-1
@LOOP
0; JMP
(END)
@END
0;JMP
