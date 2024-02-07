# 파이썬으로 이메일 보내기

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```
- `smtplib`: Python에서 이메일을 보내기 위해 사용하는 표준 라이브러리
- `email.mime.text`: 이메일 본문을 만들기 위한 모듈
- `email.mime.multipart`: 여러 파트(텍스트, HTML 등)를 가진 이메일 메시지를 만들기 위한 모듈

```python
sender_email = "your_email@gmail.com"  # 여기에 발신자 이메일 주소 입력
receiver_email = "receiver_email@gmail.com"  # 수신자 이메일 주소
password = "your_password"  # 여기에 Gmail 어플리케이션 코드 입력
```
- 이메일 발신자와 수신자의 주소를 설정한다. 
- 발신자의 이메일 주소와 비밀번호는 실제 사용하는 계정 정보여야 한다.

```python
message = MIMEMultipart("alternative")
message["Subject"] = "안녕하세요!"  # 이메일 제목
message["From"] = sender_email
message["To"] = receiver_email
```
- `MIMEMultipart("alternative")`: 텍스트와 HTML을 포함한 이메일을 생성한다.
- 이메일의 제목, 발신자, 수신자를 설정한다.

```python
text = "안녕!"
html = "<html><body><p>안녕!</p></body></html>"
```
- 이메일의 본문을 텍스트와 HTML 형식으로 작성한다.

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