#!/usr/bin/python

import subprocess

ASSEMBLY_TEMPLATE = '''
.intel_syntax noprefix
.globl main
main:
%s
'''

ASSEMBLE = 'gcc -xassembler - -o /dev/stdout -m32 -nostdlib -emain -Xlinker --oformat=binary'

def run(command, stdin):
    proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = proc.communicate(stdin)
    if stderr:
        raise RuntimeError(stderr)
    return stdout

def assemble_data(data):
    return run(ASSEMBLE, ASSEMBLY_TEMPLATE % data)
    
def assemble_file(path):
    return assemble_data(open(path, 'rb').read())

def main(path):
    try:
        print('%r' % assemble_file(path))
    except RuntimeError as error:
        print(error)

if __name__ == '__main__':
    import os, sys
    if len(sys.argv) != 2:
        print('USAGE: %s <file>' % os.path.basename(sys.argv[0]))
        sys.exit(1)
    main(path=sys.argv[1])
