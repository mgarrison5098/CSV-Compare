
def byteMath(byte_arr, start, end, order, sign):
    return int.from_bytes(getByteString(byte_arr, start, end), byteorder=order, signed=sign)


def getByteString(byte_arr, start, end):
    b_str = ""
    # print("BA=>", byte_arr, "Start:",start, "End:",end)
    if start <= len(byte_arr) and end+1 <= len(byte_arr):
        for byte in range(start, end+1):
            b_str += byte_arr[byte]
        
    return bytes.fromhex(b_str)