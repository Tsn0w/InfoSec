import assemble as asm

def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    lst = list(data)

    offset1 = 0x633
    patch1 = asm.assemble_file("patch1.asm")
    for i in xrange(len(patch1)):
        lst[offset1 +  i] = patch1[i]

    offset2 = 0x5cd
    patch2 = asm.assemble_file("patch2.asm")
    for i in xrange(len(patch2)):
        lst[offset2 + i] = patch2[i]

    data = "".join(lst)

    with open(path + '.patched', 'wb') as writer:
        writer.write(data)

def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <readfile-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
