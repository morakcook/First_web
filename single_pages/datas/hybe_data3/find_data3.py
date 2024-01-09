import json
import os

path = os.getcwd()
def find_Artist():
    with open(f'{path}/single_pages/datas/hybe_data3/daum_artist_info.json', 'r', encoding='utf-8') as file:
        # 파일의 내용 읽기
        file_content = json.load(file)
    return file_content

