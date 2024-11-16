import aiohttp
import asyncio
from datetime import datetime
from pymongo import MongoClient

mongo_client = MongoClient("mongodb+srv://{database_user}:{pass}@{cluser_name}.{host}/?retryWrites=true&w=majority&appName={cluser_name}") # your mongo db login token
db = mongo_client["roblox"]
game_passes_collection = db["gamepasses"]
icons_collection = db["icons"]

GAME_IDS = [8737899170, 18901165922] # place ids of games you want, not universe ids (pre set to ps99 and pet go)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Cookie": ".ROBLOSECURITY=_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_303553ADD0E171445BF93E513DEFEAD85FF01174EE806D72F2E5EFE84784A439A06D3D33E2B939074ADF6FA7D675FEEA6AB40E886A49E5B6DC479C22A06D26420CEC31B08F04D7807BB226C3B8093AA96CDE24A7CB526FE6B08BE8E474D4F9965D346939C83BDF7191758C841F402A2E8535546C5A09578E8F8D3142168F97E0CD5D0285262CDBC0041FD214A25A16D19454DC409186B08A8183A2445B88D6078C83BA31160E2EA03115F4283495411B724729550676FDB2BAD87040265739E48D6899BFDEFEE985663937C2D53AEE79F628298644849EA0A85005C44543A22C24CD657F00329CEAC9F49FCBE1A36BC45CFDA47859A80148D1F1E70B8F0A57CDE9D53918D6DE87EB46A97428790A612E8E1BBC3A944844CDF422061C7CB831B26042C492CDD643388F9CCB04832B01CE28533E7E2ABD4D5EA39405493796FE6569339D6F3112FE64F9B10D56EB2539BE3362D7526AED76E9BA3E4B617B1B3AF7153D47E16F8B97AD84455545A5831B6002BDC7A11D107C962551A3C8414A644F638F70BC99CFD1B07F04149720FB2C52F0FD0BA7892DA7A3BDABD48D63FA558257FE1359E3964D1233B153C3D894137099319D5F471AD013265D5571A3227B219D46574DA713B446725B2DD34D24DF988857B19B3C36EC60212DC053B1D2F5594CB78B520409C3415C50237F8782F9CC700546C0A28BBB65B458C1F9FE303D26BBAE9B4E7AB1C7978444A3691264C0FD587737BB36A5C825F44DD6803D2CF1E4C895153A436E17E87952F69FDAE796A8681EBFB1D1568693E131DAC2023EB56AB9B4DD1BCF07E7E497CA30192CAB8D2D350AD7FEBBBD7F3AE30BD9C2592CC68CF7CCA054BFC24C717A1C9094DE9EFF2B8FA43CB54A8E6E56449181751D8F683BD1D527027EA0B02C36F0732600C51C9288F57761A709F863EE94C2CD787761AEB7C6D0282B82CD2BB2A52B5D259BF67F1F7A24A370BEB0CBDED491A8507BD60802D200AD0434B09ECBC9444B107FE46E8357A59D81D1E0F3C9410B32535F4B618749A90F2EFBF46632F0EA5E0893BDFE7F21857E3119A552F6A664DB18235EE433D6C65066639CEA89FE05BD2C951106551CE7DC81E7C42D644E7167C62215603450F701; rbxas=ba3c49c0d55d0fa554d57ce37c2465742944a6577076e357db56a69af6429601; RBXEventTrackerV2=CreateDate=11/13/2024 06:19:37&rbxid=7575088351&browserid=1731500344560002"
} # dont change this unless you want to use another account for this

place_details_url = "https://games.roblox.com/v1/games/multiget-place-details?placeIds={place_id}"
game_passes_url = "https://games.roblox.com/v1/games/{universe_id}/game-passes?limit=100&sortOrder=Asc"
product_info_url = "https://apis.roblox.com/game-passes/v1/game-passes/{target_id}/phttpsroduct-info"
WEBHOOK_URL = "" # webhook

