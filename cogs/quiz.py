from discord.ext import commands
import csv
import random 
import asyncio
import json 

class Quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.quizDict = {}
        self.scoreDict = {} #이것도 여기서 관리하는게 맞나.. 
        self.score = 0 #이걸 여기서 관리하는게 맞나.. 
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
        await ctx.send(problem) #문제 출력 

        def checkAnswer(message):
            # message.channel == ctx.channel 입력한 정답의 채널과 명령어가 입력된 채널이 같은지 
            # answer in message.content : 메세지의 내용에 정답이 들어있는지? 
            if message.channel == ctx.channel and answer in message.content:
                return True
            else:
                return False

        try:
            # wait_for는 세 개의 인자를 받음 (1. 이벤트: 어떤 이벤트가 발생하기를 기다리는 함수, 여기서는 message를 기다리는 함수 ,
            # 2. 이벤트 유효성 , check : 여기서 유효한 메세지 정답을 기다림. 이 때 check 인자에 들어가는 checkAnswer 함수 -> 이게 True일때 통과) 
            await self.client.wait_for("message", timeout= 10.0, check = checkAnswer)
            await ctx.send("정답이에요!")
            self.score +=1 
            self.scoreDict[ctx.author.name] = self.score
            print(self.scoreDict)

        except asyncio.TimeoutError:
            await ctx.send(f"땡! 시간초과에요! 정답은 {answer}이에요!")
            self.score += 0 
            self.scoreDict[ctx.author.name] = self.score
            print(self.scoreDict)

        with open("C:/Users/Jimin/PycharmProjects/discord/cogs/data/score.json","w", encoding= 'utf-8') as s: #에러부분 
             json.dump(self.scoreDict, s, ensure_ascii=False)
        print("===========Modified JSON File===========")


    @commands.command(name="퀴즈종료")
    async def end_quiz(self,ctx):
        await ctx.send(f"{ctx.author.name}님의 총점은 {self.score}점 입니다!")

def setup(client):
    client.add_cog(Quiz(client))