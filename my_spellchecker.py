import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ko; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 IPMS/A640400A-14D460801A1-000000426571',   # firefox UserAgent
}

url = "https://m.search.naver.com/p/csearch/ocontent/spellchecker.nhn"

params = {
    '_callback' : 'my_callback_func',
    'q' : '잘돼는지테스트해봅시다외않되?',
}

response = requests.get(url, params = params, headers=headers).text

print(response)
