# https://dart.fss.or.kr/report/viewer.do?rcpNo=20230403004275&dcmNo=9148192&eleId=39&offset=1878332&length=136183&dtd=dart3.xsd

#주의! ProtocolUnknownError 가 떠도 파일은 잘 생성됨


import pdfkit
import requests

# wkhtmltopdf의 경로를 설정합니다.
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# 웹 페이지 URL
url = 'https://dart.fss.or.kr/report/viewer.do?rcpNo=20230403004275&dcmNo=9148192&eleId=39&offset=1878332&length=136183&dtd=dart3.xsd'

# 웹 페이지의 HTML 내용을 가져옵니다.
response = requests.get(url)
html_content = response.text

# HTML 내용을 로컬 파일로 저장
with open('temp.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

# 로컬 HTML 파일을 PDF 파일로 변환합니다.
pdfkit.from_file('H:\\내 드라이브\\web_project\\single_pages\\datas\\hybe_data5\\temp.html', 'H:\\내 드라이브\\web_project\\single_pages\\hybe_data5\\임원및직원등에관한사항.pdf', configuration=config)



