# 쿼리 최적화 기초

## 실행 계획 분석
- **정의**: 실행 계획은 데이터베이스가 쿼리를 어떻게 수행할지에 대한 로드맵이다. 이를 분석함으로써 쿼리의 성능을 이해하고 개선할 수 있다.
- **이유**: 실행 계획을 분석함으로써 어떤 부분에서 병목 현상이 일어나는지, 어떤 인덱스가 사용되고 있는지, 어떤 방식으로 데이터가 탐색이 되는지 등을 알 수 있다. 이러한 정보를 바탕으로 쿼리를 최적화할 수 있다.
  
- **사용법**: 대부분의 데이터베이스 관리 시스템(DBMS)에서는 `EXPLAIN`이나 `EXPLAIN PLAN`과 같은 명령어를 사용하여 실행 계획을 확인할 수 있다.
    ```sql
    EXPLAIN SELECT * FROM tableA WHERE column1 = 'value';
    ```
  
- **분석 방법**: 실행 계획을 통해 테이블 스캔의 유무, 사용된 인덱스, 조인 방법 등을 확인할 수 있다.

## 쿼리 최적화
- **이유**: 잘못된 쿼리는 시스템 리소스를 불필요하게 많이 사용하게 만들고 응답 시간을 느리게 할 수 있다.
- **예시**: `employees` 테이블에서 `salary`가 5,000,000원 이상인 직원의 이름을 가져오는 쿼리를 작성했다. 그런데 `salary` 컬럼에는 인덱스가 없다고 하자. 그러면 이 쿼리는 `employees` 테이블의 모든 행을 스캔한다. 데이터가 많을수록 비효율적이다. 이 경우 인덱스를 추가하면 된다.

    ```sql
    CREATE INDEX idx_salary ON employees(salary);
    SELECT name FROM employees WHERE salary >= 5000000;
    ```
    이제 인덱스를 사용하여 정렬된 자료 구조 속에서 데이터 값을 빠르게 찾을 수 있다. B-Tree 같은 구조가 주로 사용된다.

- 그 외에도 암시적 조인을 사용하는 대신 명시적인 INNER JOIN을 사용하면, 성능에 큰 변화가 생기지는 않지만 쿼리의 가독성과 명확성이 향상된다. 이 경우 성능에 큰 변화가 생기기보다 가독성과 명확성, SQL 표준 등을 따르는 쿼리문으로 최적화를 시키는 것이다.

### 쿼리 최적화 팁
- **WHERE 절 최적화**: 불필요한 조건은 제거하고, 인덱스를 활용할 수 있는 조건을 사용하자.
- **JOIN 최적화**: 가능하면 INNER JOIN을 사용하고, 필요한 컬럼만 SELECT 하자.
- **결과 집합 최적화**: `LIMIT`과 `OFFSET`을 적절히 사용하여 필요한 만큼의 데이터만 가져오자.

# 인덱스 튜닝

## 인덱스 선택 기준
- **정의**: 모든 컬럼에 인덱스를 생성하는 것은 비효율적이다. 따라서 어떤 컬럼에 인덱스를 생성할지를 결정하는 기준이 필요하다.
- **선택 기준**: 
    1. WHERE, JOIN, ORDER BY 절에서 자주 사용되는 컬럼
    2. 데이터의 카디널리티가 높은 컬럼
    3. 읽기 작업이 많고, 쓰기 작업이 적은 컬럼

## 클러스터링, 논클러스터링 인덱스
### **클러스터링 인덱스**
- 데이터 테이블의 레코드를 물리적으로 재배열하여 인덱스의 키 값에 따라 정렬하여 데이터를 빠르게 읽을 수 있게 함.
- 디스트에 데이터를 저장하는 순서가 클러스터링 인덱스의 키 값에 따라 정렬되어 저장됨.
- 데이터 조회시 키 값에 따라 정렬된 물리적인 데이터 블록을 직접 읽어 처리, 정렬되어 검색 속도 빠름.
    - **예시**: `Employees` 테이블에 `EmplyeeID`를 기준으로 클러스터링 인덱스를 생성한다. 그렇게 하면 디스크에 `EmplyeeID` 값에 따라 레코드가 물리적으로 정렬되어 저장된다.
    ```sql
    CREATE CLUSTERED INDEX index_name ON table_name(column_name);
    ```
  
### **논클러스터링 인덱스**
- 데이터의 물리적인 저장 순서를 변경하지 않고, 별도의 공간에 인덱스를 저장하는 방법.
- 색인 기능을 사용하기 위해 별도의 공간에 인덱스를 저장함. 
- 공간의 크기는 인덱스를 구성하는 컬럼의 타입과 테이블의 레코드 수에 따라 다르다.
    - **예시**: `Emplyees` 테이블에 `EmployeeName`을 기준으로 논클러스터링 인덱스를 생성함. 데이터는 변경되지 않으며 `EmplyeeName` 값과 해당 레코드가 저장된 위치에 대한 정보만 별도의 공간에 저장된다.
    ```sql
    CREATE NONCLUSTERED INDEX index_name ON table_name(column_name);
    ```

### **어떤 것을 사용할까**: 
- **속도 vs 메모리**: 클러스터링 인덱스는 읽기 속도가 빠르지만, 데이터 삽입, 수정, 삭제 등의 쓰기 작업에는 느릴 수 있다. 논클러스터링 인덱스는 별도의 저장 공간이 필요하므로 메모리 사용량이 늘어난다. 따라서 읽기 작업의 속도 향상이 필요한 경우 클러스터링 인덱스를, 쓰기 작업의 속도 향상이 필요한 경우 논클러스터링 인덱스를 사용하는 것이 좋다.
- **적용 사례**: 자주 조회되는 대용량의 데이터베이스에서 특정 컬럼을 기준으로 빠르게 데이터를 조회해야 한다면 클러스터링 인덱스를 사용하는 것이 유리하다. 반면에 쓰기 작업이 빈번하고, 여러 컬럼을 기준으로 검색이 이루어진다면 논클러스터링 인덱스를 사용하는 것이 좋다.