# 목차 및 연습 예시

1. **기본 데이터 조회**
   - `SELECT` 문을 사용하여 각 테이블의 데이터 조회.
   - 예시: `SELECT * FROM film WHERE release_year = 2006;`

2. **복잡한 조건으로 데이터 필터링**
   - 다양한 `WHERE` 절 조건을 사용하여 데이터 필터링.
   - 예시: `SELECT * FROM customer WHERE store_id = 1 AND active = 1;`

3. **데이터 정렬 및 집계**
   - `ORDER BY`, `GROUP BY`, `HAVING` 절을 사용하여 데이터 정렬 및 집계.
   - 예시: `SELECT category_id, COUNT(*) FROM film GROUP BY category_id HAVING COUNT(*) > 10;`

4. **다중 테이블 조인**
   - 여러 테이블을 조인하여 관련 데이터 검색.
   - 예시: `SELECT customer.first_name, customer.last_name, rental.rental_date FROM customer JOIN rental ON customer.customer_id = rental.customer_id WHERE customer.customer_id = 5;`

5. **서브쿼리 및 복합 쿼리**
   - 서브쿼리를 사용하여 복잡한 쿼리 구성.
   - 예시: `SELECT title FROM film WHERE film_id IN (SELECT film_id FROM film_actor WHERE actor_id = 1);`

6. **윈도우 함수 사용**
   - `OVER()`, `PARTITION BY` 등의 윈도우 함수를 사용하여 고급 데이터 분석.
   - 예시: `SELECT first_name, last_name, RANK() OVER (ORDER BY last_update DESC) FROM actor;`

7. **데이터 수정 및 관리**
   - `INSERT`, `UPDATE`, `DELETE` 명령어를 사용하여 데이터 삽입, 수정, 삭제 연습.
   - 예시: `UPDATE film SET rental_duration = 10 WHERE title = 'ACADEMY DINOSAUR';`

8. **데이터 무결성 및 제약 조건**
   - 테이블 생성 및 수정 시 데이터 무결성을 위한 제약 조건 설정 연습.
   - 예시: `ALTER TABLE film ADD CONSTRAINT chk_rental_rate CHECK (rental_rate > 0);`

9. **트랜잭션 관리**
   - `BEGIN`, `COMMIT`, `ROLLBACK`을 사용하여 트랜잭션 처리 연습.
   - 예시: `START TRANSACTION; DELETE FROM rental WHERE rental_id = 10; ROLLBACK;`

10. **성능 최적화 및 쿼리 튜닝**
    - 실행 계획(`EXPLAIN`)을 사용하여 쿼리 성능 분석 및 최적화 연습.
    - 예시: `EXPLAIN SELECT * FROM rental WHERE return_date IS NULL;`



## 연습을 통해 향상시킬 수 있는 능력
- **데이터 검색 및 분석 능력**: 복잡한 쿼리를 작성하고 실행하여 필요한 정보를 추출하는 능력.
- **문제 해결 능력**: 주어진 요구 사항에 따라 적절한 SQL 쿼리를 구성하여 문제를 해결하는 능력.
- **데이터베이스 관리 능력**: 데이터 무결성을 유지하고, 트랜잭션을 관리하는 능력.
- **성능 최적화 능력**: 쿼리 성능을 분석하고 최적화하는 능력.

## 트랜잭션(Transaction)
- 하나의 논리적인 작업 단위
- 여러개의 데이터베이스 명령으로 구성된 명령문이 있다면, 이 명령들은 모두 성공적으로 실행되거나 모두 취소되어 명령이 입력되기 전 상태로 돌아가야 함.
- 명령문 중 단 하나의 명령이라도 실패하면 전체가 취소되어야 한다.

### 트랜잭션의 주요 특징
1. 원자성(Atomicity): 트랜잭션 내의 모든 작업은 모두 완료되거나 모두 실행되지 않아야 한다. 작업 혹은 작업들은 분할 불가능한 하나의 단위로 취급된다.
2. 일관성(Consistency): 트랜잭션이 완료된 후에는 데이터의 무결성이 유지되어야 한다. 데이터베이스에 수정이 이뤄지더라도 규칙과 제약조건을 준수하면서 수정이 이뤄져야 한다.
3. 독립성(Isolation): 동시에 여려 트랜잭션이 실행되더라도 서로 영향을 주지 않고 독립적으로 실행되어야 한다. 어느 한 트랜잭션의 진행 과정을 다른 트랜잭션이 조회, 수정 등 영향을 끼칠 수 없다. 
   - [격리 수준(Isolation Level)](https://github.com/ChoiJeonSeok/TIL/blob/master/etc/Coming_Soon.md)을 참고할 것.
4. 지속성(Durability): 트랜잭션이 성공적으로 완료되면, 그 결과는 영구적으로 데이터베이스에 반영되어야 한다.