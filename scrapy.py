import requests
import json
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title_list = soup.select_one('ul.lst_detail_t1')
titles = title_list.select('li')

movie_data = []

for title in titles:
    a = title.select('dt.tit > a')[0]
    code = a['href'].split("code=")[-1]
    name = a.text
    movie_datum = {}
    movie_datum['title'] = name
    movie_datum['code'] = code
    movie_data.append(movie_datum)

json_file = json.dumps(movie_data)
with open('movie_code.json', "w", encoding='euc-kr') as f:
    f.write(json_file)