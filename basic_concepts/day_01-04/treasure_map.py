# 🚨 Don't change the code below 👇
from turtle import pos

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# convert_position = position.split(",")
# toString = str(convert_position[0]) + (convert_position[1])
# print(toString)

# if toString == "11":
#     row1[0] = " x"
# elif toString == "12":
#     row2[0] = " x"
# elif toString == "13":
#     row3[0] = " x"
# elif toString == "21":
#     row1[1] = " x"
# elif toString == "22":
#     row2[1] = " x"
# elif toString == "23":
#     row3[1] = " x"
# elif toString == "31":
#     row1[2] = " x"
# elif toString == "32":
#     row2[2] = " x"
# elif toString == "33":
#     row3[2] = " x"
# else:
#     print("\nTry Again\n")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal -1] = " X"

print(f"\n{row1}\n{row2}\n{row3}\n")



