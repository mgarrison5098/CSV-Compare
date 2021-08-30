
def byteIndex(start,length):
    start_index = start // 8
    end_index = (start + length) // 8

    return(start_index,end_index)