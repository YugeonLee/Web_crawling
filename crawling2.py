import requests
response=requests.get("https://m.moviechart.co.kr/rank/realtime/index/image")
from bs4 import BeautifulSoup
soup=BeautifulSoup(response.text,"html.parser")
title_list=soup.select("div.movieBox div.movie-title")
for i,title in enumerate(title_list):
    print(f"{i+1}위 영화:{title.text}")