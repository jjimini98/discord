import youtube_dl

option = {
    'format' : "bestaudio/best", #오디오 품질 최상
    'noplaylist' : True  #플레이리스트는 제외 
}

DL = youtube_dl.YoutubeDL(option)
url = "https://www.youtube.com/watch?v=bfH2bqMKSgk"
data = DL.extract_info(url, download=False)

print(data.keys())

print("TITLE : ", data['title'])
print("URL : ", data['url'])
print("Tumbnails : " ,data["thumbnails"])
