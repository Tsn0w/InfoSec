def check_message(path):
    i = 0
    num = 191
   
    try:
        file = open(path,"r")
    except:
        print ("ERROR: failed to open" + path + "\n")
        return -1
    
    try: 
        data = file.read(1024)
    except:
        print ("ERROR: failed to read" + path + "\n")
        file.close() 
        return -1
    
    char_at_0 = data[0]
    char_at_1 = data[1]
    
    while i < ord(char_at_0):
        if i + 2 >= len(data):
            file.close()
            return 1
        num ^= ord(data[i + 2])
        i += 1
    file.close()
    if num == ord(char_at_1):
        return 1
    return 0

def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    if check_message(path):
        print('valid message')
        return 0
    else:
        print('invalid message')
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
