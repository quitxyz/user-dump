# user-dump

user-dump is a lightweight python utility for calculating rust streamer mode usernames from steam ids.

initial s/o to [@realstrings](https://github.com/realstrings/rust-de-stream-mode) for extracting the original game functions and username data.

combine this tool with battlemetrics and steam api data to help identify active players on rust servers.

## usage

requires python 3. no external dependencies.

set the steam id in `dump.py`:

```python
steamid = 76561197961793416
```

run the script:

```bash
python dump.py
```

the corresponding streamer mode username is printed to the console.

---

> <sub><b>archive note</b></sub>
>
> <sub>this is an older utility preserved for historical reference. its results matched all 17 tested lookups against a newer online tool, suggesting it may still work, although compatibility with current rust versions isn't guaranteed.</sub>
