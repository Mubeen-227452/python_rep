import csv

with open('exp.txt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)