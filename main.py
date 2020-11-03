# coding:utf-8
import urllib3
import requests
from bs4 import BeautifulSoup
import certifi
import re

url = 'ここに検索結果のURLを入力'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

# serector利用
# elems = soup.select('#allContents > div.l-wrapper.cf > div.l-contents > div.l-contentsBody > div > div.Result__body > div > div > ul > li:nth-of-type(1) > div.Product__detail > h3 > a')

# 正規表現
productName = soup.find_all(class_=re.compile("Product__titleLink"))
elems = soup.find_all(class_=re.compile("Product__priceValue u-textRed"))
bid = soup.find_all(class_=re.compile("Product__bid"))


# タグも一緒に表示
# print(elems)
# 値のみ表示
print(elems[0].contents[0])
# リンク先表示
# print(elems[0].attrs['href'])

num = 0
while num < len(elems):
    print(productName[num].contents[0])
    print(elems[num].contents[0])
    num = num + 1