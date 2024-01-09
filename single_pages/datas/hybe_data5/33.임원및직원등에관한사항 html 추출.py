import re
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 웹 페이지 URL
url = "https://dart.fss.or.kr/report/viewer.do?rcpNo=20230403004275&dcmNo=9148192&eleId=39&offset=1878332&length=136183&dtd=dart3.xsd"

# 웹 페이지에서 HTML 가져오기
response = urlopen(url)
soup = BeautifulSoup(response, 'html.parser')

# <head> 태그 내용을 문자열로 추출
head_content = str(soup)

with open('H:\\내 드라이브\\web_project\\single_pages\\datas\\hybe_data5\\임원및직원등에관한사항.txt', 'w', encoding='utf-8') as file:
    file.write(head_content)