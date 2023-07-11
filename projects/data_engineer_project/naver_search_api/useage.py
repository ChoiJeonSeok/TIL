from NaverCrawling import NaverCrawling

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

client_id = ""
client_secret = ""

# 기본 파일 불러오기
df = pd.read_csv('search_list.csv') # 검색어 리스트. 
blacklist_file = "blacklist.csv" # 이상한 블로그 제외(정치, 뉴스 스크랩, 지나친 광고)

# Class 호출
crawler = NaverCrawling(client_id, client_secret)

# 각 단어에 대해 크롤링 작업 수행
for word in df['word']:
    # 검색 단어 설정
    search_words = [f"{word} {category}" for category in ['여행', '가볼만한 곳', '관광지', '맛집', '명소']]
    
    # 링크 저장 파일명 설정
    link_file = f"./link/{word}_links.csv"
    
    # 검색 횟수 설정
    search_count = 1
    
    # 크롤링 결과 저장 파일명 설정
    result_file = f"./result/{word}_results.csv"
    
    # 검색 및 링크 수집
    crawler.search(search_words, link_file, search_count, blacklist_file)
    
    # 크롤링 수행
    crawler.crawling(link_file, result_file)