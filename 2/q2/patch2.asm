mov eax, 0x08048633
jmp eax
lea  eax, [ebp-0x40c]
movzx eax, word ptr[eax]
cmp eax, 0x2123
jne Dont_Be_Sad
lea eax, [ebp-0x40c+2]
push eax
mov eax, 0x08048460
call eax
mov eax, 0x08048662
jmp eax

Dont_Be_Sad:
mov eax, 0x0804863a
jmp eax