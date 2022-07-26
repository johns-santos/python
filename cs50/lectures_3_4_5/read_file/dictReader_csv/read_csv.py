import csv

names = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append({"name": row["name"], "age": row["age"]})

for person in sorted(names, key=lambda person: person["name"]):
    print(f"{person['name']} is {person['age']} years old")