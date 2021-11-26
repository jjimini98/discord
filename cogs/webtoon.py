import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from discord.ext.commands.core import command
from discord.ext.commands.errors import CommandNotFound
import requests


class Webtoon(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Webtoon Cog is Ready")

    @commands.command(name='오늘웹툰')
    async def get_webtoon(self,ctx):
        url = "https://comic.naver.com/webtoon/weekday"
        headers = {'User-Agent': "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.select("#content > div.list_area.daily_all > div.col.col_selected")

    
        for x in range(1, 6):
            selector = f"#content > div.list_area.daily_all > div.col.col_selected > div > ul > li:nth-child({x}) > a"
            thumbnail = data[0].select_one(f"#content > div.list_area.daily_all > div.col.col_selected > div > ul > li:nth-child({x}) > div > a > img").get('src')
            title = data[0].select_one(selector).get('title')
            link = data[0].select_one(selector).get('href')
            embed = discord.Embed(title = title, color = discord.Color.blue())
            embed.set_thumbnail(url = thumbnail)
            embed.add_field(name = 'URL' , value = "https://comic.naver.com"+link)
            await ctx.send(embed = embed)
 


    
def setup(client):
    client.add_cog(Webtoon(client))
