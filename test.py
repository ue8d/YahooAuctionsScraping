# coding:utf-8
import urllib3
import requests
from bs4 import BeautifulSoup
import certifi

url = 'https://auctions.yahoo.co.jp/search/search?exflg=1&b=1&n=50&s1=featured&o1=d&auccat=23408&tab_ex=commerce&ei=utf-8&aq=5&oq=RTX&exflg=1&p=rtx2080ti&sc_i=auc_sug'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

elems = soup.select('#allContents > div.l-wrapper.cf > div.l-contents > div.l-contentsBody > div > div.Result__body > div > div > ul > li:nth-of-type(1) > div.Product__detail > h3 > a')

# タグも一緒に表示
print(elems[0])
# 値のみ表示
print(elems[0].contents[0])
# リンク先表示
print(elems[0].attrs['href'])