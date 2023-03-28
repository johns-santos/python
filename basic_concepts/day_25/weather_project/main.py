# with open("./weather_data.csv") as weather_file:
#     weather_list = weather_file.readlines()
#     print(weather_list)




# import csv

# # TO REMOVE ALL spaces, commas, etc./ found in list
# # use CSV library to open read file and store data in csv.reader object
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # Loop over items in csv.reader object to access each
#     for row in data:
#         # Add temperatures from each row to a list as intergers
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
print(data["temp"])

print(" ")
# Convert panda dataframe to a dictionary
data_dict = data.to_dict()
print(data_dict)


print(" ")
# Convert panda series to a list
temp_list = data["temp"].to_list()
print(temp_list)

# Average temp
average = sum(temp_list)/len(temp_list)
print(average)

# Panda method to get average using - MEAN
print(data["temp"].mean())
  
 
# Panda method to get highest value - MAX   
print(data["temp"].max())


print("\n\n\n")

# Get Data in colums
print(data["condition"])

print("\n")
# Same as above - Get Data in colums
print(data.condition)



print("\nTEST TEST TEST")
# Obtain entire row by matching value
print(data[data.day == "Monday"])


print("\n")
# Highest temp of the week
highest = data[data.temp == data.temp.max()]
print(highest)      
 
print("\n")
print("test" )
print("\n")


sunday = data[data.day == "Sunday"]
sunday_temp_fahrenheit = (sunday.temp * 9/5) + 32
print(sunday_temp_fahrenheit)

print("\n")
monday = data[data.day == "Monday"]
monday_temp_fahrenheit = (int(monday.temp) * 9/5) + 32
print(monday_temp_fahrenheit)


print("\n")
#Create a data frame from python generated dict
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
print(data_dict)

studentData = pandas.DataFrame(data_dict)
print(studentData)
# Save to csv
studentData.to_csv("student_data.csv")



