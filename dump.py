import json

steamid = 76561197961793416

names = json.load(open("usernames.json"))["streamnames"]
index = (steamid % 2147483647) % len(names)

print(names[index])
