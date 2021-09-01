
def byteMath(byte_arr, start, end, order, sign):
    return int.from_bytes(getByteString(byte_arr, start, end), byteorder=order, signed=sign)


def getByteString(byte_arr, start, end):
    b_str = ""
    for byte in range(start, end+1):
        b_str += byte_arr[byte]
        
    return bytes.fromhex(b_str)