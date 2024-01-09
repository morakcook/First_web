import re
import time
from urllib.request import Request, urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

# 웹 페이지 URL    계약사항이랑 아티스트 현황 같이 있음 
url = "https://dart.fss.or.kr/report/viewer.do?rcpNo=20230403004275&dcmNo=9148192&eleId=17&offset=153258&length=13853&dtd=dart3.xsd"

# 웹 페이지에서 HTML 가져오기
response = urlopen(url)
soup = BeautifulSoup(response, 'html.parser')

# 전체 HTML 내용을 문자열로 추출
html_all = str(soup)

# "주요계약 및 연구개발활동"과 "주요 아티스트 전속계약" 사이의 내용을 추출하는 정규 표현식
pattern = r"주요계약 및 연구개발활동.*?(?=마\. 주요 아티스트 전속계약)"
match = re.search(pattern, html_all, re.DOTALL)

if match:
    result_contract = match.group()
    with open('H:\\내 드라이브\\web_project\\single_pages\\datas\\hybe_data4\\important_contract.txt', 'w', encoding='utf-8') as file:
        file.write(result_contract)

    print("파일 저장 완료")
else:
    print("일치하는 내용이 없습니다.")

