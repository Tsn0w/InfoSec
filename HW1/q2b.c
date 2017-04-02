#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int input, output;

    if (argc != 2) {
        printf("USAGE: %s <number>\n", argv[0]);
        return -1;
    }

    input = atoi(argv[1]);

    asm ("MOV EBX, %0"
        :
        : "r"(input));

    asm (
        /* Your code starts here. */
        
        /* The algorithm took from http://stackoverflow.com/questions/11091422/iterative-version-of-modified-fibonacci-sequence */
        
        /* save registers values */
        "PUSH EBX;" // save n at stack
        "PUSH ECX;"
        "PUSH EDX;" 
        /* Done save all at stack */

        "MOV EAX, 0;" // set start of fibonacci.
        "MOV EDX, 1;" // set start of fibonacci.
        "CMP EBX, 0;" // check if n <= 0
        "JLE case0;" 
        "CMP EBX, 1;" // check if n = 1
        "JE case1;" 

        "FIBONACCI:;" // started the iteration from up to down
            "ADD EAX, EDX;" // f(i) = f(i-1) + f(i-2)
            "MOV ECX, EDX;" // temp = f(i)
            "MOV EDX, EAX;" // f(i-1) = f(i)
            "MOV EAX, ECX;" // f(i) = tmep
            "DEC EBX;" // i--
            "CMP EBX, 1;"
            "JGE FIBONACCI;"
            "JMP END;"

        "case1:;"
        "ADD EAX, 1;"
        "JMP END;"

        "case0:;"
        "ADD EAX, 0;"
        "JMP END;"

        "END:;"
        
        /* save registers values */
        "POP EBX;" // set EBX n again.
        "POP ECX;"
        "POP EDX;" 
    /* Done save all at stack */
        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
