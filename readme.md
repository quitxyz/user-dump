# user-dump

user-dump is a lightweight Python utility for calculating Rust Streamer Mode usernames from Steam IDs.

Initial s/o to [@realstrings](https://github.com/realstrings/rust-de-stream-mode) for extracting the original game functions and username data.

Combine this tool with BattleMetrics and Steam API data to help identify active players on Rust servers.

## Usage

Requires Python 3. No external dependencies.

Set the Steam ID in `dump.py`:

```python
steamid = 76561197961793416
```

Run the script:

```bash
python dump.py
```

The corresponding Streamer Mode username is printed to the console.

---

> <sub><b>Archive note</b></sub>
>
> <sub>This is an older utility preserved for historical reference. Its results matched all 17 tested lookups against a newer online tool, suggesting it may still work, although compatibility with current Rust versions isn't guaranteed.</sub>
