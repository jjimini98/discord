# with open("C:/Users/Jimin/PycharmProjects/discord/tech_interview.zip/인성/1_인성.md","r",encoding='utf-8') as f:
#     a = f.readlines()
#     print(a)


import os
 
path_dir = 'C:/Users/Jimin/PycharmProjects/discord/tech_interview.zip/인성'
 
file_list = os.listdir(path_dir)

print(file_list)