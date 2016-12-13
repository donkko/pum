# -*- coding: utf-8 -*-

import requests

HTML_REQUEST_HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '',
'Host': 'blog.naver.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36'
}

from random import randint
from time import sleep


def get_html(url, params=None, headers=HTML_REQUEST_HEADERS):
    req = requests.get(url, params=params, headers=headers)
    print u'[get_html] url:', unicode(req.url)
    print u'[get_html] status_code:', unicode(req.status_code)
    if req.status_code != 200:
        return None
    req.encoding = 'euc-kr'
    return req


def do_task():
    get_html('http://blog.naver.com/PostList.nhn?blogId=fdsa34')


if __name__ == '__main__':
    do_task()
    while True:
        do_task()
        sleep(randint(60, 180))
