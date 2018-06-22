import csv

def readCSV(file):
    csv_file = csv.reader(open(file, 'r'))
    list=[]
    for item in csv_file:
        list.append(item)
    csvlist=[]
    for lists in list:
        listitems=lists[0].split('\t')
        csvlist.append(listitems)
    return csvlist