
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

## Update:

update the headers, the account got banned because of someone or someone changed the password
if you need help getting the cookie dm me on discord

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Cookie": ".ROBLOSECURITY=_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_303553ADD0E171445BF93E513DEFEAD85FF01174EE806D72F2E5EFE84784A439A06D3D33E2B939074ADF6FA7D675FEEA6AB40E886A49E5B6DC479C22A06D26420CEC31B08F04D7807BB226C3B8093AA96CDE24A7CB526FE6B08BE8E474D4F9965D346939C83BDF7191758C841F402A2E8535546C5A09578E8F8D3142168F97E0CD5D0285262CDBC0041FD214A25A16D19454DC409186B08A8183A2445B88D6078C83BA31160E2EA03115F4283495411B724729550676FDB2BAD87040265739E48D6899BFDEFEE985663937C2D53AEE79F628298644849EA0A85005C44543A22C24CD657F00329CEAC9F49FCBE1A36BC45CFDA47859A80148D1F1E70B8F0A57CDE9D53918D6DE87EB46A97428790A612E8E1BBC3A944844CDF422061C7CB831B26042C492CDD643388F9CCB04832B01CE28533E7E2ABD4D5EA39405493796FE6569339D6F3112FE64F9B10D56EB2539BE3362D7526AED76E9BA3E4B617B1B3AF7153D47E16F8B97AD84455545A5831B6002BDC7A11D107C962551A3C8414A644F638F70BC99CFD1B07F04149720FB2C52F0FD0BA7892DA7A3BDABD48D63FA558257FE1359E3964D1233B153C3D894137099319D5F471AD013265D5571A3227B219D46574DA713B446725B2DD34D24DF988857B19B3C36EC60212DC053B1D2F5594CB78B520409C3415C50237F8782F9CC700546C0A28BBB65B458C1F9FE303D26BBAE9B4E7AB1C7978444A3691264C0FD587737BB36A5C825F44DD6803D2CF1E4C895153A436E17E87952F69FDAE796A8681EBFB1D1568693E131DAC2023EB56AB9B4DD1BCF07E7E497CA30192CAB8D2D350AD7FEBBBD7F3AE30BD9C2592CC68CF7CCA054BFC24C717A1C9094DE9EFF2B8FA43CB54A8E6E56449181751D8F683BD1D527027EA0B02C36F0732600C51C9288F57761A709F863EE94C2CD787761AEB7C6D0282B82CD2BB2A52B5D259BF67F1F7A24A370BEB0CBDED491A8507BD60802D200AD0434B09ECBC9444B107FE46E8357A59D81D1E0F3C9410B32535F4B618749A90F2EFBF46632F0EA5E0893BDFE7F21857E3119A552F6A664DB18235EE433D6C65066639CEA89FE05BD2C951106551CE7DC81E7C42D644E7167C62215603450F701; rbxas=ba3c49c0d55d0fa554d57ce37c2465742944a6577076e357db56a69af6429601; RBXEventTrackerV2=CreateDate=11/13/2024 06:19:37&rbxid=7575088351&browserid=1731500344560002"
}
```




For any issues or questions, please DM me on Discord: **Wiktorxd_1**.
