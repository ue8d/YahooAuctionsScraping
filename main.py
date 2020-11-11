# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re

# 検索したい文字列
product = "任天堂スイッチ"
# 出力ファイル名
file = "sample2.txt"
# 何ページ分スクレイピングするか
page_count = 5
# 何件以上の入札分を出力するか
bid_count = 0



page = 1
i = 0
while i < page_count:
    url = 'https://auctions.yahoo.co.jp/search/search?p=' + product +'&va=' + product + '&exflg=1&b=' + str(page) +'&n=100'

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # 正規表現
    productName = soup.find_all(class_=re.compile("Product__titleLink"))
    elems = soup.find_all(class_=re.compile("Product__priceValue u-textRed"))
    bid = soup.find_all(class_=re.compile("Product__bid"))


    fileobj = open(file, "a", encoding = "utf_8")

    num = 0
    while num < len(elems):
        if int(bid[num].contents[0]) >= bid_count:
            # print(productName[num].contents[0])
            fileobj.write(productName[num].contents[0] + "\n")
            # print(elems[num].contents[0])
            fileobj.write(elems[num].contents[0] + "\n")
        num = num + 1

    fileobj.close()
    print(str(i + 1) + "ページ目終了")

    i += 1
    page += 100