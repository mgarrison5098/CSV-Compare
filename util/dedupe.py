import csv
from collections import Counter

def dedupe(file):
    id_arr = []

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] not in id_arr:
                id_arr.append(row[1])

    return id_arr

def dedupe_arr(pass_arr, fail_arr, pass_obj_arr):
    pass_ct = Counter(pass_arr)
    fail_ct = Counter(fail_arr)
    export_arr = []

    for key in pass_ct.keys():
        if key in fail_ct.keys():
            export_arr.append({
                'id': key,
                'pass_count': list(pass_ct.values())[list(pass_ct.keys()).index(key)],
                'fail_count': list(fail_ct.values())[list(fail_ct.keys()).index(key)]
            })
        else:
          export_arr.append({
                'id': key,
                'pass_count': list(pass_ct.values())[list(pass_ct.keys()).index(key)],
                'fail_count': '0'
            }) 
    
    return export_arr
# list(myl.keys())[list(myl.values()).index(16)]

# list(myl.values())[list(myl.keys()).index(2)]
#     >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]
    
    


      
