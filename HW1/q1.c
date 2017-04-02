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
    	
    	/* save registers values */
    	"PUSH EBX;" // save n at stack
    	"PUSH ECX;"
    	"PUSH EDX;" 
        /* Done save all at stack */

        "MOV ECX, 0;"
    	"CMP EBX, 1;" // in case given nubmer is not greater then 1
    	"JLE case1;"

    	"MOV ECX, 2;" // i = 2
    	"MOV EAX, EBX;" // EAX = n
    	"the_alg:;"
    	"MOV EDX, 0;" // set EDX to zero beacsuse div concating EDX:EAX
    	"MOV EBX, EAX;" // save EAX in case not divided.
    	"DIV ECX;" // does EAX/ECX, EDX = n % i, EAX = n / i
    	"CMP EDX, 0;" 
    	"JNE if_condition;"
    	"DEC ECX;" // i--
    	"JMP condition;"

    	// in case not divide need to retrun EAX as he was.
    	"if_condition:;"
    	"MOV EAX,EBX;"

    	"condition:;"
    	"ADD ECX, 1;"
    	"CMP ECX, EAX;"
    	"JG END;" // i <= n check
    	"JMP the_alg;"

    	"case1:;"
    	"MOV EAX, 0;"

    	"END:"
    	"MOV EAX, ECX;" // set answer at EAX as wanted
    	
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


/*
THE_ALGORITHM.
*** n is input
for (i = 2; i <= n; i++)
{
	if (n % i == 0)
	{
		n /= i;
		i--;
	}
}
retrun i;
*/