# user-dump

user-dump is a lightweight python utility for calculating rust streamer mode usernames from steam ids.

initial s/o to [@realstrings](https://github.com/realstrings/rust-de-stream-mode) for extracting the original game functions and username data.

combine this tool with battlemetrics and steam api data to help identify active players on rust servers.

## usage

requires python 3.

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
> <sub>this tool is pretty old, while archiving this I quickly tested some cases and all of them worked against other working services.</sub>
