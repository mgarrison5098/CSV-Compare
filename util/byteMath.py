
def byteMath(bytes, start, end, order, sign):
    int.from_bytes(b'\x0F\xF9', byteorder=order, signed=sign)

def getByteString(bytes, start, end):
    b_str = ""
    print(int.from_bytes(b'\x0F\xFE', byteorder="big", signed=True))
