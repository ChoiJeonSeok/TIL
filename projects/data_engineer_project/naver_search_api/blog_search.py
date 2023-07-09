import csv
import json
import os
import sys
import urllib.request
from tqdm import tqdm

client_id = "ID"
client_secret = "CODE"
encText = urllib.parse.quote("관광지")
fieldnames = ['title', 'link', 'description', 'bloggername', 'bloggerlink', 'postdate']

with open('output.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:  # Use 'utf-8-sig' encoding
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    if csvfile.tell() == 0:  # Check if file is empty
        writer.writeheader()  # Write header only if the file is empty
    
    count = 0  # Initialize count variable
    
    for start in tqdm(range(1, 11), desc="API 호출 및 저장 중"):  # Iterate from 1 to 100 with tqdm progress bar
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText + f"&display=100&start={start}&sort=sim"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        
        if rescode == 200:
            response_body = response.read()
            data = json.loads(response_body.decode('utf-8'))
            for item in data['items']:
                writer.writerow({'title': item['title'], 'link': item['link'], 'description': item['description'], 'bloggername': item['bloggername'], 'bloggerlink': item['bloggerlink'], 'postdate': item['postdate']})
            count += 1  # Increment count after each successful API call
        else:
            print(f"API 호출 실패: start={start}, 응답 코드={rescode}")
    
    print(f"API 호출 및 저장 완료: 총 {count}번 호출")  # Print the total count of successful API calls

print('작업 완료')
