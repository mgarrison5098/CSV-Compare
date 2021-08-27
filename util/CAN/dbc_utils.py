import sys, getopt

class dbc: 
    def __init__(self, id, name): 
        self.id = id 
        self.name = name

def dbc_map(file):
    file1 = open(file, 'r')
    Lines = file1.readlines()
    dbc_list = []
    for index, row in enumerate(Lines, start=0):
        line = row.split()
        if len(line) >= 3 and line[0] == "BO_":
            dbc_list.append( dbc(line[1], line[2]) )
        elif len(line) >= 4 and line[0] == "CM_" and line[1] and line[1] == "SG_":
            dbc_list.append( dbc(line[2], line[3]) )
        elif len(line) >= 3 and line[0] == "VAL_":
            dbc_list.append( dbc(line[1], line[2]) )
    
    return dbc_list


def match_dbc(dbc_list, id_array):

    for item in id_array:
        temp = next((x for x in dbc_list if x.id == item), None)
        if temp and len(temp.id) and len(temp.name):
            print(temp.id, ", ",temp.name)
        else:
            print(item, ", UNKNOWN")
    print(">>>>>>>>>>>>EOF>>>>>>>>>>>>>")