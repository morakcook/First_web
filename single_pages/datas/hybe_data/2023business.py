import requests

# API 요청 URL  하이브 고유번호를 찾아서 입력 2023년 4월에 공시된 사업보고서, 최근3개년 18기,17기,16기
url = 'https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json?crtfc_key=tell_me&corp_code=01204056&bsns_year=2022&reprt_code=11011&fs_div=CFS'

# HTTP 요청을 보내어 응답 받기
response = requests.get(url)

# 응답이 성공적인지 확인
if response.status_code == 200:
    # JSON 데이터를 파일로 저장    재무상태표 저장
    with open('single_pages\datas\hybe_data\hybe2023.json', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("JSON 파일이 성공적으로 저장되었습니다.")
else:
    print("요청에 실패했습니다. 상태 코드:", response.status_code)
