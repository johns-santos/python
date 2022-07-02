#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a LIST in a DICTIONARY
travel_log = {
    "France": ["Paris", "Lille","Dijon"],
    "Germany" : ["Berlin","Hamburg","Stuttgart"]
}

# print(travel_log["Germany"])

#Nesting many DICTIONARIES in a LIST
travel_log_01 = [
    {
    "country" : "France",  # String
    "cities_visited": ["Paris", "Lille","Dijon"], # List
    "total_visits": 12 # Int
    },
    {
    "country" : "Germany", 
    "cities_visited": ["Berlin","Hamburg","Stuttgart"], 
    "total_visits": 8
    },
    {
    "country" : "United States", 
    "cities_visited": ["Chicago","New York","Dallas"], 
    "total_visits": 15
    },
]

print("\n")

# for each in travel_log_01:
#         print(each)


# Function taht adds new dictionary to existing LIST
# def add_new_country(country, cities_visited, total_visits):
#     travel_log_01.append({
#         "country" : country,
#         "cities_visited" : cities_visited,
#         "total_visits": total_visits
#         })

# Function taht adds new dictionary to existing LIST
def add_new_country(country_visited, cities_visited, times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = times_visited
    travel_log_01.append(new_country)
    

add_new_country("Russia", ["Moscow", "Saint Petersberg", "Odessa"], 2)

for each in travel_log_01:
    print(each)

