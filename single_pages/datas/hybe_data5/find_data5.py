import os

path = os.getcwd()
def find_htmls(file):
    with open(f'{path}/single_pages/datas/hybe_data5/{file}.txt', 'r', encoding='utf-8') as file:
        # 파일의 내용 읽기
        file_content = file.read()
    return file_content

