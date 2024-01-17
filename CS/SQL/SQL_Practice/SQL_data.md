### [SQL Sample Data](https://dev.mysql.com/doc/index-other.html)

# Sakila Database
- 영화 DVD 대여점의 데이터를 모델링한 MySQL의 공식 샘플 데이터이다. 이 데이터로 SQL을 연습하려고 한다.

1. **MySQL 설치 확인**: MySQL이 설치되어 있지 않다면, [MySQL 공식 웹사이트](https://www.mysql.com/)를 통해 설치한다.
- visual studio code를 사용하고 있으므로 MySQL Shell for VS Code Extension을 설치하였다.

2. **Sakila Database 다운로드**:  [MySQL 사이트](https://dev.mysql.com/doc/index-other.html)에서 Sakila Database의 `.zip` 파일을 다운로드한다.

3. **압축 해제**: 다운로드한 `.zip` 파일을 압축 해제한다. 압축 해제하면 `sakila-schema.sql`과 `sakila-data.sql` 두 개의 SQL 파일이 포함되어 있을 것이다.
![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/8fd59fbe-0203-4c15-8a69-37308b96420d)

4. **MySQL에 접속**: 커맨드 라인 인터페이스(Command Line Interface, CLI)나 MySQL Workbench와 같은 GUI 툴을 사용하여 MySQL 서버에 접속한다.

5. **새 데이터베이스 생성**: MySQL 프롬프트에서 `CREATE DATABASE sakila;` 명령어를 실행하여 새로운 데이터베이스를 생성한다.

6. **Sakila 데이터베이스 선택**: 생성한 `sakila` 데이터베이스를 사용하도록 설정하기 위해 `USE sakila;` 명령어를 실행한다.

7. **스키마 로드**: `sakila-schema.sql` 파일을 MySQL에 로드한다. 이 파일은 데이터베이스 스키마(테이블, 뷰, 스토어드 프로시저 등)를 생성한다. 커맨드 라인에서는 `source [파일 경로]/sakila-schema.sql;` 명령을 사용한다.

8. **데이터 로드**: `sakila-data.sql` 파일을 MySQL에 로드하여 스키마에 데이터를 채웁니다. 이 파일은 실제 데이터를 포함하고 있습니다. 커맨드 라인에서는 `source [파일 경로]/sakila-data.sql;` 명령을 사용합니다.

9. **데이터베이스 검증**: 데이터베이스가 올바르게 로드되었는지 확인하기 위해 간단한 쿼리를 실행해 본다. 예를 들어, `SELECT * FROM sakila.actor;` 명령어를 실행하여 배우(actor) 테이블의 내용을 확인할 수 있다.
 
## MySQL 데이터베이스와 sakila 파일 연동

1. **`sakila-schema.sql` 실행**:
   - 이 파일은 데이터베이스 스키마(테이블, 뷰 등의 구조)를 정의한다.
   - MySQL 서버에 접속한 후, `sakila` 데이터베이스를 생성하고 해당 파일을 실행하여 스키마를 구축한다.
     ```sql
     CREATE DATABASE sakila;
     USE sakila;
     SOURCE /path/to/sakila-schema.sql;
     ```
   - `/path/to/`는 `sakila-schema.sql` 파일의 실제 경로다.

2. **`sakila-data.sql` 실행**:
   - 이 파일에는 `sakila` 데이터베이스의 실제 데이터가 포함되어 있다.
   - 이미 `sakila` 데이터베이스를 선택한 상태(USE sakila)에서 데이터를 삽입한다.
     ```sql
     SOURCE /path/to/sakila-data.sql;
     ```

3. **`sakila.mwb` 파일**:
   - `.mwb` 확장자는 MySQL Workbench의 모델링 파일이다.
   - MySQL Workbench에서 열어 데이터베이스의 시각적 구조를 볼 수 있으며, 데이터베이스 설계 및 수정에 사용할 수 있다.
   - MySQL Workbench를 사용하여 해당 스키마를 기반으로 실제 데이터베이스 테이블을 생성하거나 수정할 수 있다.

### 데이터 조회 및 검증

1. **데이터베이스 선택**:
   - MySQL에 접속한 후, `sakila` 데이터베이스를 사용하도록 설정한다.
     ```sql
     USE sakila;
     ```

2. **테이블 목록 조회**:
   - `sakila` 데이터베이스에 어떤 테이블들이 있는지 확인한다.
     ```sql
     SHOW TABLES;
     ```
    ![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/8999b45b-6f20-48e6-9e7b-ec311035f4b8)


3. **각 테이블의 데이터 조회 및 검증**:
   - 특정 테이블의 데이터를 조회하여 검증한다. 
   - 예를 들어, `actor` 테이블의 데이터를 조회하는 경우
     ```sql
     SELECT * FROM actor;
     ```
    ![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/c9f2ab95-f3a7-4134-a740-16834b3c7a49)

    - 예를 들어, `film`, `customer`, `rental` 테이블의 데이터를 조회하려면 다음과 같이 실행한다.

     ```sql
     SELECT * FROM film;
     SELECT * FROM customer;
     SELECT * FROM rental;
     ```
    - 결과가 긴 시간동안 출력되었다. 모든 데이터를 항상 다 볼 필요는 없다. 때로는 10개만 보고 싶을 수도 있다. 그럴 때는 `LIMIT` 을 사용한다.


    ```sql
    SELECT * FROM film LIMIT 10;
    SELECT * FROM customer LIMIT 10;
    SELECT * FROM rental LIMIT 10;
    ```
    - 이렇게 하면 `film`, `customer`, `rental` 각 테이블에서 처음 10개의 행만을 조회하게 된다. 데이터의 샘플을 확인할 수 있는 것이다.
    ![image](https://github.com/ChoiJeonSeok/TIL/assets/82266289/5362c257-9cbd-4fe8-9f15-99baf51778bc)