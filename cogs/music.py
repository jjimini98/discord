import discord
from discord import embeds
from discord.ext import commands
from youtube_dl import YoutubeDL

class Music(commands.Cog):
    def __init__(self, client):
        option = {
            'format': 'bestaudio/best',
            'noplaylist': True,
        }
        self.client = client 
        self.DL = YoutubeDL(option) #youtubeDL 객체 생성
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is Ready")

    @commands.command(name ="음악재생")
    async def play_music(self, ctx, url):
        url = url= url[1:len(url)]
        #봇의 음성 채널 연결이 없으면
        if ctx.voice_client is None: 
            # 명령어(ctx) 작성자(author)의 음성 채널에 연결 상태(voice)
            if ctx.author.voice:
                # 봇을 명령어 작성자가 연결되어 있는 음성 채널에 연결
                await ctx.author.voice.channel.connect()
            else:
                embed = discord.Embed(title = '오류 발생', description = "음성 채널에 들어간 후 명령어를 사용해 주세요!", color = discord.Color.red())
                await ctx.send(embed=embed)
                raise commands.CommandError("Author not connected to a voice channel.")
        # 봇이 음성채널에 연결되어 있고, 재생중이라면
        elif ctx.voice_client.is_playing():
            # 현재 재생중인 음원을 종료
            ctx.voice_client.stop()
        await ctx.send(url)
        
        embed = discord.Embed(title = '음악 재생', description = '음악 재생을 준비하고있어요. 잠시만 기다려 주세요!' , color = discord.Color.red())
        
        await ctx.send(embed=embed)

        data = self.DL.extract_info(url, download = False)
        link = data['url']
        title = data['title']

        ffmpeg_options = {
            'options': '-vn',
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        }
        player = discord.FFmpegPCMAudio(link, **ffmpeg_options, executable = "C:/ffmpeg/bin/ffmpeg")
        ctx.voice_client.play(player)
        
        embed = discord.Embed(title = '음악 재생', description = f'{title} 재생을 시작힐게요!' , color = discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.command(name ="유튜브")
    async def youtube_info(self, ctx, url):
        #내가 입력한 채팅에서는 임베드 안보이게 설정 
        url= url[1:len(url)] # 앞뒤 <> 제거 
        data = self.DL.extract_info(url, download = False)
        embed = discord.Embed(title = data['title'], url = url )
        embed.set_author(name = data['uploader'])
        embed.set_image(url = data['thumbnail'])
        embed.add_field(name="조회수",value=data['view_count'],inline=True)
        embed.add_field(name="평점",value=data['average_rating'],inline=True)
        embed.add_field(name="좋아요 수",value=data['like_count'],inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Music(client))

