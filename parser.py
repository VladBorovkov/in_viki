import requests
from bs4 import BeautifulSoup

HOST = 'https://ru.wikipedia.org'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}


def get_html(url, params=''):
    html = requests.get(url, headers=HEADERS, params=params)
    return html


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='mw-search-result')
    all_articles = []
    for item in items:
        try:
            all_articles.append({
                'link_article': HOST + item.find('div', class_='mw-search-result-heading').find('a').get('href'),
            })
        except IndexError:
            continue
    return all_articles


def parser(text):
    URL = f"https://ru.wikipedia.org/w/index.php?search={text}&title=Служебная%3AПоиск&profile=advanced&fulltext=1&ns0=1"
    html = get_html(URL)
    articles = get_content(html.text)[:5]
    if articles == []:
        return ('Соответствий', 'запросу', 'не', 'найденно')
    else:
        return articles[0]['link_article'],\
               articles[1]['link_article'],\
               articles[2]['link_article'],\
               articles[3]['link_article'],