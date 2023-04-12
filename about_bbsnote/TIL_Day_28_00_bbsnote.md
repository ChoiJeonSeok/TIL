# Django project 과정

## 목차 

<a href="#section-1">1. Django 설치 및 프로젝트 생성</a>
<ul>
  <li><a href="#section-2">가상환경 생성 및 활성화</a></li>
  <li><a href="#section-3">Django 설치</a></li>
  <li><a href="#section-4">Django 프로젝트 생성</a></li>
</ul>

1. [앱 생성 및 모델 작성][2]
   - [앱 생성][21]
   - [모델 작성][22]
   - [데이터베이스 마이그레이션][23]
2. [뷰 및 템플릿 작성][3]
   - [뷰 함수 작성][31]
   - [URL 패턴 작성][32]
   - [템플릿 작성][33]
3. [정적 파일 관리][4]
   - [정적 파일 디렉토리 생성][41]
   - [정적 파일 설정][42]
   - [정적 파일 사용][43]
4. [디버깅 및 테스트][5]
   - [디버깅][51]
   - [테스트 코드 작성][52]
   - [테스트 실행][53]
5. [배포][6]
   - [서버 설정][61]
   - [데이터베이스 설정][62]
   - [스태틱 파일 및 미디어 파일 설정][63]
   - [WSGI 설정][64]
<br><br>
<hr style="border-style: solid; border-width: 8px;">

<h2 id="section-1">1. Django 설치 및 프로젝트 생성</h2>

<h3 id="section-2">가상환경 생성 및 활성화</h3>

1. Anaconda Prompt 실행
   - 시작 메뉴에서 "Anaconda Prompt"를 찾아 실행합니다.
2. 가상환경 생성
   - conda create --name 가상환경이름 python=3.9
   - "가상환경이름"에는 원하는 이름을 작성한다.
   - python 버전은 명시해야 원하는 버전의 가상환경을 생성할 수 있다.
3. 가상환경 활성화
   - 가상환경 생성이 완료되면 가상환경을 활성화한다.
   - conda activate 가상환경이름

<h3 id="section-3">Django 설치</h3> 

1. Django 설치
   - 가상환경이 활성화된 상태에서 Django를 설치한다.
   - pip install django
  
<h3 id="section-4">Django 프로젝트 생성</h3>

1. Django 프로젝트를 생성할 폴더로 이동
   - cd C:\Users\username\projects
2. Django 프로젝트 생성
   - django-admin startproject myproject
   - myproject라는 폴더가 생성되며, 그 안에 Django 프로젝트의 기본 구조와 파일이 생성된다.
3. 생성된 프로젝트 폴더로 이동한다.
   - cd myproject

