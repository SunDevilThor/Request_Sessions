# ScrapeThisSite - Request_Sessions
# Tutorial from John Watson Rooney YouTube channel

import requests
from bs4 import BeautifulSoup
import datetime

def get_title(x):
    url = f'http://scrapethissite.com/pages/forms/?page_num={x}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title.text)
    return 

def get_title_session(x):
    url = f'http://scrapethissite.com/pages/forms/?page_num={x}'
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title.text)
    return 


# no session 0:00:13.874503
# with session 0:00:12.667068
if __name__ == '__main__':
    s = requests.Session()
    start = datetime.datetime.now()
    for x in range(1, 21):
        get_title_session(x)
    finish = datetime.datetime.now() - start
    print(finish)

