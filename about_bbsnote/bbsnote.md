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
  <ol>
  <li>from django.db import models : <br>Django에서 제공하는 models 모듈을 가져옵니다. 이 모듈은 데이터베이스 모델링을 위한 다양한 클래스와 필드를 제공합니다.</li>

   <li>class Post(models.Model): :<br>Post라는 모델 클래스를 선언합니다. 이 클래스는 models.Model 클래스를 상속받아 정의됩니다.</li>

   <li>title = models.CharField(max_length=200) : <br>CharField는 문자열 필드를 정의하는 클래스입니다. title 필드는 최대 길이가 200인 문자열 필드입니다.</li>

   <li>content = models.TextField() : <br>TextField는 긴 문자열을 저장할 수 있는 필드를 정의하는 클래스입니다. content 필드는 길이 제한이 없는 문자열 필드입니다.</li>

   <li>created_at = models.DateTimeField(auto_now_add=True) : <br>DateTimeField는 날짜와 시간을 저장하는 필드를 정의하는 클래스입니다. auto_now_add=True는 객체가 생성될 때 자동으로 현재 날짜와 시간을 저장하도록 설정한 옵션입니다.</li>

   <li>updated_at = models.DateTimeField(auto_now=True): <br>updated_at 필드는 객체가 저장될 때마다 자동으로 현재 날짜와 시간으로 갱신됩니다. 따라서 auto_now=True 옵션을 사용합니다.</li>

   <li>def __str__(self): : <br>__str__ 메서드는 객체를 문자열로 표현할 때 사용하는 메서드입니다.</li>

   <li>return self.title : <br>__str__ 메서드에서는 객체의 title 필드 값을 반환합니다. 이를 통해 Post 객체를 문자열로 출력할 때는 해당 객체의 title 값이 출력됩니다.</li></ol>
</details>


<br>
1. Post 모델 설명
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

```
# views.py
from django.shortcuts import render

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post_list.html', context)
```
1. post_list 함수 정의
   - post 모델의 모든 객체를 posts 변수에 저장.
   - context 딕셔너리에 posts 값을 담아 템플릿으로 전달한다.
   - render 함수란, 템플릿을 특정 context 와 함께 렌더링하는 기능을 수행하는 함수이다. 
     - 첫 번째 인자로 request 객체, 두 번째 인자로 렌더링할 템플릿의 경로, 세 번째 인자로 템플릿에 전달할 context 데이터를 받는다.
     - 넘겨받은 곳의 {{posts}}라는 부분에 posts 값이 들어간다.

<h3 id="section-32">URL 패턴 작성</h3>

```
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```
1. 빈 문자열 URL 패턴을 post_list 뷰 함수와 연결한다. name 매개변수로 URL 패턴에 이름을 지정했다.

<h3 id="section-33">템플릿 작성</h3>

1. base.html
   - 웹페이지의 뼈대가 되는 부분이며, 다른 HTML 파일들이 상속하여 사용할 수 있도록 구성된다.
   - templates 디렉토리에 생성한다.
   ```
      <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>{% block title %}Django Project{% endblock %}</title>
      {% block head %}
      <!-- 기본 head 내용 -->
      {% endblock %}
   </head>
   <body>
      {% block content %}
      <!-- 기본 content 내용 -->
      {% endblock %}
      {% block footer %}
      <!-- 기본 footer 내용 -->
      {% endblock %}
   </body>
   </html>
   ```

   ```
   <!-- post_list.html -->
   {% extends 'base.html' %}

   {% block content %}
   <h1>게시판</h1>
   {% for post in posts %}
      <div class="post">
         <h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>
         <p>{{ post.content }}</p>
         <p>작성자: {{ post.author.username }}</p>
      </div>
   {% empty %}
      <p>게시글이 없습니다.</p>
   {% endfor %}
   {% endblock %}
   ```
2. base.html을 확장한다.
   - content 블록에 게시판을 출력한다. 
   - posts 변수를 for 문을 사용하여 반복하면서 게시글의 제목, 내용, 작성자를 출력한다. 
   - {% empty %} 이 태그는 posts가 비어있을 때 출력할 내용을 정의한다.
  
3. 게시판 접속하기
   - 로컬 서버에서 실행 중인 경우 "http://127.0.0.1:8000/post_list" 또는 "http://localhost:8000/post_list"에 접속하면 게시판이 나타난다.

<h2 id="section-4">4. 정적 파일 관리</h2>

<h3 id="section-41">정적 파일 디렉토리 생성</h3>

1. blog 애플리케이션 디렉토리 안에 static 디렉토리를 생성해야 한다. 
   - static 안에는 앱에서 사용될 정적 파일들이 저장된다.
   - 애플리케이션과 같은 이름(blog)의 디렉토리를 생성한다. 나중에 다른 앱에서 같은 이름의 정적 파일을 생성할 경우 구분하기 위해서이다.
   - 위 과정을 마친 후의 대략적인 디렉토리 구조
   ```
   project/
    blog/
        static/
            blog/
    templates/
        base.html
        post_list.html
    manage.py
   ```

<h3 id="section-42">정적 파일 설정</h3>

