
def isUnique(arr1,arr2):
    
    to_remove = []
    for row in arr1: 
        if row in arr2:
            to_remove.append(row)

    for item in to_remove:
        arr1.remove(item)
        arr2.remove(item)

    return[arr1,arr2]

