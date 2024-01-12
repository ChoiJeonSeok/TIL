## [MySQL 다운로드](https://dev.mysql.com/downloads/)

1. **``MySQL Installer for Windows`` 로 이동.**
![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/0c4f9a77-ce27-4ebb-8e90-d777254dfcfe)

2. **설치 파일을 다운**
- 로그인 또는 계정을 만들라고 나오면 No thanks, just start my download.를 눌러서 다운로드를 진행한다.
- 설치 파일로 설치할 수 있다. 또는 실행 파일들이 함께 있는 압출 폴더를 다운받을 수도 있다.
![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/cda66f25-3a44-4108-ba6e-7b999d995a4b)

3. **MySQL 서버 초기화**:
- 명령 프롬프트를 관리자 권한으로 열어야 한다.
- MySQL이 설치된 폴더로 이동한다. 
- `bin` 폴더로 이동한다: `cd bin`.
- MySQL 서버를 초기화한다: `mysqld --initialize`.
- MySQL을 Windows 서비스로 등록하기 위해, 다음 명령을 실행한다: `mysqld --install`.
- MySQL 서비스를 시작한다: `net start mysql`.
![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/ec189ec8-7790-4cd1-bc50-ca7c7ecac2f6)

4. **루트 비밀번호 설정**:
- 초기화 과정에서 생성된 임시 루트 비밀번호를 `data` 폴더의 로그 파일에서 찾는다. `.err 확장자` 파일에 있다고 한다.
![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/431bea0a-2457-457e-8c10-662726f10d65)
- MySQL에 접속한다: `mysql -u root -p`, 그리고 임시 비밀번호를 입력한다.
- 루트 비밀번호를 변경한다: `ALTER USER 'root'@'localhost' IDENTIFIED BY '새비밀번호';`.
![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/9d124f39-9307-46a0-9b36-8b9cc8538e13)


5. **환경 변수 설정**
- 필수는 아니지만 추천한다.
- 시스템 경로에 MySQL의 `bin` 폴더를 추가하여 어디에서나 MySQL 명령어를 실행할 수 있도록 한다.
- 시스템 속성 -> 고급 시스템 설정 -> 환경 변수 -> 시스템 변수에서 PATH 편집 -> 새로 만들기를 클릭하고 MySQL의 경로를 추가한다.

6. **Visual Studio Code 연결 설정**:
- Visual Studio Code에서 MySQL 확장 기능을 열고 새 연결을 추가한다.
- extensions에서 MySQL Shell for VS code를 다운 받는다.
- Shell 선택 창에 MySQL Shell for VS Code가 생성된 것을 볼 수 있다.
- Visual Studio Code 좌측 데이터베이스 탭으로![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/20211250-43cf-44fa-88a8-cf3c1cfed745) 이동하여 Create Connection을 클릭한다.
- 호스트는 `127.0.0.1` 또는 `localhost`, 포트는 `3306`, 사용자 이름은 `root`, 비밀번호는 4단계에서 설정한 비밀번호를 사용한다.