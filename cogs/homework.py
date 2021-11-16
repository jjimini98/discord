from discord.ext import commands
import json
import random 

#1116 과제 코드 
class Lunch(commands.Cog): 
    def __init__(self, client):
        self.client = client
        with open("cogs\data\lunch.json", "r", encoding="utf-8") as f:
            self.lunchDict = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Homework Lunch Cog is Ready")

    # @commands.command(name="점심메뉴골라줘")
    # async def homework_lunch(self,ctx, *args):
    #     if len(args) == 0: 
    #         categories = list(self.lunchDict.keys()) #딕셔너리 key값만 해당 
    #         category = random.choice(categories) # categories중에서 하나 선택 
    #         lunch = random.choice(self.lunchDict[category]) #categories 중에서 또 하나 선택 
    #         await ctx.send(f"오늘 점심은 {category} 그 중에서도 {lunch}가 어떠세요?")
    #     else: 
    #         categories = list(args)
    #         category =  random.choice(categories)
    #         lunch = random.choice(self.lunchDict[category])
    #         # await ctx.send(f"오늘 점심은 {category} 그 중에서도 {lunch}가 어떠세요?")
    #         await ctx.send(f"{categories[0]}이랑 {categories[1]}이면...{lunch} 어떠세요?")

    @commands.command(name="점심메뉴골라줘")
    async def homework_lunch(self,ctx, arg1 = None, arg2 = None):
        if arg1 == None and arg2 == None: 
            categories = list(self.lunchDict.keys()) #딕셔너리 key값만 해당 
            category = random.choice(categories) # categories중에서 하나 선택 
            lunch = random.choice(self.lunchDict[category]) #categories 중에서 또 하나 선택 
            await ctx.send(f"오늘 점심은 {category} 그 중에서도 {lunch}가 어떠세요?")
        else: 
            categories = list()
            categories.append(arg1)
            categories.append(arg2)
            category =  random.choice(categories)
            lunch = random.choice(self.lunchDict[category])
            await ctx.send(f"{arg1}이랑 {arg2}이면...{lunch} 어떠세요?")

def setup(client):
    client.add_cog(Lunch(client))


# 1115 과제 코드 
# class Homework(commands.Cog): 
#     def __init__(self, client):
#         self.client = client
    
#     @commands.Cog.listener()
#     async def on_ready(self):
#         print("Homework Cog is Ready")

#     @commands.command(name= "이름")
#     async def name(self,ctx):
#         # name = ctx.author.name
#         await ctx.send(f"명령어를 입력하신 분의 이름은 {ctx.author.name} 이네요!")
    
# def setup(client):
#     client.add_cog(Homework(client))


