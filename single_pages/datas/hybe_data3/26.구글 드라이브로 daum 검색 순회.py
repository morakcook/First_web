import json
import re
import time
from urllib.request import Request, urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller 

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

try:
    # 웹 페이지 URL
    url = "https://dart.fss.or.kr/report/viewer.do?rcpNo=20230403004275&dcmNo=9148192&eleId=17&offset=153258&length=13853&dtd=dart3.xsd"

    # 웹 페이지에서 HTML 가져오기
    response = urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')

    # 전체 HTML 내용을 문자열로 추출
    html_content = str(soup)

    # "아티스트" 다음에 오는 모든 내용을 추출하는 정규 표현식
    pattern = re.compile(r'아티스트(.*)', re.DOTALL)

    # 정규 표현식을 사용하여 검색
    match = pattern.search(html_content)
    if not match:
        print("아티스트라는 단어를 찾을 수 없습니다.")
        exit()

    # "아티스트" 다음에 오는 모든 내용을 추출
    artist_content = match.group(1)

    # 각 행을 분리하는 정규 표현식
    rows = re.findall(r'<tr>(.*?)</tr>', artist_content, re.DOTALL)

    # 결과를 저장할 딕셔너리 리스트
    artists_contracts = []

    # 현재 회사명과 그룹명을 추적하기 위한 변수
    current_company = None
    current_group = None

    for row in rows:
        # 각 열의 내용을 추출
        columns = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)

        # 회사명, 그룹, 아티스트 추출
        if len(columns) == 3:
            current_company = re.sub(r'<.*?>', '', columns[0]).strip()
            current_group = re.sub(r'<.*?>', '', columns[1]).strip()
            artist = re.sub(r'<.*?>', '', columns[2]).strip()
        elif len(columns) == 2:
            current_group = re.sub(r'<.*?>', '', columns[0]).strip()
            artist = re.sub(r'<.*?>', '', columns[1]).strip()
        elif len(columns) == 1:
            artist = re.sub(r'<.*?>', '', columns[0]).strip()
        else:
            continue

        # 결과 딕셔너리에 추가     
        artists_contracts.append({"회사명": current_company, "그룹": current_group, "아티스트": artist})

    artists_contracts1 = artists_contracts[1:]

    # 아티스트 정보 추출하는 부분
    artist_info_dict = {}

    # 아티스트 데이터를 순회하며 다음 검색 결과 페이지의 HTML 추출 및 분석
    for artist in artists_contracts1:
        group_name = artist['그룹']
        artist_name = artist['아티스트']
        search_query = f"{group_name} {artist_name}"
        encoded_query = quote(search_query)
        search_url = f"https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={encoded_query}"

        # WebDriver 페이지 열기
        driver.get(search_url)

        # 페이지가 완전히 로드될 때까지 기다림
        time.sleep(0.5)

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 원하는 정보가 담긴 div 태그 찾기
        div_content = soup.find('div', class_='c-item-exact')

       # 정보 추출 및 저장
        if div_content:
            extracted_content = str(div_content)
        else:
            # 아티스트 이름의 첫 글자를 제거하고 다시 검색 시도
            if len(artist_name) > 1:
                search_query = f"{group_name} {artist_name[1:]}"
                encoded_query = quote(search_query)
                search_url = f"https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={encoded_query}"
                driver.get(search_url)
                time.sleep(0.5)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                div_content = soup.find('div', class_='c-item-exact')

                if not div_content:
                    # 아티스트 이름이 두 어절 이상인 경우, 뒤 어절을 제거하고 다시 검색
                    if ' ' in artist_name:
                        first_name = artist_name.split(' ')[0]
                        search_query = f"{group_name} {first_name}"
                        encoded_query = quote(search_query)
                        search_url = f"https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={encoded_query}"
                        driver.get(search_url)
                        time.sleep(0.5)
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        div_content = soup.find('div', class_='c-item-exact')

                    if not div_content:
                        # 아티스트 이름만으로 다시 검색 시도
                        search_query = artist_name
                        encoded_query = quote(search_query)
                        search_url = f"https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={encoded_query}"
                        driver.get(search_url)
                        time.sleep(0.5)
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        div_content = soup.find('div', class_='c-item-exact')

        if div_content:
            extracted_content = str(div_content)
        else:
            extracted_content = "<img src=\"H:\\내 드라이브\\web_project\\single_pages\\static\\single_pages\\images\\logo5.png\">"

        artist_info_dict[artist_name] = extracted_content

        # 각 요청 사이에 딜레이 추가
        time.sleep(0.5)

    # 생성된 딕셔너리를 JSON 파일로 저장
    with open('H:\\내 드라이브\\web_project\\single_pages\\datas\\hybe_data3\\daum_artist_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(artist_info_dict, json_file, ensure_ascii=False, indent=4)

    print("정보가 artist_info.json 파일에 저장되었습니다.")

finally:
    # WebDriver 종료
    driver.quit()
