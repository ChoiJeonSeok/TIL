# html 기본 문법

## 태그
- html에서 태그(tag)는 가장 중요하다.
- 해당 문자열 등의 자료를 태그로 감싸면, 해당 태그의 목적에 맞게 정보가 변형된다.
- 태그는 열리고 닫힌다. <열림 태그>내용<\/닫힘 태그> 닫히는 태그는 앞에 /가 붙는다.
- \<strong>강조\</strong>
- <strong>강조</strong>
- 태그는 중첩해서 사용할 수 있다.

## 태그 사용량 통계 => 학습 우선순위
![elements](https://user-images.githubusercontent.com/82266289/228263392-5651bfd1-b513-4390-a261-9019dbb767a6.png)

## 줄바꿈
- \<br> 이란 태그는 html에서 줄바꿈의 역할을 한다.
- 닫히는 태그가 없는 이유는 어떤 정보를 설명하고 있지 않기 때문이다. 
- 하지만 \<br>은 줄바꿈의 역할이지, 단락을 표현하는 태그가 아니다.

## 단락 표현
- \<p> 태그는 \<br> 태그와 다르게 하나의 단락을 그룹핑할 수 있도록 열고 닫는다.
- 즉, 일정 내용을 한 단락으로 묶을 수 있다는 것이다. 그 안에서 줄바꿈이 일어나고, 이미지가 삽입되어도 한 단락으로 표현되는 것이다.
- 따라서 단락을 표현할 때는 줄바꿈 태그보다 p 태그를 사용하는 것이 좋다.
- 문제는 p는 단락 간의 간격이 정해져있다. 
- 이를 자유자재로 조절하려면 CSS를 사용해야 한다.
- \<p style="margin-top:45px;">
- style="margin-top:45px;" 는 p 태그 위쪽에 45만큼의 여백(margin)을 생성한다.
- 이제 원하는 만큼 여백을 생성하며 단락을 사용할 수 있게 되었다.

## 태그의 속성(attribute)
- image를 추가하여 글을 부연설명하고 싶다고 하자. \<img> 태그를 사용해서 image를 붙이고 싶은데, 어떤 image를 붙이고 싶은지 아직 모른다. 이때 속성을 사용한다.
- source를 의미하는 src에 image의 주소값을 부여하면 해당 image의 주소를 통해 image를 삽입할 수 있다. 
- \<img src="주소">
- 인터넷에 있는 image의 주소를 입력하면 내 컴퓨터에 해당 image가 없어도 괜찮다.
- 내 컴퓨터에 있는 image를 표시하고 싶다면 해당 디렉토리를 명시하면 된다. 
- 웹페이지 파일과 image 파일이 같은 위치에 있다면 image 파일의 이름만 적어주면 된다.
- width라는 속성을 이용하면 숫자나 %를 사용하여 원하는 크기로 image 크기를 조정할 수 있다.
- \<img src="주소" width="100%>