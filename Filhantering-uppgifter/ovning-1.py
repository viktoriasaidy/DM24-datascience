import csv
with open("ovning-1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)