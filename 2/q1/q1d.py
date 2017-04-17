def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()

    num1 = int ("597", 16)
    num2 = int ("598", 16)
    num3 = int ("599", 16)
    num4 = int ("59A", 16)
    num5 = int ("59B", 16)
    num6 = int ("59C", 16)
    lst = list(data)
    lst[num1] = chr(int("b8", 16))
    lst[num2] = chr(int("1", 16))
    lst[num3] = chr(int("0", 16))
    lst[num4] = chr(int("0", 16))
    lst[num5] = chr(int("0", 16))
    lst[num6] = chr(int("90", 16))

    data = "".join(lst)

    with open(path + '.patched', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msgcheck-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))