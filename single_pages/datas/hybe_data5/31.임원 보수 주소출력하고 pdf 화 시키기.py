import re
import time
from urllib.request import Request, urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import pdfkit
import requests

# 예시 텍스트 (HTML 콘텐츠나 다른 문자열에서 추출된 것으로 가정)
text = """
# var node2 = {};
# node2['text'] = "2. 임원의 보수 등";
# node2['id'] = "41"; 	
# node2['rcpNo'] = "20230403004275";
# node2['dcmNo'] = "9148192";
# node2['eleId'] = "41";
# node2['offset'] = "1923147";
# node2['length'] = "91354";
# node2['dtd'] = "dart3.xsd";
# node2['tocNo'] =  "39";  //eleId 가 toc 순번하고 동일 하지 않은 문서가 존재함.

# cnt++;
"""

# 정규 표현식 패턴
pattern = r"node2\['text'\] = \"(.*?)\";.*?node2\['id'\] = \"(.*?)\";.*?node2\['rcpNo'\] = \"(.*?)\";.*?node2\['dcmNo'\] = \"(.*?)\";.*?node2\['eleId'\] = \"(.*?)\";.*?node2\['offset'\] = \"(.*?)\";.*?node2\['length'\] = \"(.*?)\";.*?node2\['dtd'\] = \"(.*?)\";.*?node2\['tocNo'\] =  \"(.*?)\";"

# 정규 표현식 검색
match = re.search(pattern, text, re.DOTALL)

if match:
    node_data = {
        'text': match.group(1),
        'id': match.group(2),
        'rcpNo': match.group(3),
        'dcmNo': match.group(4),
        'eleId': match.group(5),
        'offset': match.group(6),
        'length': match.group(7),
        'dtd': match.group(8),
        'tocNo': match.group(9)
    }
    print(node_data)
else:
    print("일치하는 내용이 없습니다.")

url = f"https://dart.fss.or.kr/report/viewer.do?rcpNo={node_data['rcpNo']}&dcmNo={node_data['dcmNo']}&eleId={node_data['eleId']}&offset={node_data['offset']}&length={node_data['length']}&dtd={node_data['dtd']}"

print(url)



# wkhtmltopdf의 경로를 설정합니다.
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# 웹 페이지의 HTML 내용을 가져옵니다.
response = requests.get(url)
html_content = response.text

# HTML 내용을 로컬 파일로 저장
with open('temp.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

# 로컬 HTML 파일을 PDF 파일로 변환합니다.
pdfkit.from_file('H:\\내 드라이브\\web_project\\single_pages\\datas\\hybe_data5\\temp.html', 'H:\\내 드라이브\\web_project\\single_pages\\hybe_data5\\임원 보수.pdf', configuration=config)
