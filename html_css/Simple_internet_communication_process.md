# 인터넷이 동작하는 기본 원리
- 서로 다른 두 대의 컴퓨터가 통신할 수 있다면, 인터넷이 있다고 봐도 좋다.
<ol>
<li>예를 들면 http://example.com/webpage.html 이라는 사이트가 있다.</li>
<li>웹브라우저의 주소창에 주소를 입력하면 인터넷을 통해 해당 주소의 컴퓨터에게 신호를 보낸다.</li>
<li>이는 해당 웹페이지의 소스 코드, 다시 말해 webpage.html 이라는 파일의 코드를 요청하는 것이다.</li>
<li>그러면 그 컴퓨터는 example.com에 설치된 웹서버 프로그램이 webpage.html이라는 파일을 찾는다. 그리고 내용을 읽어 전기 신호로 웹브라우저가 설치된 컴퓨터에 신호를 보낸다.</li>
<li>웹브라우저가 설치된 컴퓨터에 webpage.html 파일의 코드가 도착한다. 이 코드를 읽어서 화면에 출력하는 것이다.</li>
</ol>
- 그래서 인터넷이 도중에 끊겨도, 새로고침이 되지 않는 한 현재 열려 있는 웹페이지는 그대로 있는 것이다.

## client & server
- client(고객)은 요청하고
- server(사업자)는 응답한다.
- 웹브라우저는 client 컴퓨터에서 동작하고, 웹서버는 server 컴퓨터에서 동작한다.
- 게임 프로그램이 게임 client이고, 게임 회사에 설치된 프로그램이 게임 server이다.
> 결국, client와 server의 본질은 통신이다. 모스 부호로 통신한다 했을 때, 일어나는 과정과 크게 다르지 않다. 신호를 보내면 이를 받아 인간이 이해할 수 있는 형태로 표현하는 것이다.
 

![image](https://user-images.githubusercontent.com/82266289/229356977-a45493b4-2ace-4854-b3a7-bc599dffe742.png)