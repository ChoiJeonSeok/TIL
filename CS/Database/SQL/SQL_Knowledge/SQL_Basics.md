# SQL 기초

### SQL 문의 필요성
1. 데이터베이스는 현대 사회의 중요한 자원인 데이터를 구조화하고 저장하며 효율적으로 관리하기 위해 사용된다.
2. SQL은 데이터베이스와 상호작용하기 위해 표준화된 언어이다. 
3. 작성의 목적
   1. 특정 조건을 충족하는 데이터를 필터링해서 가져와 조회할 수 있다.
   2. 데이터를 추가, 수정, 삭제하여 데이터베이스의 상태를 변경할 수 있다.
   3. 데이터베이스의 구조를 정의하거나 수정하여 데이터의 유형, 제약 조건, 관계 등을 정의할 수 있다.
4. 작성의 효과
   1. 필요한 정보를 빠르게 검색하여 의사 결정에 활용할 수 있다.
   2. SQL을 사용하여 데이터베이스에 접근하면 여러 사용자가 동시에 데이터를 수정하는 것을 방지하여 데이터 일관성을 유지할 수 있다.
   3. SQL을 통해 접근 권한을 관리하고 데이터의 무결성을 유지함으로써 보안을 강화할 수 있다.



## 1. SQL과 RDBMS 소개

### 관계형 데이터베이스의 개념
- 관계형 데이터베이스(RDBMS)는 데이터를 테이블 형식으로 저장하는 데이터베이스 관리 시스템.
- 테이블은 행(Row)과 열(Column)로 구성되며, 각 행은 고유한 ID(Primary Key)로 식별된다.

### SQL의 역할과 중요성
- SQL(Structured Query Language)은 RDBMS에서 데이터를 조회, 삽입, 수정, 삭제하는 등 다양한 작업을 수행하는 언어.
- 데이터 분석, 웹 개발, 데이터베이스 관리 등 다양한 분야에서 사용된다.

## 2. 데이터 타입과 스키마

### 기본 데이터 타입
- INTEGER: 정수형 데이터. (나이, 학년 등)
- FLOAT: 부동소수점 데이터. (점수, 가격 정보 등)
- TEXT, VARCHAR: 문자열 데이터. (VARCHAR은 길이 제한이 있는 문자열, TEXT는 길이 제한 없음)
- DATE, TIME, TIMESTAMP: 날짜와 시간. (DATE는 날짜만, TIME은 시간만, TIMESTAMP는 날짜와 시간)
- BOOLEAN: 참/거짓 값
- CHAR: 고정 길이의 문자열
- BLOB: 이진 데이터. (이미지나 파일을 저장할 때)

### 테이블 스키마 설계
- 테이블을 생성할 때 각 열의 데이터 타입과 제약 조건을 명시한다. 
- 제약 조건은 데이터의 무결성을 보장하기 위해 사용된다.<br><br>
- PRIMARY KEY: 유일한 값을 가지며, NULL을 허용하지 않는 필드
- FOREIGN KEY: 다른 테이블의 PRIMARY KEY를 참조하는 필드
- UNIQUE: 유일한 값을 가질 수 있는 필드
- NOT NULL: NULL 값을 허용하지 않는 필드
- DEFAULT: 기본값을 설정하는 필드
- 예: `CREATE TABLE Employees (ID INTEGER PRIMARY KEY, Name TEXT);`
- 예: 
```sql
CREATE TABLE Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Salary FLOAT DEFAULT 0.0
);
```

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

## 5. 별칭
### FROM, JOIN 절에서 테이블에 별칭을 할당할 수 있다.
- FROM tableA A
- tableA는 이제 A로 쓰일 수 있다.
- SELECT, WHERE, GROUP BY, HAVING, ORDER BY 등등

#### 쿼리는 쿼리 분석 후 전체 문장이 한번에 실행되며, 그 과정에서 parser가 정의된 별칭을 인식하고, 사용할 수 있게 한다. 
#### 따라서 별칭을 선언한 FROM 등이 맨 처음에 써있지 않아도 별칭 사용이 가능하다.

### SQL 논리적 실행 순서
1. `FROM` 절: 여기서는 필요한 테이블들을 불러온다.
2. `JOIN` 절: 여러 테이블을 연결한다.
3. `WHERE` 절: 조건에 맞는 레코드를 필터링한다.
4. `GROUP BY` 절: 특정 칼럼을 기준으로 데이터를 그룹화한다.
5. `HAVING` 절: 그룹화 한 후에 조건에 맞는 그룹을 필터링한다.
6. `SELECT` 절: 필요한 칼럼을 선택한다.
7. `ORDER BY` 절: 결과를 정렬한다.