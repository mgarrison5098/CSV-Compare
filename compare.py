import sys, getopt
from util.dedupe import dedupe
from util.unique import isUnique
from util.CAN.dbc_utils import dbc_map
from util.CAN.dbc_utils import match_dbc

def main(argv):
    afile = ''
    bfile = ''
    dbcfile = ''
    try:
        opts, args = getopt.getopt(argv,"ha:b:d:",)
    except getopt.GetoptError:
        print('test.py -a <File A> -b <File B>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -a <File A> -b <File B>')
            sys.exit()
        elif opt in ("-a"):
            afile = arg
        elif opt in ("-b"):
            bfile = arg
        elif opt in ("-d"):
            dbcfile = arg
    
    unique_arr = isUnique(dedupe(afile),dedupe(bfile))
    map = dbc_map(dbcfile)
    match_dbc(map, unique_arr[0])
    match_dbc(map, unique_arr[1])


if __name__ == "__main__":
   main(sys.argv[1:])


# python3 compare.py -a '/Users/michaelgarrison/Downloads/without_radar.csv' -b '/Users/michaelgarrison/Downloads/with_radar.csv' -d '/Users/michaelgarrison/Downloads/toyota_nodsu_pt_generated.dbc'