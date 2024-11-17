
# Gamepass & Icon scanner

Scan gamepasses and Game icons with this script

## Requirements

- Python 3.14 or higher
- `aiohttp` library
- `pymongo` library
- `datetime` library
- `asyncio` library


Command to install:

```bash
pip install aiohttp pymongo datetime asyncio
```

## Configuration

Update theses varibles:

```python
mongo_client = MongoClient("mongodb+srv://{database_user}:{pass}@{cluser_name}.{host}/?retryWrites=true&w=majority&appName={cluser_name}")  # Your MongoDB connection string
GAMEPASS_GAME_IDS = [8737899170, 18901165922] # place ids of games for the gamepass scanning, not universe ids (pre set to ps99 and pet go)
ICONS_GAME_IDS = [8737899170, 18901165922]# place ids of games for game icon scanning, not universe ids (pre set to ps99 and pet go)
GAMEPASSES_WEBHOOK_URL = "" # webhook for gamepasses
ICONS_WEBHOOK_URL = "" # webhook for game icons

and if you want to turn off a function:

run_scan_gamepasses = True  # change to False if you don't want to use it
run_icons_enabled = True  # change to False if you don't want to use it

```





For any issues or questions, please DM me on Discord: **Wiktorxd_1**.
