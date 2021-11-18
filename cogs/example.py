# cog란 discord에서 제공하는 모듈화에 특화된 친구(?)
# 명령어를 여러개를 모아 하나의 클래스를 구성

from discord.ext import commands
import discord
# Example 클래스는 commands.Cog 클래스를 상속 
# commands.Cog는 모든 Cog 클래스가 상속해야하는 기반 클래스 .
class Example(commands.Cog): 
    def __init__(self, client):
        self.client = client
    
    #Example Cog가 실행 준비가 되었을 때 실행되는 이벤트 리스너를 등록
    @commands.Cog.listener()
    async def on_ready(self):
        print("Example Cog is Ready")

    @commands.command(name= "ping")
    async def _ping(self,ctx):
        await ctx.send("pong!")


    @commands.command(name = "임베드")
    async def embed(self, ctx):
        embed=discord.Embed(
            title="Embed의 제목입니다.",
            description="임베드 설명입니다.", 
            color=discord.Color.blue()
        )
        embed.set_author(
            name="Jimin", 
            url="https://cafe.naver.com/codeuniv", 
            icon_url="https://source.unsplash.com/random")


        embed.add_field(
            name="Field 1 Title", 
            value="This is the value for field 1. This is NOT an inline field.", 
            inline=False) 
        embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
        embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)

        embed.set_thumbnail(url="https://source.unsplash.com/random")
    
        await ctx.send(embed = embed)
        
# 함수 이름은 반드시 setup이어야 하고 인자로 봇 객체 하나만 받아야 함. 
def setup(client):
    client.add_cog(Example(client))