1. 프로젝트 설정 파일 settings.py
   - STATIC_URL 변수를 지정한다.
   - 이 변수는 정적 파일이 참조될 URL을 지정하는 변수이다. 
   - 예시: STATIC_URL = '/static/'


<h3 id="section-43">정적 파일 사용</h3>

1. base.html 템플릿에서 정적 파일 사용.
   - static 템플릿 태그를 이용해서 css/styles.css 파일을 가져온다.

   ```
   {% load static %}

   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>{% block title %}{% endblock %}</title>
      <link rel="stylesheet" href="{% static 'blog/css/styles.css' %}">
   </head>
   <body>
      <div class="content">
         {% block content %}
         {% endblock %}
      </div>
   </body>
   </html>
   ```
2. post_list.html 템플릿에서 static 태그로 css 파일 적용하기
   ```
   {% extends 'base.html' %}

   {% block content %}
      <h1>Posts</h1>
      <ul>
         {% for post in posts %}
               <li><a href="#">{{ post.title }}</a></li>
         {% endfor %}
      </ul>
   {% endblock %}
   ```
   - {% extends 'base.html' %}로 base.html 상속. 따라서 content 내용만 작성.
   - base.html의 content 내용은 사용하지 않고, post_list.html에서 작성한 내용으로 대체.
3. overriding => 부토 템플릿에서 정의한 블록을 자식 템플릿에서 다시 정의하거나 변경하는 것. 필요에 따라 새로 또는 수정해서 사용할 수 있다.

<h2 id="section-5">5. 디버깅 및 테스트</h2>

<h3 id="section-51">디버깅</h3>

1. 디버깅이란?
   - 코드에서 발생한 오류를 찾고 수정하는 과정을 뜻한다. 
   - Django에서는 오류가 발생하면 서비스를 실행했을 때 웹페이지 상에 오류 메시지를 띄워 준다. 
   - 디버깅 페이지를 활성화하려면 settings.py 파일에 DEBUG=True 설정을 한다.
   - settings.py 파일에서 LOGGING 설정으로 로그를 사용하여 디버깅을 할 수도 있다.
2. pdb
   - python 자체 디버거

   ```
   def divide(a, b):
    result = a / b
    return result

   num1 = 10
   num2 = 0
   

   import pdb; pdb.set_trace() # 중단점 설정

   result = divide(num1, num2)

   print(result)
   ```
   - 코드를 실행하면 중단점에서 코드가 멈추고 pdb prompt가 나타난다. 
   - 확인하고 싶은 값을 prompt에 입력하면 된다.
   ```
   > /path/to/script.py(8)divide()
   -> result = a / b
   (Pdb) a
   10
   (Pdb) b
   0
   ```

<h3 id="section-52">테스트 코드 작성</h3>

1. tests.py
   - 각 앱 별로 tests.py 파일을 생성해야 한다. 테스트 케이스 클래스를 작성하고 메소드를 통해 각각의 테스트를 수행한다. 
   - assert 문 사용.
<details>
  <summary>테스트 코드</summary>
   from django.test import TestCase
   from django.urls import reverse

   from .models import Post

   class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test Post', body='Test content')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        self.assertEqual(expected_title, 'Test Post')

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
</details>
<details>
  <summary>테스트 코드 설명</summary>
  <ul><li>
위 코드에서는 Post 모델과 관련된 테스트를 작성하고 있다. </li><li>
setUpTestData 메소드를 이용해서 테스트 데이터를 생성하고, 이후에 test_title_content 메소드에서 Post 객체의 title 필드와 비교하는 테스트를 작성하고 있다. </li><li>또한 test_post_list_view 메소드에서는 post_list URL에 대한 요청을 보내서 응답 코드가 200인지, 그리고 'Test Post'라는 텍스트가 응답에 포함되어 있는지를 검증하는 테스트를 작성하고 있다.</ul>
</details>
<h3 id="section-53">테스트 실행</h3>

1. python manage.py test 명령어
   - Django는 모든 앱의 tests.py 파일을 검색하고, 그 파일 내에 정의된 모든 테스트 케이스를 실행한다. 
   - 각각의 테스트가 성공하면 . 출력
   - 실패하면 F 출력한다.
   - 이후 실패와 성공의 결과가 요약된다.

<h2 id="section-6">6. 배포</h2>

<h3 id="section-61">서버 설정</h3>

1. 웹 서버 설치 및 설정
2. SSL 인증서 설치 및 설정

<h3 id="section-62">데이터베이스 설정</h3>

1. 웹 서버와 Django 앱이 데이터베이스에 접근할 수 있는 권한 설정
2. 데이버베이스 설정 파일 수정

<h3 id="section-63">스태틱 파일 및 미디어 파일 설정</h3>

1. 스태틱 파일과 미디어 파일을 저장할 디렉토리 생성
2. 웹 서버와 Django 앱이 스태틱 파일과 미디어 파일에 접근할 수 있는 권한 설정
3. 스태틱 파일 및 미디어 파일 경로를 설정

<h3 id="section-64">WSGI 설정</h3>

1. 웹 서버와 Django 앱을 연동하기 위해 WSGI(Web Server Gateway Interface) 설정
2. WSGI 모듈 설치
3. WSGI 파일 생성