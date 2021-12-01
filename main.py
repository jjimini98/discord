#1115 코드 (최종 코드)
import discord
from discord.ext import commands
import os


def main():
    prefix = '!'
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)
    
    for filename in os.listdir('./cogs'):
        if '.py' in filename:
            filename = filename.replace('.py','')
            client.load_extension(f'cogs.{filename}') # 모듈을 client(봇)에 추가. 반드시 함수는 setup
            


    @client.event
    async def on_message(message):  
        if message.author.bot:
            pass
        else:
            name = message.author.name
            channel = message.channel
            await channel.send(f"{name}님이 보내신 메세지를 확인했어요!")

            await client.process_commands(message)


    @client.event
    async def on_member_join(member):
        if member.dm_channel:
            channel = member.dm_channel
        else:
            channel = await member.create_dm()
        name = member.name
        await channel.send(f"{name}님, 안녕하세요! 알싸한 파이썬 서버에 오신걸 환영합니다.")

    @client.command(name = "추가")
    async def _load(ctx, extension):
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"{extension}이 추가 되었어요!")

    @client.command(name = "제거")
    async def _unload(ctx, extension):
        client.unload_extension(f"cogs.{extension}")
        await ctx.send(f"{extension}이 제거 되었어요!")

    @client.command(name = "새로고침")
    async def _reload(ctx, extension):
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"{extension}이 새로고침 되었어요!")






    with open('token.txt', 'r') as f:
        token = f.read()
    client.run(token)


if __name__ == '__main__':
    main()






#1112 코드     
# import discord
# from discord.ext import commands
# import os

# def main():
#     prefix = '!'
#     intents = discord.Intents.all()

#     client = commands.Bot(command_prefix=prefix, intents = intents)
    
#     with open('token.txt', 'r') as f:
#         token = f.read()

#     client.run(token)

# if __name__ == '__main__':
#     main()
# main.py

# 1113 코드 
# import discord
# from discord.ext import commands
# import os

# def main():
#     prefix = '!'
#     intents = discord.Intents.all()

#     client = commands.Bot(command_prefix=prefix, intents = intents)

#     #봇에 명령어를 등록해주는 데코레이터 
#     @client.command(name = 'ping')
#     async def _ping(ctx): #메세지의 문장 : ctx 
#         await ctx.send("pong!")

#     #방법 1 
#     # @client.command(name = '이름')
#     # async def _name(ctx):
#     #     await ctx.send("명령어를 입력하신 분의 이름은 Jimin 이네요!")
#     #방법 2
#     @client.command(name='이름')
#     async def _name(ctx):
#         answer = "명령어를 입력하신 분의 이름은 "+ctx.author.name+" 이네요!"
#         await ctx.send(answer)
#     # #채널 정보
#     # @client.command(name="채널정보")
#     # async def _channelInfo(ctx):
#     #     await ctx.send(ctx.channel)
#     #채널 이름
#     @client.command(name="채널이름")
#     async def _channelName(ctx):
#         answer = "해당 채널의 이름은 <"+ctx.channel.name+"> 이네요!"
#         await ctx.send(answer)



#     with open('token.txt', 'r') as f:
#         token = f.read()

#     client.run(token)


