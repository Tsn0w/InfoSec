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
        /* The code starts here */

    /* save registers values */
    "PUSH EBX;" // save n at stack
    "PUSH ECX;"
    "PUSH EDX;" 
    /* Done save all at stack */

	"FIBONACCI:;"
	"MOV EAX, 0;" // set EAX as 0.
	"MOV EDX, 0;"
	"CALL REC_FIBONACCI;"
	"JMP TRUE_END;"
	
	"REC_FIBONACCI:;"

	/* PROLOUGE */
	"PUSH EBP;"
	"MOV EBP, ESP;"
	/* PROLOUGE */

	// edge cases.
	"CMP EBX, 0;"
	"JLE CASE0;" // check if n = 0.
	"CMP EBX, 1;"
	"JE CASE1;" // chekc if n = 1.

	// will calc f(n-1).
	"PUSH EBX;" //save n.
	"DEC EBX;"
	"CALL REC_FIBONACCI;" // save at EAX the fibonnaci nubmer n-1.
	
	// will calc f(n-2).
	"POP EBX;"
	"SUB EBX, 2;" 
	"PUSH EAX;" // save n -1 fibonnaci nubmer.
	"CALL REC_FIBONACCI;" // save at EAX the fibonnaci nubmer n-2.
	
	// will calc f(n) , f(n) = f(n-1) + f(n - 2).
	"POP EDX;" // extract from stack fibonnaci nubmer n-1 to EDX.
	"ADD EAX, EDX;"
	"JMP END_REC;"


	"CASE0:;" // if EBX == 0.
	"MOV EAX, 0;"
	"JMP END_REC;"

	"CASE1:;" // if EBX == 1.
	"MOV EAX, 1;"
	"JMP END_REC;"

	"END_REC:;"
	/* EPILOGUE */
	"MOV  ESP, EBP;"
	"POP  EBP;"	
	/* EPILOGUE */ 
	"RET;"

	"TRUE_END:;"
	/* retrun the original value to each register */
    "POP EDX;" 
    "POP ECX;"
    "POP EBX;" 
    /* Done set register values back */

        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
