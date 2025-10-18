import requests
from bs4 import BeautifulSoup
url="https://namu.wiki/w/%EC%9A%B4%EB%B9%A8%EC%A1%B4%EB%A7%8E%EA%B2%9C/%EC%98%81%EC%9B%85"
response=requests.get(url)
response.raise_for_status()
soup=BeautifulSoup(response.text,"html.parser")
main_table=soup.find("strong",string="일반").find_parent("table")
if main_table:
    all_rows=main_table.find_all("tr")
    current_rarity=""
    for row in all_rows:
        header_cell=row.find("td",{"cdlspan":"5"})
        if header_cell and header_cell.find("strong"):
            current_rarity=header_cell.find("strong").get_text(strip=True)
            print(f"\n{current_rarity}등급")
        else:
            heroes=row.find_all("td")
            for hero_cell in heroes:
                hero_link=hero_cell.find("a")
                if hero_link:
                    hero_name=hero_link.get_text(strip=True)
                    if hero_name:
                        print(hero_name)
else:
    print("영웅 목록 테이블을 찾지 못했습니다.")