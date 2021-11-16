import discord
from discord.ext import commands
import json
import random 


class Lunch(commands.Cog): 
    def __init__(self, client):
        self.client = client
        with open("cogs\data\lunch.json", "r", encoding="utf-8") as f:
            self.lunchDict = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lunch Cog is Ready")


    @commands.command(name="점심추천")
    async def recommand_lunch(self,ctx, arg = None):
        if arg == None: 
            categories = list(self.lunchDict.keys()) #딕셔너리 key값만 해당 
            category = random.choice(categories) # categories중에서 하나 선택 
            lunch = random.choice(self.lunchDict[category]) #categories 중에서 또 하나 선택 
            await ctx.send(f"오늘 점심은 {category} 그 중에서도 {lunch}가 어떠세요?")
        else :
            category = arg
            lunch = random.choice(self.lunchDict[category])
            await ctx.send(f"오늘 점심은 {lunch} 어떠세요? ")
    

def setup(client):
    client.add_cog(Lunch(client))