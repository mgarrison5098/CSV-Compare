import sys, getopt
import csv
from util.configTests import configTests
from util.byteMath import byteMath
from util.parseMessage import parseMessage

test_arr = []
pass_arr = []


def main(argv):
    dataFile = ''


    try:
        opts, args = getopt.getopt(argv,"hd:t")
    except getopt.GetoptError:
        print('test.py -a <File A> -b <File B>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -a <File A> -b <File B>')
            sys.exit()
        elif opt in ("-d"):
            dataFile = arg
        elif opt in ("-t"):
            ag = [{"min_num": 0,"max_num": 20,"start": 2,"length": 22,"factor": 1.5},{"min_num": -500,"max_num": 500,"start": 0,"length": 12,"factor": .00075}]
            temp_arr = configTests(ag)
            for i in temp_arr:
                test_arr.append(i)
    
    with open(dataFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            runTest(row[1],row[3])
    
    print(pass_arr)
    
    
def runTest(id, data):
    for t in range(0, len(test_arr)):
        byte_int = byteMath(parseMessage(data), test_arr[t]['indexes'][0], test_arr[t]['indexes'][1], 'big', 1)
        byte_int = byte_int * test_arr[t]['factor']
        if byte_int <= test_arr[t]['max_num'] and byte_int >= test_arr[t]['min_num']:
            pass_arr.append([id, data])
        # else:
        #     print(id,data)
    
    


if __name__ == "__main__":
   main(sys.argv[1:])


# python3 compare.py -a '/Users/michaelgarrison/Downloads/without_radar.csv' -b '/Users/michaelgarrison/Downloads/with_radar.csv' -d '/Users/michaelgarrison/Downloads/toyota_nodsu_pt_generated.dbc'

# [{"min_num": 0,"max_num": 2,"start": 6,"length": 2,"factor": 1},{"min_num": 0,"max_num": 163.8,"start": 8,"length": 13,"factor": .02}]