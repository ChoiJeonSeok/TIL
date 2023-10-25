# SQL_Queries

## JOIN 연산

### INNER JOIN
- **정의**: 두 테이블에서 특정 조건에 일치하는 행만 결합한다.
- **예시**: `tableA`와 `tableB`에서 `id`가 일치하는 행만 선택하여 결합함.
    ```sql
    SELECT A.column1, B.column2 
    FROM tableA A 
    INNER JOIN tableB B ON A.id = B.id;
    ```
- **사용 사례**: 회원 정보와 주문 내역을 연결할 때 사용할 수 있다.

### LEFT JOIN
- **정의**: 왼쪽 테이블의 모든 행과 오른쪽 테이블의 일치하는 행을 결합한다. 일치하지 않는 경우 NULL 값을 반환한다.
- **예시**: `tableA`의 모든 행과 `tableB`에서 일치하는 행을 결합한다. `tableB`에 일치하는 행이 없으면 NULL 반환.
    ```sql
    SELECT A.column1, B.column2 
    FROM tableA A 
    LEFT JOIN tableB B ON A.id = B.id;
    ```
- **사용 사례**: 회원 정보와 그 회원의 주문 내역을 보고 싶지만, 주문 내역이 없는 회원도 포함해야 할 때 

### RIGHT JOIN
- **정의**: 오른쪽 테이블의 모든 행과 왼쪽 테이블의 일치하는 행을 결합한다. 일치하지 않는 경우 NULL 값을 반환한다.
- **예시**
    ```sql
    SELECT A.column1, B.column2 
    FROM tableA A 
    RIGHT JOIN tableB B ON A.id = B.id;
    ```
- **사용 사례**: 주문 내역과 그 주문을 한 회원 정보를 보고 싶지만, 주문을 한 적이 없는 회원을 제외하고 싶을 때

### 복잡한 JOIN 쿼리
- **정의**: 여러 테이블과 조건을 사용한 복잡한 JOIN 연산
- **예시**: `tableA`, `tableB`, `tableC`를 다양한 방식으로 결합하면서 `WHERE`의 조건을 적용
    ```sql
    SELECT A.column1, B.column2, C.column3 
    FROM tableA A 
    INNER JOIN tableB B ON A.id = B.id
    LEFT JOIN tableC C ON A.id = C.id
    WHERE A.column1 > 10;
    ```
- **사용 사례**: 회원 정보, 주문 내역, 그리고 리뷰 등 여러 테이블을 결합해야 할 때
- 
## 서브쿼리

### IN, EXISTS, ALL, ANY
- **정의**: `IN`은 주어진 값 목록 중 하나와 일치하는지, `EXISTS`는 서브쿼리의 결과가 존재하는지, `ALL`은 모든 조건을 만족하는지, `ANY`는 어느 하나의 조건을 만족하는지를 확인한다.
- **예시**: `tableB`의 `id` 값과 `tableA`의 `id`값과 일치하는 모든 값 출력.
    ```sql
    SELECT * FROM tableA WHERE id IN (SELECT id FROM tableB);
    ```

### 스칼라 서브쿼리
- **정의**: 단일 값을 반환하는 서브쿼리.
- **예시**: `tableA`의 각 행에 대하여 `tableB`에서 계산한 평균 나이(`AVG(age)`)를 `ave_age`라는 열로 추가하여 출력.
    ```sql
    SELECT name, (SELECT AVG(age) FROM tableB) AS avg_age FROM tableA;
    ```

## 집계 함수와 GROUP BY

### COUNT, SUM, AVG 등
- **정의**: `COUNT`는 행의 수를 세고, `SUM`은 값을 합산하며, `AVG`는 평균 값을 계산한다.
- **예시**: `tableA`에서 모든 행의 수를 count 하고 `column1`의 합계와 `column2`의 평균을 계산.
    ```sql
    SELECT COUNT(*), SUM(column1), AVG(column2) FROM tableA;
    ```

### HAVING 절
- **정의**: `GROUP BY`로 묶인 결과에 추가적인 조건을 적용한다.
- **예시**: `tableA`에서 `column1`을 기준으로 그룹을 묶고, 그룹 내 행의 수가 1보다 큰 경우만 출력
    ```sql
    SELECT column1, COUNT(*) 
    FROM tableA 
    GROUP BY column1
    HAVING COUNT(*) > 1;
    ```

## 윈도우 함수

### RANK(), DENSE_RANK(), NTILE()
- **정의**: `RANK()`는 순위를 계산하고, `DENSE_RANK()`는 중복을 허용하지 않는 순위를 계산하며, `NTILE()`은 결과를 분할한다.
- **예시**: `tableA`에서 `column1`을 기준으로 순위를 매기고 (`RANK()`), 중복을 허용하지 않는 순위를 매기며 (`DENSE_RANK()`), 결과를 4개의 타일로 분할.
    ```sql
    SELECT RANK() OVER (ORDER BY column1), DENSE_RANK() OVER (ORDER BY column1), NTILE(4) OVER (ORDER BY column1) 
    FROM tableA;
    ```

### PARTITION BY, ORDER BY
- **정의**: `PARTITION BY`는 결과를 특정 기준으로 분할하고, `ORDER BY`는 결과를 정렬한다.
- **예시**: `tableA`에서 `column1`을 기준으로 결과를 분할한 뒤, `column2`를 기준으로 순위를 매긴다.
    ```sql
    SELECT RANK() OVER (PARTITION BY column1 ORDER BY column2) 
    FROM tableA;
    ```