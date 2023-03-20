statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(people_dict):
    count = 0
    for name, status in people_dict.items():
        if status == "online":
            count += 1
    return count

# # short version
# def online_count(people):
#     return len([p for p in people if people[p] == "online"])


print(online_count(statuses))


            