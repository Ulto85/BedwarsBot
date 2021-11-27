import requests
from bs4 import BeautifulSoup
import discord

client = discord.Client()
class MinceCraft():
    def __init__(self):
        pass
    def get_solo_wins(self,player):
        url = 'https://plancke.io/hypixel/player/stats/'+player+'#BedWars'
        page = requests.get(url)
        supper = BeautifulSoup(page.content,'html.parser')
        try:
            n = supper.find_all('table')[1].find_all('tr')[2].find_all('td')[6].get_text()
        except:
            n = supper.find_all('table')[2].find_all('tr')[2].find_all('td')[6].get_text()
        return n
    def get_double_wins(self,player):
        url = 'https://plancke.io/hypixel/player/stats/'+player+'#BedWars'
        page = requests.get(url)
        supper = BeautifulSoup(page.content,'html.parser')
        try:
            n = supper.find_all('table')[1].find_all('tr')[3].find_all('td')[6].get_text()
        except:
            n = supper.find_all('table')[2].find_all('tr')[3].find_all('td')[6].get_text()
        return n
minecraft = MinceCraft()
prev_wins = minecraft.get_double_wins('USERNAME')
token="YOUR_TOKEN"

@client.event
async def on_ready():
    print(f'{client.user}')
@client.event
async def on_message(message):
    global prev_wins
    if message.author == client.user:
        return
    if str(message.author) == 'USER#IDNUMBER':
       
        current_wins=minecraft.get_double_wins('USERNAME')
        if current_wins>prev_wins:
            prev_wins=current_wins
        else:
            await message.delete()
            msg=f'''```USERNAME has {current_wins} out of the minimum of {int(prev_wins)+1} wins needed to send a message```'''.upper()
            await message.channel.send(msg)
            
            



client.run(token)
