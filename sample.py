# coding:utf-8
import urllib3
from bs4 import BeautifulSoup
import certifi

# アクセスするURL
url = "https://auctions.yahoo.co.jp/search/search?exflg=1&b=1&n=50&s1=featured&o1=d&auccat=23408&tab_ex=commerce&ei=utf-8&aq=5&oq=RTX&exflg=1&p=rtx2080ti&sc_i=auc_sug"

# httpsの証明書検証を実行している
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
r = http.request('GET', url)

soup = BeautifulSoup(r.data, 'html.parser')

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.title

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
title = title_tag.string

# タイトル要素を出力
print(title_tag)

# タイトルを文字列を出力
print(title)