async def fetch_universe_id(session, place_id):
    async with session.get(place_details_url.format(place_id=place_id), headers=headers) as response:
        data = await response.json()
        if data and isinstance(data, list) and len(data) > 0:
            return data[0]["universeId"], data[0]["name"]
        return None, None

async def fetch_game_passes(session, universe_id):
    async with session.get(game_passes_url.format(universe_id=universe_id), headers=headers) as response:
        data = await response.json()
        return data.get('data', [])

async def fetch_product_info(session, target_id):
    async with session.get(product_info_url.format(target_id=target_id), headers=headers) as response:
        data = await response.json()
        return data

def format_created_date(created_date):
    if created_date is None:
        return "Unknown"
    timestamp = datetime.fromisoformat(created_date[:-1])
    discord_timestamp = int(timestamp.timestamp())
    return f"<t:{discord_timestamp}:R>"

async def store_game_pass_data(game_pass_info, universe_id):
    game_pass_data = {
        "id": game_pass_info.get("id"),
        "name": game_pass_info.get("name"),
        "description": game_pass_info.get("description"),
        "priceInRobux": game_pass_info.get("priceInRobux"),
        "created": game_pass_info.get('created'),
        "iconImageAssetId": game_pass_info.get('iconImageAssetId'),
        "universeId": universe_id
    }
    
    print(f"Storing Game Pass Data: {game_pass_data}")
    

    game_passes_collection.update_one(
        {"id": game_pass_data["id"]},
        {"$set": game_pass_data},
        upsert=True
    )

async def compare_game_passes(old_info, new_info):
    changes = []
    if old_info['name'] != new_info['name']:
        changes.append(f"Name: **{old_info['name']}** ➜ **{new_info['name']}**")
    
    if old_info.get('description') != new_info.get('description'):
        changes.append(f"Description: **{old_info.get('description', 'N/A')}** ➜ **{new_info.get('description', 'N/A')}**")
        
    if old_info.get('priceInRobux') != new_info.get('priceInRobux'):
        changes.append(f"Price: **{old_info['priceInRobux']}⏣** ➜ **{new_info['priceInRobux']}⏣**")
        
    if old_info.get('iconImageAssetId') != new_info.get('iconImageAssetId'):
        changes.append(f"Icon Image: **Old:** https://ps99.biggamesapi.io/image/{old_info['iconImageAssetId']} ➜ **New:** https://ps99.biggamesapi.io/image/{new_info['iconImageAssetId']}")

    return changes

async def send_webhook(game_pass_info, game_name, game_pass_id, game_id, changes=None):
    embed_data = {
        "title": f"Game Pass: {game_pass_info.get('name', 'Unknown')}",
        "description": game_pass_info.get("description", "No description available."),
        "fields": [
            {"name": "Price", "value": str(game_pass_info.get("priceInRobux", "N/A")) + " ⏣"},
            {"name": "Game", "value": f"[{game_name}](https://roblox.com/games/{game_id})"},
            {"name": "Game Pass URL", "value": f"https://www.roblox.com/game-pass/{game_pass_id}"},
            {"name": "Created", "value": format_created_date(game_pass_info.get('created'))}
        ],
        "image": {"url": f"https://ps99.biggamesapi.io/image/{game_pass_info.get('iconImageAssetId', 0)}"},
        "footer": {"text": "Made by Wiktorxd_1 :3"}, # pwease leave this :3
        "color": 0x0000FF
    }
    
    if changes:
        if embed_data["description"] is None:
            embed_data["description"] = ""
        embed_data["description"] += "\n\n**Updates:**\n" + "\n".join(changes)

    async with aiohttp.ClientSession() as session:
        response = await session.post(WEBHOOK_URL, json={"embeds": [embed_data]}, headers=headers)
        if response.status == 204:
            print("Webhook sent successfully!")
        else:
            print(f"Failed to send webhook. Status: {response.status}. Response: {await response.text()}")

