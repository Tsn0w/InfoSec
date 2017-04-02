import os

import infosec


def error(message):
    print('\x1b[31m{}\x1b[0m'.format(message))


def check_if_compiles(source_path):
    exit_code, stdout, stderr = infosec.utils.execute('gcc -masm=intel {source_path} -o /dev/null')
    if exit_code != 0:
        error('ERROR: {} does not compile:\n{}'.format(source_path, stderr))
        return False
    return True


def check_if_nonempty(path):
    with open(path) as reader:
        data = reader.read().strip()
    if not data:
        error('ERROR: {} is empty'.format(path))
        return False
    return True


def check_fibonacci(source_path):
    try:
        with infosec.utils.TemporaryDirectory() as temporary_directory_path:
            target_path = os.path.join(temporary_directory_path, 'q2')
            exit_code, stdout, stderr = infosec.utils.execute('gcc -masm=intel {source_path} -o {target_path}')
            a0 = int(infosec.utils.execute('{target_path} 0').stdout)
            a1 = int(infosec.utils.execute('{target_path} 1').stdout)
            if a0 != 0 or a1 != 1:
                error('ERROR: Fibonacci sequence should begin with 0, 1, ..., not with {}, {}, ...'.format(a0, a1))
                return False
            return True
    except Exception:
        return False


def smoketest():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if all([
        check_if_compiles('q1.c'),
        check_if_compiles('q2a.c'),
        check_if_compiles('q2b.c'),
        check_if_nonempty('q3.txt'),
        check_fibonacci('q2a.c'),
        check_fibonacci('q2b.c'),
    ]):
        print('smoketest seems cool')


if __name__ == '__main__':
    smoketest()
