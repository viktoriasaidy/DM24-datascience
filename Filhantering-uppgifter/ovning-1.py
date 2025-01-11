import csv
with open("ovning-1.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

    data[0].append("Category")
    for row in reader:
        print(row)