# Django project 과정

## 목차 

<a href="#section-1">1. Django 설치 및 프로젝트 생성</a>
<ul>
  <li><a href="#section-11">가상환경 생성 및 활성화</a></li>
  <li><a href="#section-12">Django 설치</a></li>
  <li><a href="#section-13">Django 프로젝트 생성</a></li>
</ul>

<a href="#section-2">2. 앱 생성 및 모델 작성</a>
<ul>
  <li><a href="#section-21">앱 생성</a></li>
  <li><a href="#section-22">모델 작성</a></li>
  <li><a href="#section-23">데이터베이스 마이그레이션</a></li>
</ul>

<a href="#section-3">3. 뷰 및 템플릿 작성</a>
<ul>
  <li><a href="#section-31">뷰 함수 작성</a></li>
  <li><a href="#section-32">URL 패턴 작성</a></li>
  <li><a href="#section-33">템플릿 작성</a></li>
</ul>

<a href="#section-4">4. 정적 파일 관리</a>
<ul>
  <li><a href="#section-41">정적 파일 디렉토리 생성</a></li>
  <li><a href="#section-42">정적 파일 설정</a></li>
  <li><a href="#section-43">정적 파일 사용</a></li>
</ul>

<a href="#section-5">5. 디버깅 및 테스트</a>
<ul>
  <li><a href="#section-51">디버깅</a></li>
  <li><a href="#section-52">테스트 코드 작성</a></li>
  <li><a href="#section-53">테스트 실행</a></li>
</ul>

<a href="#section-6">6. 배포</a>
<ul>
  <li><a href="#section-61">서버 설정</a></li>
  <li><a href="#section-62">데이터베이스 설정</a></li>
  <li><a href="#section-63">스태틱 파일 및 미디어 파일 설정</a></li>
  <li><a href="#section-64">WSGI 설정</a></li>
</ul>

<br><br>
<hr style="border-style: solid; border-width: 8px;">

<h2 id="section-1">1. Django 설치 및 프로젝트 생성</h2>

<h3 id="section-11">가상환경 생성 및 활성화</h3>

1. Anaconda Prompt 실행
   - 시작 메뉴에서 "Anaconda Prompt"를 찾아 실행합니다.
2. 가상환경 생성
   - conda create --name 가상환경이름 python=3.9
   - "가상환경이름"에는 원하는 이름을 작성한다.
   - python 버전은 명시해야 원하는 버전의 가상환경을 생성할 수 있다.
3. 가상환경 활성화
   - 가상환경 생성이 완료되면 가상환경을 활성화한다.
   - conda activate 가상환경이름

<h3 id="section-12">Django 설치</h3> 

1. Django 설치
   - 가상환경이 활성화된 상태에서 Django를 설치한다.
   - pip install django
  
<h3 id="section-13">Django 프로젝트 생성</h3>

1. Django 프로젝트를 생성할 폴더로 이동
   - cd C:\Users\username\projects
2. Django 프로젝트 생성
   - django-admin startproject myproject
   - myproject라는 폴더가 생성되며, 그 안에 Django 프로젝트의 기본 구조와 파일이 생성된다.
3. 생성된 프로젝트 폴더로 이동한다.
   - cd myproject

<h2 id="section-2">2. 앱 생성 및 모델 작성</h2>

<h3 id="section-21">앱 생성</h3>

1. Django에서는 startapp 명령어로 앱을 생성할 수 있다.
   - $ python manage.py startapp blog
   - blog 라는 이름의 앱이 생성된다. 
   - 프로젝트 내에 blog 라는 디렉토리가 생성되고, 그 안에 자동으로 다양한 파일들이 생성된다.

<h3 id="section-22">모델 작성</h3>

1. 모델이란 데이터베이스에 저장될 데이터의 구조를 정의하는 클래스 
   - 클래스를 정의하면 객체를 생성할 수 있고, 생성된 객체는 클래스에서 정의한 변수와 함수를 가지고 있다.
   - 모델 클래스를 생성하여 데이터베이스에 저장할 데이터의 구조를 정의하고, 필요한 필드와 메소드를 포함시킬 수 있다.
