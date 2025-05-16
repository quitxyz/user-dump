<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F3F3F3&center=true&vCenter=true&width=435&lines=rust;user-dumper" alt="Typing SVG: user-dumper" />
  </a>
</p>

## 🧾 Overview

`user-dump` allows you to reverse Rust's Streamer Mode name mapping by converting Steam IDs into their randomized in-game usernames.

Initial s/o [@realstrings](https://github.com/realstrings) for dumping the functions from the game code and file from the game files.

Combining this, with the data from BattleMetrics and the Steam API, you can streamline the identification of active players on your Rust server.

## Config

Copy and paste this into your markdown, and that's it. Simple!

Change the `steamid = xxx` value to your desired SteamId's.

If you want to do multiple at once simple, add change and add the following snippets (the second one has to be placed above the calcuation):

```python
steamids = [
    76561197961793416,
    7652537961793416,
    76561197963354416
]
```

```python
for steamid in steamids:
```
> [!WARNING]\
> The script won't execute if you don't include both additions for multiple dumping.

## Usage

```bash
python dumper.py
```

> i ain't gonna explain how to use it gang -- y'all smart enough
