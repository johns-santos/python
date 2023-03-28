# Read CSV and generate a subset. Create a new CSV with specified data.

import pandas

# Read CSV
data = pandas.read_csv("./2018_squirrel_census.csv")

# Return rows containing <red, black, grey) squirrels
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])


# Convert data to python dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}


# Create a data frame
df = pandas.DataFrame(data_dict)

# Direct data frame output to csv
df.to_csv("squirrel_count.csv")