2. 생성된 모델 클래스는 django.db.models.Model 클래스를 Django로부터 상속받았다.
   - 따라서 생성된 모델 클래스는 데이터베이스와 연동할 때 필요한 기능들을 상속받았다.
   - 따라서 생성된 모델 클래스는 필요한 필드와 메소드를 추가하여 데이터의 구조를 정의할 수 있다.
3. 모델은 데이터베이스 매핑을 제공한다.
   - 데이터베이스와 상호 작용을 추상화하여 개발자가 데이터베이스 쿼리를 최소한으로 작성할 수 있도록 돕는다.
4. blog/models.py 파일을 연다.
   - blog에 어울리는 post 모델을 정의한다.
```
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```
<details>
  <summary>코드 설명</summary>
  
  from django.db import models: Django에서 제공하는 models 모듈을 가져옵니다. 이 모듈은 데이터베이스 모델링을 위한 다양한 클래스와 필드를 제공합니다.

   class Post(models.Model):: Post라는 모델 클래스를 선언합니다. 이 클래스는 models.Model 클래스를 상속받아 정의됩니다.

   title = models.CharField(max_length=200): CharField는 문자열 필드를 정의하는 클래스입니다. title 필드는 최대 길이가 200인 문자열 필드입니다.

   content = models.TextField(): TextField는 긴 문자열을 저장할 수 있는 필드를 정의하는 클래스입니다. content 필드는 길이 제한이 없는 문자열 필드입니다.

   created_at = models.DateTimeField(auto_now_add=True): DateTimeField는 날짜와 시간을 저장하는 필드를 정의하는 클래스입니다. auto_now_add=True는 객체가 생성될 때 자동으로 현재 날짜와 시간을 저장하도록 설정한 옵션입니다.

   updated_at = models.DateTimeField(auto_now=True): updated_at 필드는 객체가 저장될 때마다 자동으로 현재 날짜와 시간으로 갱신됩니다. 따라서 auto_now=True 옵션을 사용합니다.

   def __str__(self):: __str__ 메서드는 객체를 문자열로 표현할 때 사용하는 메서드입니다.

   return self.title: __str__ 메서드에서는 객체의 title 필드 값을 반환합니다. 이를 통해 Post 객체를 문자열로 출력할 때는 해당 객체의 title 값이 출력됩니다.
</details>


<br>
5. Post 모델 설명
   - 이 모델은 제목(title), 내용(content), 작성일(created_at), 수정일(updated_at)을 저장한다.
   - 모델 클래스 내에는 필드를 정의하는 CharField, TextField, DateTimeField 등 다양한 필드 타입이 있으며, 이를 조합하여 모델을 정의할 수 있다.

<h3 id="section-23">데이터베이스 마이그레이션</h3>

1. 모델을 데이터베이스에 적용하기
   - 아직 데이터베이스에 생성한 모델이 적용되지 않았다.
   - 데이터베이스에 모델을 적용하는 과정을 "마이그레이션(migration)"이라고 한다.
   - 순서대로 명령어를 입력한다.
   - blog 앱에 대한 마이그레이션 파일을 생성한 후 데이터베이스에 적용한다.

``` 
$ python manage.py makemigrations blog
$ python manage.py migrate
```


<h2 id="section-3">3. 뷰 및 템플릿 작성</h2>

<h3 id="section-31">뷰 함수 작성</h3>

<h3 id="section-32">URL 패턴 작성</h3>

<h3 id="section-33">템플릿 작성</h3>


<h2 id="section-4">4. 정적 파일 관리</h2>

<h3 id="section-41">정적 파일 디렉토리 생성</h3>

<h3 id="section-42">정적 파일 설정</h3>

<h3 id="section-43">정적 파일 사용</h3>


<h2 id="section-5">5. 디버깅 및 테스트</h2>

<h3 id="section-51">디버깅</h3>

<h3 id="section-52">테스트 코드 작성</h3>

<h3 id="section-53">테스트 실행</h3>


<h2 id="section-6">6. 배포</h2>

<h3 id="section-61">서버 설정</h3>

<h3 id="section-62">데이터베이스 설정</h3>

<h3 id="section-63">스태틱 파일 및 미디어 파일 설정</h3>

<h3 id="section-64">WSGI 설정</h3>