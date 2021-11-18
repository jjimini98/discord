import json

from discord.channel import StoreChannel 

with open("C:/Users/Jimin/PycharmProjects/discord/cogs/data/score.json","r", encoding= 'utf-8') as s:
        data = json.load(s)

sdict = sorted(dict.items(data))

for idx, name, score in enumerate(sdict):
    print(idx,name,score)