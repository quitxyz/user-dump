import json

steamid=xxx

quit=json.loads(open("usernames.json","r").read())["RandomUsernames"]

v = steamid % 2147483647

v = v % len(quit)

print(quit[v])
