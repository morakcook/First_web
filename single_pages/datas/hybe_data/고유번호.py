# # 1. 다트 api 에서 api 키를 발급 받기
# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019018

# # 2. 다트 개발가이드에서 고유번호 요청 url 확인
# https://opendart.fss.or.kr/guide/main.do?apiGrpCd=DS001


# # 3. 개발자 가이드에서 필요한 코드 확인하기
# https://dart-fss.readthedocs.io/en/latest/dart_search.html



crtfc_key = 'tell_me'
 
import requests 
import pandas as pd 
import io 
import zipfile
import xml.etree.ElementTree as et 
import json


def get_corpcode(crtfc_key): 
    """ 
    OpenDART 기업 고유번호 받아오기 
    return 값: 주식코드를 가진 업체의 DataFrame 
    """ 
    params = {'crtfc_key':crtfc_key} 
    items = ["corp_code","corp_name","stock_code","modify_date"] 
    item_names = ["고유번호","회사명","종목코드","수정일"] 
    url = "https://opendart.fss.or.kr/api/corpCode.xml" #요청 url
    res = requests.get(url,params=params) #url 불러오기
    zfile = zipfile.ZipFile(io.BytesIO(res.content))  #zip file 받기
    fin = zfile.open(zfile.namelist()[0])  #zip file 열고
    root = et.fromstring(fin.read().decode('utf-8'))  #utf-8 디코딩
    data = [] 
    for child in root: 
        if len(child.find('stock_code').text.strip()) > 1: # 종목코드가 있는 경우 
            data.append([]) #data에 append하라 
            for item in items: 
                data[-1].append(child.find(item).text) 
    df = pd.DataFrame(data, columns=item_names) 
    return df


stock_comp = get_corpcode(crtfc_key)

with open('고유번호.txt', 'w', encoding='utf-8') as file:
    file.write(stock_comp.to_string())


#         고유번호          종목코드 수정일
# 2362  01204056  하이브  352820  20230110