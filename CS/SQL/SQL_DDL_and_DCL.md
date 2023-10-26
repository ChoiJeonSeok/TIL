## 데이터 정의 언어(DDL: Data Definition Language)

#### 정의
- DDL은 데이터베이스 스키마와 설명, 그리고 그 스키마에 대한 여러 종류의 물리적 세부 사항들을 정의하기 위한 언어. 

#### 사용 이유
- 데이터 구조를 만들거나 수정할 때 사용한다. 예를 들어, 테이블을 만들거나, 컬럼을 추가하거나 삭제할 때 사용한다.


## 데이터 제어 언어(DCL: Data Control Language)

#### 정의
- DCL은 데이터베이스에 저장된 데이터에 대한 접근을 제어하는 언어.

#### 사용 이유
- 특정 사용자에게 특정 데이터에 대한 권한을 주거나 빼앗을 때 사용한다.

## 1. 테이블 생성과 변경

### CREATE
- 새로운 테이블을 생성한다.
- 예시: `employees`라는 이름의 새 테이블을 생성하고, `id`, `name`, `age`라는 컬럼을 가진다.
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
```

### ALTER
- 이미 존재하는 테이블을 변경한다. 예를 들어, 컬럼을 추가하거나 삭제할 수 있다.
- 예시:  `employees` 테이블에 `salary`라는 새로운 컬럼을 추가한다.
```sql
ALTER TABLE employees ADD COLUMN salary INT;
```

### DROP
- 테이블을 삭제한다.
- 예시: `employees` 테이블을 삭제한다.
```sql
DROP TABLE employees;
```


## 2. 인덱스

### 인덱스 생성과 사용
- 데이터의 검색 속도를 향상시키기 위한 자료 구조.
- 예시: `employees` 테이블의 `name` 컬럼에 인덱스를 생성하여 검색 성능을 향상시킨다.
```sql
CREATE INDEX idx_employee_name ON employees (name);
```

### 인덱스 튜닝
- 인덱스의 성능을 최적화한다. 예를 들어, 불필요한 인덱스를 제거하거나, 컬럼의 순서를 변경할 수 있다.

## 3. 권한 관리

### GRANT
- 사용자에게 특정 작업을 수행할 수 있는 권한을 부여한다.
- 예시: `some_user` 사용자에게 `employees` 테이블에 데이터를 조회하고 삽입할 권한을 부여한다.
```sql
GRANT SELECT, INSERT ON employees TO some_user;
```

### REVOKE
- 사용자로부터 특정 권한을 빼앗는다.
- 예시: `some_user` 사용자로부터 `employees` 테이블에 데이터를 조회하고 삽입할 권한을 회수한다.
```sql
REVOKE SELECT, INSERT ON employees FROM some_user;
```

### 사용자 관리
- 데이터베이스에 접근할 수 있는 사용자를 관리한다. 사용자를 생성, 삭제, 권한을 할당하는 등의 작업을 수행한다.