async def scan_gamepasses():
    async with aiohttp.ClientSession() as session:
        while True:
            for place_id in GAME_IDS:
                universe_id, game_name = await fetch_universe_id(session, place_id)
                if universe_id is None:
                    continue
                
                game_passes_data = await fetch_game_passes(session, universe_id)
                for game_pass in game_passes_data:
                    product_info = await fetch_product_info(session, game_pass["id"])
                    
                    current_info = {
                        'id': game_pass.get("id"),
                        'name': game_pass.get('name'),
                        'description': game_pass.get('Description'),
                        'priceInRobux': product_info.get("PriceInRobux"),
                        'created': product_info.get('Created'),
                        'iconImageAssetId': product_info.get('IconImageAssetId')
                    }

                    previous_info = game_passes_collection.find_one({"id": current_info["id"]})

                    if previous_info:
                        changes = await compare_game_passes(previous_info, current_info)
                        if changes:
                            await store_game_pass_data(current_info, universe_id)
                            await send_webhook(current_info, game_name, game_pass["id"], place_id, changes)
                    else:
                        await store_game_pass_data(current_info, universe_id)
                        await send_webhook(current_info, game_name, game_pass["id"], place_id)

            await asyncio.sleep(30)

async def get_game_details(game_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://games.roblox.com/v1/games/multiget-place-details?placeIds={game_id}"
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            if isinstance(data, list) and data:
                game = data[0]
                universe_id = game.get('universeId')
                game_name = game.get('name')
                new_url = game.get("url", "")
                return game, universe_id, game_name, new_url
    return None, None, None, None

async def get_game_icon(universe_id):
    async with aiohttp.ClientSession() as session:
        icon_url = f"https://thumbnails.roblox.com/v1/games/icons?universeIds={universe_id}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false"
        async with session.get(icon_url, headers=headers) as response:
            icon_data = await response.json()
            if 'data' in icon_data and icon_data['data']:
                return icon_data['data'][0].get('imageUrl', "")
    return None

async def store_icon_data(game_id, icon_url):
    icon_data = {
        "game_id": game_id,
        "icon_url": icon_url,
        "timestamp": datetime.now()
    }
    icons_collection.update_one({"game_id": game_id}, {"$set": icon_data}, upsert=True)

async def send_update_embed(game_name, game_id, universe_id, old_url, new_url, icon_url):
    embed = {
        "title": f"{game_name} Icon Updated",
        "color": 16711680,
        "fields": [
            {"name": "Time", "value": f"<t:{int(datetime.now().timestamp())}:R>", "inline": False},
            {"name": "Game ID", "value": str(game_id), "inline": True},
            {"name": "Universe ID", "value": str(universe_id), "inline": True},
            {"name": "Old Icon", "value": old_url or "N/A", "inline": False},
            {"name": "New Icon", "value": icon_url or "N/A", "inline": False}
        ],
        "image": {"url": icon_url or ""},
        "footer": {"text": "Made by Wiktorxd_1 :3"} # please leave this, again :3
    }

    async with aiohttp.ClientSession() as session:
        await session.post(WEBHOOK_URL, json={"embeds": [embed]})

async def script_main():
    while True:
        for game_id in GAME_IDS:
            game, universe_id, game_name, new_url = await get_game_details(game_id)
            if game:
                icon_url = await get_game_icon(universe_id)
                existing_icon = icons_collection.find_one({"game_id": game_id})
                old_url = existing_icon["icon_url"] if existing_icon else "N/A"

                if icon_url and (old_url == "N/A" or old_url != icon_url):
                    await send_update_embed(game_name, game_id, universe_id, old_url, new_url, icon_url)
                    await store_icon_data(game_id, icon_url)

        await asyncio.sleep(5)

async def main():
    await asyncio.gather(scan_gamepasses(), script_main())

if __name__ == "__main__":
    asyncio.run(main())
