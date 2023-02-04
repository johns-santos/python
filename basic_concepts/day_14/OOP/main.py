from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes


# Construct a prettytable object
table = PrettyTable()
# Update content alignment using ALIGN attribute
table.align = "l"
# Using pretty table methods create a two column table
table.field_names = ["Pokemon Name", "Type"]
# Add rows to columns
table.add_rows(
    [
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
    ]
)
print(table)
print("")


# Do same as above. Create table, create columns using methods
table2 = PrettyTable()
# Using colortable(theme) attribute change color of table2 object.
table2 = ColorTable(theme=Themes.OCEAN)
table2.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table2.add_column("Type", ["Electric", "Water", "Fire"])
# Align content of columns to the LEFT using built in attribute
table2.align = "l"

print(table2)
print("")


x = PrettyTable()
x.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
1554769])
x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
869.4])
x.align = "l"

print(x)





