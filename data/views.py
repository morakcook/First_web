from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def news_search(request):
    news_list = get_data()
    return render(request, 'data/news_board.html', {'news_list': news_list})

def get_data():
    news_list =[]

    url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query=하이브"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for news_item, news_imgs in zip(soup.find_all('a', class_='news_tit'), soup.find_all('a', class_='dsc_thumb')):
        title = news_item.get('title')
        link = news_item.get('href')
        print(news_imgs)
        
        img = news_imgs.find('img').get('data-lazysrc')
        #관련 뉴스 아이템의 설명 추출
        description = news_item.find_next_sibling('div', class_='news_dsc').get_text(strip=True)
        news_list.append({'title': title, 'link': link, 'description': description, 'img':img})
    return news_list