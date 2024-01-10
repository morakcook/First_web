경영 정보 데시보드

만든 사람들 

https://github.com/morakcook/
https://github.com/moviemanejeongdo/
https://github.com/simjooseung/


--------------------------------------
1. 게시판 만들기

2. 차트 만들기

3. 네이버 증권 스크래핑 해서 보여주기 (x)
    ▷ dart 하이브 크롤링 하기로 변경 (o)

django

1. admin 계정
    - id: admin
    - pw: admin

--------------------------------------
# 23/12/20
팀명: 하이브로

# 주의사항
- 메뉴이동 : href에 주소넣을때 띄어쓰기 금지
- 예 : Dash Board/ : X , DashBoard/ : O


# 23/12/21

메뉴 구성

연결 포괄손익계산서(Statement of comprehensive income) 분석 id=Is    #hybe_data 에 저장
    ▷포괄손익계산서 id=Is_is 
    ▷매출액(Sales) 변화 id=Is_Sales
    ▷매출원가(Cost of Sales) 변화 id=Is_Cos
    ▷판매비와관리비(Selling, General and Administrative Expenses) 변화 id=Is_Exp
    ▷법인세비용(Income Tax Expense) 변화 id=Is_Tax
    ▷순이익(Net Income) 변화 id=Is_Netincome

재무제표(Financial Statements) id=Fs                   
    ▷재무상태표(Balance sheet(B/S)) id=Fs_Bs
    ▷재무제표 주석(Notes to Financial Statements) id=Fs_Note   #hybe_data2 에 저장

임직원(Employees) id=Em
    ▷임직원 현황(Employee Status) id=Em_Status                     #hybe_data5        
    ▷임원 보수(Executive Compensation) id=Em_Compensation          #hybe_data5

비지니스(Business) id=Bs
    ▷계약사항(Contractual Obligations) id=Bs_Contrac       #hybe_data4
    ▷아티스트 현황(Artist Status) id=Bs_Artist             #hybe_data3

- 아이콘 수집
- 로고 제작(HYBE_RO)
    1. 유저
    2. 메뉴(모든 메뉴)
    3. 이메일
    4. 검색(돋보기)


-------------------------------------
하이브 DART API 고유번호

#         고유번호          종목코드 수정일
# 2362  01204056  하이브  352820  20230110
--------------------------------------------

dart api
api key
crtfc_key = 'tell_me'

23년 하이브 사업보고서

https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json?crtfc_key=tell_me&corp_code=01204056&bsns_year=2022&reprt_code=11011&fs_div=CFS

-------------------------------------------------

- html에 넘어가는 data의 형태
    - data = [label, data]의 형태임
    - label을 쓸때 - data[0]
    - data를 쓸때 - data[1]

-------------------------------------------------

# 23/12/29

하이브 18기는 2022년, 17년은 2021년, 16기는 2020년 임


아티스트 현황(Artist Status) id=Bs_Artist   

https://dart.fss.or.kr/report/viewer.do?rcpNo=20230403004275&dcmNo=9148192&eleId=17&offset=153258&length=13853&dtd=dart3.xsd

아티스트 네이버 검색 결과 크롤링 하기 -> 네이버 정보 부족 -> 다음에서 크롤링 하는걸로


# 24/01/12

게시판 만들기

뉴스 페이지 만들기


# 24/01/09

데이터 밴다이어그램으로 표현

유튜브 동영상 캐러셀로

프론트엔드 더 예쁘게












