from discord.ext import commands


class Homework(commands.Cog): 
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Homework Cog is Ready")

    @commands.command(name= "이름")
    async def name(self,ctx):
        # name = ctx.author.name
        await ctx.send(f"명령어를 입력하신 분의 이름은 {ctx.author.name} 이네요!")
    
def setup(client):
    client.add_cog(Homework(client))