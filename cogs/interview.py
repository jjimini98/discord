import discord
from discord.errors import HTTPException
from discord.ext import commands
import json
import random 
import sys
sys.path.append("C:/Users/Jimin/PycharmProjects/discord/cogs/data/")

class Interview(commands.Cog): 
    def __init__(self, client):
        self.client = client
        with open("cogs/data/interview.json", "r", encoding="utf-8") as f:
            self.interviewDict = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Interview Cog is Ready")


    @commands.command(name="면접질문")
    async def interview_question(self,ctx, arg = None):
        if arg == None: 
            categories = list(self.interviewDict.keys()) 
            category = random.choice(categories) 
        try:
            question = random.choice(self.interviewDict[category])
        except HTTPException: 
            question = random.choice(self.interviewDict[category])

        await ctx.send(question)


def setup(client):
    client.add_cog(Interview(client))