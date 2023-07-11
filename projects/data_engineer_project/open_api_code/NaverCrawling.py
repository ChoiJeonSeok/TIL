import csv
import json
import time
import pandas as pd
import urllib.request
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class NaverCrawling:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def search_and_save_api_results(self, text, output_file, iterations):
        encText = urllib.parse.quote(text)
        fieldnames = ['title', 'link', 'description', 'bloggername', 'bloggerlink', 'postdate']

        with open(output_file, 'a', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            count = 0

            for _ in tqdm(range(1, iterations + 1), desc="API 호출 및 저장 중"):

                url = "https://openapi.naver.com/v1/search/blog?query=" + encText + f"&display=100&sort=sim"
                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id", self.client_id)
                request.add_header("X-Naver-Client-Secret", self.client_secret)
                response = urllib.request.urlopen(request)
                rescode = response.getcode()

                if rescode == 200:
                    response_body = response.read()
                    data = json.loads(response_body.decode('utf-8'))
                    for item in data['items']:
                        writer.writerow({'title': item['title'], 'link': item['link'], 'description': item['description'], 'bloggername': item['bloggername'], 'bloggerlink': item['bloggerlink'], 'postdate': item['postdate']})
                    count += 1
                    print(f"API 호출 및 {text}에 대한 {count * 100}개의 검색 데이터 저장 완료.")
                else:
                    print(f"API 호출 실패: start={start}, 응답 코드={rescode}")



    def crawl_links(self, csv_file, output_file):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        service = Service(executable_path=r"C:\Users\art\Desktop\chromedriver\chromedriver.exe")

        driver = webdriver.Chrome(service=service, options=chrome_options)

        df = pd.read_csv(csv_file)
        blog_links = df['link'].tolist()

        contents = []
        count = 0

        for link in tqdm(blog_links, desc="Crawling", unit="link"):
            driver.get(link)
            time.sleep(1)

            driver.switch_to.frame("mainFrame")

            try:
                #table_exists = driver.find_elements(By.CSS_SELECTOR, 'table')
                #if len(table_exists) > 0:
                    #continue
                a = driver.find_element(By.CSS_SELECTOR, 'div.se-main-container').text
                contents.append(a)
            except NoSuchElementException:
                a = driver.find_element(By.CSS_SELECTOR, 'div#content-area').text
                contents.append(a)
            except:
                pass

            count += 1

        driver.quit()
        
        # contents 리스트의 길이가 0인 경우 빈 문자열을 추가하여 DataFrame의 길이에 맞춤
        if len(contents) == 0:
            contents = [''] * len(df)
            
        df['content'] = contents    
        df['content'] = df['content'].astype(str)
        df = df[df['content'].str.strip() != '']

        df.to_csv(output_file, index=False, encoding='utf-8-sig')

        print(f"Crawling completed: {count} links processed")


    def preprocess_links(self, csv_file, blacklist_file):
        # CSV 파일 읽기
        df = pd.read_csv(csv_file)

        # 'https://blog.naver.com/'로 시작하지 않는 링크 제거
        df = df[df['link'].str.startswith('https://blog.naver.com/')]

        # 중복된 링크 제거
        df = df.drop_duplicates(subset=['link'], keep='first')
        
        # 블랙리스트 CSV 파일 읽기
        blacklist = pd.read_csv(blacklist_file)

        # 블랙리스트에 포함된 링크 제거
        df = df[~df['link'].isin(blacklist['link'])]

        # 수정된 데이터프레임을 새로운 CSV 파일로 저장
        df.to_csv(csv_file, index=False, encoding='utf-8-sig')

        print(f"Naver blog 링크의 수: {len(df['link'])}")
        return len(df['link'])

    def extract_columns(self, csv_file):
        # CSV 파일 읽기
        df = pd.read_csv(csv_file)

        # 필요한 열만 선택
        columns_to_extract = ['title', 'content']
        df = df[columns_to_extract]
        df = df[df['content'].str.strip() != '']
        
        # title과 content 중 하나라도 값이 없는 행 제거
        df = df.dropna(subset=['title', 'content'])        
        
        # 수정된 데이터프레임을 기존 CSV 파일로 덮어씌우기
        df.to_csv(csv_file, mode='w', index=False, encoding='utf-8-sig')
        print('데이터 정제 및 불필요한 열 제거 완료')

    def search(self, search_words, link_file_name, search_count, blacklist_file):
        # 코드 실행
        for word in search_words:
            self.search_and_save_api_results(word, link_file_name, search_count)
        i = self.preprocess_links(link_file_name, blacklist_file)
        print(f'\n{i}개의 링크에 대해서 크롤링 시작.')

    
    def crawling(self,link_file_name, result_file_name):
        start_time = time.time()
        self.crawl_links(link_file_name, result_file_name)
        self.extract_columns(result_file_name)
        
        # 총 실행 시간 계산
        execution_time = time.time() - start_time

        # 시, 분, 초로 변환
        minutes, seconds = divmod(execution_time, 60)
        hours, minutes = divmod(minutes, 60)

        # 시간을 시, 분, 초 형식으로 출력
        print(f"Total execution time: {int(hours)}시 {int(minutes)}분 {int(seconds)}초")