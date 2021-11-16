from discord.ext import commands
from datetime import datetime

class Submit_mogakco(commands.Cog): 
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("submit_mogakco Cog is Ready")
        
    @commands.command(name= "모각코과제제출")
    async def submit_mogakco(self,ctx,arg=None):
        if arg == None: 
            await ctx.send(f"==============================={datetime.now().date()}모각코 과제===============================")
        else: 
            await ctx.send(f"===============================모각코 {arg}일차 과제===============================") 
            
def setup(client):
    client.add_cog(Submit_mogakco(client))