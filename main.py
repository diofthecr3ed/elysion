f = open("registers/IX F T2.csv", 'r')
import csv
reader = csv.reader(f)
for row in reader:
    print(row)