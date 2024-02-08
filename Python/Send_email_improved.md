# 파이썬으로 이메일 보내기

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```
- `smtplib`: Python에서 이메일을 보내기 위해 사용하는 표준 라이브러리
- `email.mime.text`: 이메일 본문을 만들기 위한 모듈
- `email.mime.multipart`: 여러 파트(텍스트, HTML 등)를 가진 이메일 메시지를 만들기 위한 모듈

### credentials.txt: 발신자의 이메일 주소와 비밀번호(애플리케이션 코드)
```txt
your_email@gmail.com
your_password
```
- 이메일 발신자와 수신자의 주소를 설정한다. 
- 발신자의 이메일 주소와 비밀번호는 실제 사용하는 계정 정보여야 한다.
- 발신자의 이메일 주소와 비밀번호를 안전하게 관리하기 위해 별도의 파일에 저장하고 읽어오는 것이 좋다.

```python
# 발신자 이메일 및 비밀번호 읽기
with open('credentials.txt', 'r') as file:
    sender_email = file.readline().strip()  # 첫 번째 줄에 이메일
    password = file.readline().strip()      # 두 번째 줄에 비밀번호
```

### receiver.txt: 수신자의 이메일 주소
```txt
receiver1@gmail.com
receiver2@gmail.com
```
```python
# 개행으로 구분된 수신자 이메일 읽기
with open('receivers.txt', 'r') as file:
    receiver_emails = file.read().splitlines()
```



```python
message = MIMEMultipart("alternative")

location = "서울"
weather_condition = "폭염"
subject = f"{location}에 {weather_condition} 발생 예정!"

message["Subject"] = subject  # 이메일 제목을 동적으로 변경할 수 있음.
message["From"] = sender_email
message["To"] = receiver_email
```
- `MIMEMultipart("alternative")`: 텍스트와 HTML을 포함한 이메일을 생성한다.
- 이메일의 제목, 발신자, 수신자를 설정한다.

```python
with open('text.txt', 'r') as file:
    text = file.read()

with open('html.html', 'r') as file:
    html = file.read()
```
- 이메일의 본문을 텍스트와 HTML 형식으로 작성한다.
- 서로 내용이 다른 경우 HTML 버전을 우선하여 전송한다. 텍스트 버전은 HTML을 지원하지 않거나 접근성 설정(시각 장애인이 주로 사용하는 스크린 리더)가 있는 경우 유용하다.
- 수신자가 HTML 형식 이메일을 차단하고 있을 수도 있다.

```python
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)
```
- `MIMEText` 객체를 사용하여 이메일의 텍스트 및 HTML 파트를 생성한다.
- `attach` 함수를 사용하여 이러한 파트들을 메시지에 추가한다.

```python
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)  # Gmail 로그인
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )  # 이메일 전송
```
- `smtplib.SMTP_SSL`: SMTP 서버에 안전하게 연결하기 위해 SSL(Secure Sockets Layer)을 사용한다. `smtp.gmail.com`과 포트 `465`는 Gmail을 위한 설정.
- `login`: 이메일 서버에 로그인.
- `sendmail`: 이메일을 발송.

### 변경할 것.
- 코드 내 이메일 주소, 내용, 비밀번호 등을 직접 입력하지 않고 파일로 대체할 수 있는 방법 알아보기.