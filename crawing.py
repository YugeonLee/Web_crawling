import requests
response=requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%98%81%ED%99%94+%EB%9E%AD%ED%82%B9&oquery=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&tqi=jLOLhsqptbNssPESZMGssssss38-339491&ackey=kkuv7n8z")
from bs4 import BeautifulSoup
soup=BeautifulSoup(response.text,"html.parser")
title=soup.select_one("a.title")
print(f"1위 영화:{title.text}")