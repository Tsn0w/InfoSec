import os

import infosec


def error(message):
    print('\x1b[31m{}\x1b[0m'.format(message))


def check_q1a():
    with infosec.utils.in_directory('q1'):
        q1a = infosec.utils.import_module('q1a.py')
        if not q1a.check_message('01.msg'):
            error('ERROR: python q1a.py 01.msg should return True')
            return False
        if q1a.check_message('02.msg'):
            error('ERROR: python q1a.py 02.msg should return False')
            return False
        return True


def check_fix(name):
    with infosec.utils.in_directory('q1'):
        module = infosec.utils.import_module(name)
        module.fix_message('02.msg')
        if infosec.utils.execute('./msgcheck 02.msg.fixed').exit_code != 0:
            error('ERROR: msgcheck failed on 02.msg.fixed (generated by python {} 02.msg)'.format(name))
            return False
        return True


def check_patch(name):
    with infosec.utils.in_directory('q1'):
        module = infosec.utils.import_module(name)
        module.patch_program('msgcheck')
        os.chmod('msgcheck.patched', 0o700)
        if infosec.utils.execute('./msgcheck.patched 02.msg').exit_code != 0:
            error('ERROR: msgcheck.patched (generated by python {} msgcheck) failed on 02.msg'.format(name))
            return False
        return True


def check_q2():
    with infosec.utils.in_directory('q2'):
        module = infosec.utils.import_module('q2.py')
        module.patch_program('readfile')
        os.chmod('readfile.patched', 0o700)
        result = infosec.utils.execute('./readfile.patched 1.txt')
        if result.exit_code != 0:
            error('ERROR: readfile.patched failed on 1.txt')
            return False
        if '#!' in result.stdout:
            error("ERROR: readfile.patched doesn't seem to work as expected on 1.txt")
            return False
        return True


def check_if_nonempty(path):
    if not os.path.exists(path):
        error('ERROR: {} does not exist'.format(path))
        return False
    with open(path) as reader:
        data = reader.read().strip()
    if not data:
        error('ERROR: {} is empty'.format(path))
        return False
    return True


def smoketest():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if all([
        check_q1a(),
        check_if_nonempty('q1/q1a.txt'),
        check_fix('q1b.py'),
        check_if_nonempty('q1/q1b.txt'),
        check_fix('q1c.py'),
        check_if_nonempty('q1/q1c.txt'),
        check_patch('q1d.py'),
        check_if_nonempty('q1/q1d.txt'),
        check_patch('q1e.py'),
        check_if_nonempty('q1/q1e.txt'),
        check_patch('q1e.py'),
        check_if_nonempty('q1/q1e.txt'),
        check_q2(),
        check_if_nonempty('q2/q2.txt')
    ]):
        print('smoketest seems cool')


if __name__ == '__main__':
    smoketest()