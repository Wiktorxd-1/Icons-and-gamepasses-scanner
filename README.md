
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
WEBHOOK_URL = ""  # Your Discord webhook URL
GAME_IDS = [8737899170, 18901165922]  # Place IDs of the games you want to monitor
```





For any issues or questions, please DM me on Discord: **Wiktorxd_1**.
