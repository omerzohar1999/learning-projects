// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


(START)
@SCREEN
D=A
@R0
M=D
@8192
D=D+A
@R1
M=D
@KBD
D=M
@LIGHTEN
D; JEQ
(BLACKEN)
@R0
D=M
(BLACKLOOP)
@R0
D=M
A=D
M=-1
D=D+1
@R0
M=D
@R1
D=M-D
@BLACKLOOP
D; JGT

@START
0; JMP
(LIGHTEN)
@R0
D=M
(LIGHTLOOP)
@R0
D=M
A=D
M=0
D=D+1
@R0
M=D
@R1
D=M-D
@LIGHTLOOP
D; JGT

@START
0; JMP