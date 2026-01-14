
import csv

with open('cilveki.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        print(f"{line[0]} {line[1]}")


    