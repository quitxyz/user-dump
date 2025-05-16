import json

steamid=76561197961793416

names=json.loads(open("usernames.json").read())["streamnames"]

v = (steamid % 2147483647) % len(names)

print(names[v])