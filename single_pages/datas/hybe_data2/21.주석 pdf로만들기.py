import pdfkit
import requests


#프로그램 설치
# https://wkhtmltopdf.org/

# wkhtmltopdf의 경로를 설정합니다.
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# 웹 페이지 URL
url = 'https://dart.fss.or.kr/report/viewer.do?rcpNo=20231115000333&dcmNo=9501770&eleId=5&offset=88839&length=421456&dtd=dart3.xsd'

# 웹 페이지의 HTML 내용을 가져옵니다.
response = requests.get(url)
html_content = response.text

# PDF 파일로 변환합니다.
pdfkit.from_string(html_content, 'H:\\내 드라이브\\web_project\\single_pages\\datas\\hybe_data2\\output.pdf', configuration=config)
