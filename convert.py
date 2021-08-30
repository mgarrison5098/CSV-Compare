import sys, getopt
import struct

def main(argv):
    bytes = ''
    try:
        opts, args = getopt.getopt(argv,"hb:",)
    except getopt.GetoptError:
        print('test.py -a <File A> -b <File B>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -a <File A> -b <File B>')
            sys.exit()
        elif opt in ("-b"):
            bytes = arg
            print(bytes_to_int(bytes))
            print((-3).to_bytes(2, byteorder='big', signed=True))

def bytes_to_int(bytes):
    return int.from_bytes(b'\x0F\xF9', byteorder='big', signed=True)




if __name__ == "__main__":
   main(sys.argv[1:])
