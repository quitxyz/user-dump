import json

steamid=xxx

quit=json.loads(open("usernames.json","r").read())["streamnames"]

v = steamid % 2147483647

v = v % len(quit)

print(quit[v])
