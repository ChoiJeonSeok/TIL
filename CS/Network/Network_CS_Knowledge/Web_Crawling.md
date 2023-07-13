# 웹 크롤링(Web Crawling)

## Web Scraping
### 웹 크롤링의 개념과 동작 원리 (Concepts and principles of web scraping)
- 웹 크롤링은 웹 페이지에서 데이터를 수집하거나 탐색하는 과정을 의미한다. 

<br>웹 크롤링은 다음과 같은 단계로 진행된다.:

1. 웹 페이지 탐색: 웹 크롤러는 시작점으로부터 출발하여 웹 페이지를 탐색한다. 이를 위해 URL을 기반으로 링크를 따라가며 여러 페이지를 방문한다.

2. 데이터 추출: 웹 페이지를 방문하면서 필요한 데이터를 추출한다. HTML 문서에서 원하는 요소를 선택하고, 텍스트, 이미지, 링크 등 다양한 정보를 추출한다.

3. 데이터 가공: 추출된 데이터를 가공하여 원하는 형식으로 정리한다. 예를 들어, 텍스트 데이터의 경우 정규 표현식이나 문자열 처리 기법을 사용하여 정제하고 구조화한다.

4. 데이터 저장 또는 분석: 가공된 데이터를 필요에 따라 저장하거나 분석한다. 데이터베이스에 저장하거나 CSV, JSON 등의 형식으로 내보낼 수 있다.

### 크롤링에 사용되는 도구와 라이브러리 소개 (Introduction to web scraping tools and libraries) (e.g., BeautifulSoup, Scrapy)
### 크롤링 데이터의 파싱과 추출 (Parsing and extracting data from web scraping)

## API Scraping
### API와 API 크롤링의 개념 (Concepts of API and API scraping)
### RESTful API와 SOAP API의 차이점
### API 키 인증과 사용 방법 (API key authentication and usage)

## Ethics and Legal Aspects of Web Crawling
### 웹 크롤링 시 고려해야 할 윤리적 측면 (Ethical considerations in web crawling)
### 로봇 배제 표준과 크롤링 정책 소개 (Robots.txt and crawling policies)


## Blocking Web Crawling:

### Robots.txt
  - 로봇 배제 표준 파일이란 (Introduction to Robots.txt file)
  - 로봇 배제 표준의 문법와 구조 (Syntax and structure of Robots.txt)
  - 웹 크롤링을 막기 위한 로봇 배제 표준의 사용 (Using Robots.txt to block web crawlers)

### Meta Tags
  - 웹 크롤링을 위한 Meta 태그 개요 (Overview of Meta tags for web crawling)
  - "nofollow" 속성을 사용하여 크롤링 방지 (Using "nofollow" attribute to prevent crawling)
  - 크롤링 제어와 관련된 다른 Meta 태그들 (Other Meta tags related to crawling control)

### CAPTCHA
  - CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart)
  - 자동화된 크롤링을 방지하기 위한 CAPTCHA 구현 (Implementing CAPTCHA to prevent automated crawling)

### IP Blocking
  - IP 차단을 통해 웹 크롤러의 접근 제한하기 (Using IP blocking to restrict access for web crawlers)
    - 노이즈를 활용하면 인공지능도 인식하지 못할까?
  - IP 차단 규칙과 필터 설정하기 (Configuring IP blocking rules and filters)

