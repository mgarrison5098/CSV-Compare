import csv

def dedupe(file):
    id_arr = []

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] not in id_arr:
                id_arr.append(row[1])

    return id_arr

        
