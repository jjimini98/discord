import discord
from discord.ext import commands
import csv
import random 
import asyncio
import json 

class Quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.quizDict = {}
        # self.scoreDict = {} #이것도 여기서 관리하는게 맞나.. 
        # self.score = 0 #이걸 여기서 관리하는게 맞나.. 
        with open("C:/Users/Jimin/PycharmProjects/discord/cogs/data/quiz.csv", 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.quizDict[row[0]] = row[1]

    @commands.Cog.listener()
    async def on_ready(self):
        print("Quiz Cog is Ready")

    @commands.command(name="퀴즈")
    async def quiz(self,ctx):
        problemList = list(self.quizDict.keys()) #여기서 딕셔너리의 key는 문제임 
        problem = random.choice(problemList) #문제 리스트에서 하나 랜덤으로 추출 
        answer = self.quizDict[problem] #문제에 해당하는 value가 answer 변수에 들어감 
        # await ctx.send(problem) #문제 출력 
        embed = discord.Embed(title = '퀴즈', description = problem, color = discord.Color.blue())
        await ctx.send(embed=embed)
        
        def checkAnswer(message):
            if message.channel == ctx.channel and answer in message.content:
                return True
            else:
                return False

        try:
            message = await self.client.wait_for("message", timeout = 10.0, check = checkAnswer)
            name = message.author.name
            embed = discord.Embed(title = '', description = f'{name} 님, 정답이에요 !', color = discord.Color.blue())
            await ctx.send(embed=embed)
            self.score +=1 
            self.scoreDict[ctx.author.name] = self.score
            print(self.scoreDict)

        except asyncio.TimeoutError:
            embed = discord.Embed(title = '', description = f'땡! 시간초과입니다~ 정답은 {answer}이에요!', color = discord.Color.red())
            await ctx.send(embed=embed)
            self.score += 0 
            self.scoreDict[ctx.author.name] = self.score
            print(self.scoreDict)

        with open("C:/Users/Jimin/PycharmProjects/discord/cogs/data/score.json","w", encoding= 'utf-8') as s: #에러부분 
            json.dump(self.scoreDict, s, ensure_ascii=False)
        print("===========Modified JSON File===========")


    @commands.command(name="퀴즈랭킹")
    async def ranking_quiz(self,ctx,arg1 = None, arg2 = None):
        with open("C:/Users/Jimin/PycharmProjects/discord/cogs/data/score.json","r", encoding= 'utf-8') as s:
            data = json.load(s)
        # sdict = sorted(dict.items(data)) #점수를 내림차순으로 정렬 
        sdict = sorted(list(data.items()), key=lambda x:x[1], reverse=True)
        if arg1 ==None and arg2 == None: 
            embed = discord.Embed(title = '전체 퀴즈 랭킹', description = "전체 퀴즈 랭킹입니다. \n 한 문제 맞출 때마다 1점이 증가해요! ", color = discord.Color.blue())
            idx = 1
            for name,score in sdict: 
                mod_name = str(idx)+"."+name
                embed.add_field(name=mod_name,value=score,inline=False)
                idx += 1
            await ctx.send(embed=embed)
        
        elif arg1 !=None and arg2 == None: 
            embed = discord.Embed(title = '개인 퀴즈 랭킹', description = "개인 퀴즈 랭킹입니다.", color = discord.Color.gold())
            personal_score = data.get(arg1)
            for x in sdict: 
                if arg1 in x : 
                    rank = sdict.index(x) +1 
                    text = f"{arg1}님은 {personal_score}점으로 {rank}등입니다."
                    embed.add_field(name=arg1,value=text,inline=False)
                    await ctx.send(embed=embed)
        
        elif arg1 !=None and arg2 != None: #매니저 곰 같은 경우 
            embed = discord.Embed(title = '개인 퀴즈 랭킹', description = "개인 퀴즈 랭킹입니다.", color = discord.Color.gold())
            args = arg1 +" "+ arg2
            personal_score = data.get(args)
            for x in sdict: 
                if args in x : 
                    rank = sdict.index(x) +1 
                    text = f"{args}님은 {personal_score}점으로 {rank}등입니다."
                    embed.add_field(name=args,value=text,inline=False)
                    await ctx.send(embed=embed)


    @commands.command(name="퀴즈종료")
    async def end_quiz(self,ctx):
        await ctx.send(f"{ctx.author.name}님의 총점은 {self.score}점 입니다!")

def setup(client):
    client.add_cog(Quiz(client))



