import json
def find_menu():
    with open('H:/내 드라이브/web_project/single_pages/datas/menu_data/menu.json', 'r', encoding='utf-8') as file:
        # 파일의 내용 읽기
        file_content = json.load(file)
    return file_content
