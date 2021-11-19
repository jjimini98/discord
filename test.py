# import json

# from discord.channel import StoreChannel 

# with open("C:/Users/Jimin/PycharmProjects/discord/cogs/data/score.json","r", encoding= 'utf-8') as s:
#         data = json.load(s)

# sdict = sorted(dict.items(data))

# for idx, name, score in enumerate(sdict):
#     print(idx,name,score)

origin = {"매니저 곰": 3, "코뮤": 2, "김변수" : 11, "미니언" : 6 }
sdict = sorted(origin.items(), key=lambda x:x[1], reverse=True)
for x in sdict: 
        if "코뮤" in x : 
                rank = sdict.index(x) +1 
                print(rank)
# lis= [('김변수', 11), ('미니언', 6), ('매니저 곰', 3), ('코뮤', 2)]
# print(lis.index("김변수"))