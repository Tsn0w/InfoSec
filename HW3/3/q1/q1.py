import os, sys


PATH_TO_SUDO = './sudo'


def run_command(cmd):
    os.execl(PATH_TO_SUDO, __file__, "DontBeSad" + chr(1), cmd)


def main(argv):
    if not len(argv) == 2:
        print 'Usage: %s <command>' % argv[0]
        sys.exit(1)

    cmd = argv[1]
    run_command(cmd)


if __name__ == '__main__':
    main(sys.argv)
