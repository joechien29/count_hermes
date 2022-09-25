import requests
import time
from bs4 import BeautifulSoup



def get_item_count():
    headers = {
        'User-Agent': 'Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/105.0.0.0 Safari/537.36'
    }
    proxies = {"http": "http://192.10.1.10:8080", "https": "http://193.121.1.10:9080", }
    url = 'https://www.hermes.com/tw/zh/category/women/bags-and-small-leather-goods/' \
          'bags-and-clutches/'
    try:
        r = requests.get(url=url, headers=headers)
    except:
        print('----- Reject ----\n------- Go to Sleep -------')
        time.sleep(1200)
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all('div', class_='product-item-meta')
    items = []
    for item in divs:
        item = item.text.strip()
        print(item)
        items.append(item)
    item_count = len(items)
    print('----------- Number of types currently on sale at Hermers:', item_count, '  -----------')
    return item_count
