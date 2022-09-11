import csv

with open('popuplist.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row[0]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+' '+row[1])