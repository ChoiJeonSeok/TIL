# SQL 기초

## 1. SQL과 RDBMS 소개

### 관계형 데이터베이스의 개념
- 관계형 데이터베이스(RDBMS)는 데이터를 테이블 형식으로 저장하는 데이터베이스 관리 시스템.
- 테이블은 행(Row)과 열(Column)로 구성되며, 각 행은 고유한 ID(Primary Key)로 식별된다.

### SQL의 역할과 중요성
- SQL(Structured Query Language)은 RDBMS에서 데이터를 조회, 삽입, 수정, 삭제하는 등 다양한 작업을 수행하는 언어.
- 데이터 분석, 웹 개발, 데이터베이스 관리 등 다양한 분야에서 사용된다.

## 2. 데이터 타입과 스키마

### 기본 데이터 타입
- INTEGER: 정수형 데이터
- FLOAT: 부동소수점 데이터
- TEXT, VARCHAR: 문자열 데이터
- DATE, TIME: 날짜와 시간

### 테이블 스키마 설계
- 테이블을 생성할 때 각 열의 데이터 타입과 제약 조건을 명시한다.
- 예: `CREATE TABLE Employees (ID INTEGER PRIMARY KEY, Name TEXT);`

## 3. 기본 쿼리 작성

### SELECT 문
- 데이터베이스에서 특정 테이블의 데이터를 조회할 때 사용한다.
- 예: `SELECT * FROM Employees;` # 모든 column 선택
- 예: `SELECT column1, column2 FROM table_name;`

### WHERE 절
- 조회할 데이터의 조건을 명시한다.
- 예: `SELECT * FROM table_name WHERE condition;`
- 예: `SELECT * FROM Employees WHERE ID=1;`

### ORDER BY, LIMIT, OFFSET
- 조회된 데이터의 정렬 순서와 개수를 지정한다.
- ORDER BY: 조회된 결과를 특정 column 기준으로 정렬한다.
- 예: `SELECT * FROM table_name ORDER BY column1 ASC;`
- LIMIT: 조회되는 record의 수를 제한한다.
- 예: `SELECT * FROM table_name LIMIT 5;`
- OFFSET: 몇 번째 record 부터 조회할지 지정한다.
- 예: `SELECT * FROM table_name LIMIT 5 OFFSET 2;`
<br><br>
- 문: `Employees` 테이블에서 `ID`로 정렬된 record 중 2번째부터 6번째까지의 record를 반환하라.
- 답: `SELECT * FROM Employees ORDER BY ID LIMIT 5 OFFSET 1;`

## 4. 함수와 연산자

### 수치형, 문자열, 날짜 함수
- `ABS()`, `ROUND()`: 수치형 함수
- `UPPER()`, `LOWER()`: 문자열 함수
- `NOW()`, `DATE_ADD()`: 날짜 함수

### 논리 연산자와 비교 연산자
- `AND`, `OR`: 논리 연산자
- `=`, `>`, `<`: 비교 연산자
