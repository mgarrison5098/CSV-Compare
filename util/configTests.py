from util.byteIndex import byteIndex

def configTests(test_arr):

    processed_arr = []

    for t in range(0, len(test_arr)):
        min_num = test_arr[t]["min_num"]
        max_num = test_arr[t]["max_num"]
        indexes = byteIndex(test_arr[t]["start"], test_arr[t]["length"])
        factor  = test_arr[t]["factor"]
        
        obj = {
            "min_num" : min_num,
            "max_num" : max_num,
            "indexes" : indexes,
            "factor"  : factor
        }
        processed_arr.append(obj)

    return processed_arr

# [{"min_num": 0,"max_num": 20,"start": 2,"length": 22,"factor": 1.5},{"min_num": -500,"max_num": 500,"start": 0,"length": 12,"factor": .00075}]
# Returned -> [{'min_num': 0, 'max_num': 20, 'indexes': (0, 3), 'factor': 1.5}, {'min_num': -500, 'max_num': 500, 'indexes': (0, 2), 'factor': 0.00075}]