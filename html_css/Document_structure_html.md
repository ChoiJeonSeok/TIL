# 문서의 구조
- 책에는 표지가 있다. 표지에는 제목과 저자가 있다.
- 표지를 넘기면 목차가 있다. 목차에는 책에 담긴 정보의 흐름이 있다.
- 문서의 구조는 정보를 정리정돈하여 정보의 습득 효율을 상승시키기 위해 존재한다.

## 웹페이지가 깨지는 이유
- 페이지를 열었는데, 알 수 없는 글자들로 이루어진 화면을 본 적이 있다. 
- 영문만 제대로 나타나고 한글은 깨지는 경우도 있다. 
- 웹페이지가 저장된 문자 표현 방식과 웹브라우저가 웹페이지를 해석하는 방식이 일치하지 않으면 문자가 깨지게 된다.
### 웹페이지를 깨지지 않게 작성하는 방법
- \<!doctype html>을 문서의 맨 위에 선언하여 HTML로 만들어졌다는 것을 알린다. 
- 이후 \<html>\</html>로 문서 전체를 감싼다.
- \<title>WEB1 - html\</title>
- \<meta charset="utf-8">
- 위 두 줄은 HTML 문서의 헤더 부분이다.
- 웹브라우저에게 내가 만든 웹페이지가 어떤 방식으로 쓰여있는지 알려주는 역할을 한다. 
- 웹브라우저는 헤더를 읽고 웹 페이지를 올바르게 렌더링한다.
- \<title> : 페이지의 제목을 정의합니다.<br>
\<meta> : 문서의 문자 인코딩 및 기타 메타 데이터를 정의합니다.<br>charset="utf-8"은 문자 인코딩을 UTF-8로 설정합니다.
- head 태그를 이용해 감싼다.
```
<!doctype html>
<html>
<head>
    <title>WEB1 - html</title>
    <meta charset="utf-8">
</head>
<body>
    내용
</body>
</html>
```

## Anchor & HyperText Reference
<ul>
<li>a라는 태그는 anchor의 약자로 문자 또는 이미지에 링크를 건다. 클릭시 해당 링크로 이동하게 된다.</li>
<li>herf는 HyperText Reference의 약자로 herf="링크의 주소"로 사용한다.</li>
<li>target="_blank" 옵션을 주면 새창에서 열리고 쓰지 않으면 창을 이동한다.</li>
<li>title="내용" 옵션을 주면 마우스 등을 올렸을때 해당 링크에 대한 설명이 팝업된다. 링크로 이동하기 전에 링크가 어떤 웹사이트로 연결되는지 미리 알 수 있는 역할을 한다.</li>
</ul>

```
예시.
<a href="https://www.w3.org/TR/html5/" target="_blank" title="html5 specification">Hypertext Markup Language (HTML)</a>
```