[SQL Sample Data](https://dev.mysql.com/doc/index-other.html)

# Sakila Database
- 영화 DVD 대여점의 데이터를 모델링한 MySQL의 공식 샘플 데이터이다. 이 데이터로 SQL을 연습하려고 한다.

1. **MySQL 설치 확인**: MySQL이 설치되어 있지 않다면, [MySQL 공식 웹사이트](https://www.mysql.com/)를 통해 설치한다.

2. **Sakila Database 다운로드**:  [MySQL 사이트](https://dev.mysql.com/doc/index-other.html)에서 Sakila Database의 `.zip` 파일을 다운로드한다.

3. **압축 해제**: 다운로드한 `.zip` 파일을 압축 해제한다. 압축 해제하면 `sakila-schema.sql`과 `sakila-data.sql` 두 개의 SQL 파일이 포함되어 있을 것.

4. **MySQL에 접속**: 커맨드 라인 인터페이스(Command Line Interface, CLI)나 MySQL Workbench와 같은 GUI 툴을 사용하여 MySQL 서버에 접속한다.

5. **새 데이터베이스 생성**: MySQL 프롬프트에서 `CREATE DATABASE sakila;` 명령어를 실행하여 새로운 데이터베이스를 생성한다.

6. **Sakila 데이터베이스 선택**: 생성한 `sakila` 데이터베이스를 사용하도록 설정하기 위해 `USE sakila;` 명령어를 실행한다.

7. **스키마 로드**: `sakila-schema.sql` 파일을 MySQL에 로드한다. 이 파일은 데이터베이스 스키마(테이블, 뷰, 스토어드 프로시저 등)를 생성한다. 커맨드 라인에서는 `source [파일 경로]/sakila-schema.sql;` 명령을 사용한다.

8. **데이터 로드**: `sakila-data.sql` 파일을 MySQL에 로드하여 스키마에 데이터를 채웁니다. 이 파일은 실제 데이터를 포함하고 있습니다. 커맨드 라인에서는 `source [파일 경로]/sakila-data.sql;` 명령을 사용합니다.

9. **데이터베이스 검증**: 데이터베이스가 올바르게 로드되었는지 확인하기 위해 간단한 쿼리를 실행해 본다. 예를 들어, `SELECT * FROM sakila.actor;` 명령어를 실행하여 배우(actor) 테이블의 내용을 확인할 수 있다.