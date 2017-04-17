def fix_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    
    lst = list(data)
    lst[0] = chr(len(data) - 3)
    num = 191
    for i in xrange(ord(lst[0])):
        num ^= ord(lst[i+2])
    lst[1] = chr(num)
    data = "".join(lst)
    with open(path + '.fixed', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    fix_message(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
