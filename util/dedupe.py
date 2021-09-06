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

def dedupe_arr(pass_arr, fail_arr, pass_obj_arr, fail_obj_arr):
    pass_ct = Counter(pass_arr)
    fail_ct = Counter(fail_arr)
    export_arr = []

    for key in pass_ct.keys():
        pass_min = []
        pass_max = []
        fail_min = []
        fail_max = []
        test_number = [element['test_num'] for element in pass_obj_arr if element['id'] == key]
        for test in Counter(test_number).keys():
            tmp_list = [telem['result'] for telem in pass_obj_arr if telem['id'] == key and telem['test_num'] == test]
            pass_min.append(min(tmp_list))
            pass_max.append(max(tmp_list))
            if key in fail_ct.keys():
                tmp_fail_list = [telem['result'] for telem in fail_obj_arr if telem['id'] == key and telem['test_num'] == test]
                if len(tmp_fail_list): 
                    fail_min.append((test,min(tmp_fail_list)))
                    fail_max.append((test,max(tmp_fail_list)))


        if key in fail_ct.keys():
            export_arr.append({
                'id': key,
                'pass_count': list(pass_ct.values())[list(pass_ct.keys()).index(key)],
                'fail_count': list(fail_ct.values())[list(fail_ct.keys()).index(key)],
                'min_val': str(pass_min),
                'max_val': str(pass_max),
                'fail_min':str(fail_min),
                'fail_max':str(fail_max)
            })
        else:
          export_arr.append({
                'id': key,
                'pass_count': list(pass_ct.values())[list(pass_ct.keys()).index(key)],
                'fail_count': '0',
                'min_val': str(pass_min),
                'max_val': str(pass_max)
            }) 

    return export_arr
# list(myl.keys())[list(myl.values()).index(16)]

# list(myl.values())[list(myl.keys()).index(2)]
#     >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]
    
    

# [{'id': "123", "test": 0, "result": "aaa"},{'id': "123", "test": 0, "result": "aaa"},{'id': "123", "test": 0, "result": "bbb"},{'id': "123", "test": 0, "result": "bbb"},{'id': "123", "test": 1, "result": "aaa"},{'id': "123", "test": 1, "result": "bbb"},{'id': "123", "test": 1, "result": "aaa"},{'id': "123", "test": 2, "result": "aaa"},{'id': "123", "test": 2, "result": "aaa"},{'id': "456", "test": 0, "result": "aaa"},{'id': "456", "test": 0, "result": "aaa"},{'id': "456", "test": 0, "result": "bbb"},{'id': "456", "test": 0, "result": "bbb"},{'id': "456", "test": 1, "result": "aaa"},{'id': "456", "test": 1, "result": "bbb"},{'id': "456", "test": 1, "result": "aaa"},{'id': "456", "test": 2, "result": "aaa"},{'id': "456", "test": 2, "result": "aaa"}]

      
# for key in pct.keys():
#         test_number = [element['test'] for element in parr if element['id'] == key]
#         for test in Counter(test_number).keys():
#             tmp_list = [telem['result'] for telem in parr if telem['id'] == key and telem['test_num'] == test]
#             print(tmp_list)