# 데이터 조작 언어(Data Manipulation Language, DML)

### 기본 DML 문장
1. **INSERT 문**
    - **데이터 삽입**: 새로운 행을 테이블에 삽입한다.
      ```sql
      INSERT INTO table_name (column1, column2, column3, ...)
      VALUES (value1, value2, value3, ...);
      ```
    - **복수 행 삽입**: 여러 행을 한 번에 삽입할 수 있다.
      ```sql
      INSERT INTO table_name (column1, column2, column3, ...)
      VALUES (value1, value2, value3, ...),
             (value4, value5, value6, ...),
             ...;
      ```

2. **UPDATE 문**
    - **데이터 수정**: 테이블의 기존 행을 수정한다.
      ```sql
      UPDATE table_name                           # 데이터를 수정할 대상 테이블의 이름
      SET column1 = value1, column2 = value2, ... # 수정할 열과 해당 열에 들어갈 새로운 값
      WHERE some_column = some_value;             # 특정 조건을 만족하는 행만 수정
      ```
    - **조건부 수정**: `WHERE` 절을 사용하여 특정 조건에 맞는 행만 수정할 수 있다.

3. **DELETE 문**
    - **데이터 삭제**: 테이블의 행을 삭제한다.
      ```sql
      DELETE FROM table_name WHERE some_column = some_value;
      ```
    - **조건부 삭제**: `WHERE` 절을 사용하여 특정 조건에 맞는 행만 삭제할 수 있다.

4. **SELECT INTO**
    - 선택한 데이터를 새로운 테이블에 삽입한다.
    ```sql
    # 특정 조건을 만족하는 old_table의 행만 new_table에 삽입하겠다는 의미
    SELECT column1, column2 INTO new_table FROM old_table WHERE some_column = some_value;
    ```

5. **MERGE**
    - 두 테이블의 데이터를 결합한다. 일치하는 값이 있으면 `UPDATE`를, 없으면 `INSERT`를 수행한다.
    ```sql
    MERGE INTO target_table USING source_table    # 병합될 두 테이블의 이름
    ON (condition)                                # 두 테이블을 어떤 조건으로 병합할지를 정의
    WHEN MATCHED THEN 
        UPDATE SET column1 = value1, column2 = value2,...
    WHEN NOT MATCHED THEN
        INSERT (column1, column2, ... ) VALUES (value1, value2, ...);
    ```

6. **CALL**
    - 저장 프로시저를 호출한다.
    ```sql
    CALL procedure_name(arguments);               # 호출할 저장 프로시저와 필요한 인자
    ```

7. **EXPLAIN PLAN**
    - SQL 쿼리의 실행 계획을 확인한다.
    ```sql
    EXPLAIN PLAN FOR SELECT * FROM table_name;    # 실행 계획을 확인하고 싶은 SQL 쿼리
    ```

8. **LOCK TABLE**
    - 특정 테이블에 락을 걸어 다른 트랜잭션이 해당 테이블을 수정할 수 없게 한다. (READ, WRITE 등)
    ```sql
    LOCK TABLE table_name [IN lock_mode MODE];    # 특정 테이블에 락의 유형을 지정하여 걸음
    ```

9. **TRUNCATE**
    - 테이블의 모든 데이터를 빠르게 삭제한다. `DELETE`보다 빠르지만 롤백이 불가능하다.
    ```sql
    TRUNCATE TABLE table_name;
    ```