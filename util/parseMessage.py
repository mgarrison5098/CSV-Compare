
def parseMessage(msg):
    tmp = []
    for i in range(0, len(msg), 2) :
        if msg[i]:
            if i+1 in range(len(msg)):
                str = msg[i] + msg[i+1]
                tmp.append(str)
            elif i in range(len(msg)):
                str = msg[i]
                tmp.append(str)
        else:
            break

    return tmp