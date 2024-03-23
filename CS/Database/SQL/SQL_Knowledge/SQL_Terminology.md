# SQL 용어

1. **데이터베이스 구조와 설계**

<img src="https://github.com/ChoiJeonSeok/TIL/assets/82266289/6ca9396d-f782-4f09-b33e-e0a6c94635af" width="80%">

   - Database: 데이터를 저장하고 관리하는 컨테이너.
   - Table: 데이터베이스 내에 구조화된 데이터를 저장하는 장소.
   - Column: 테이블의 열.
   - Field: 레코드의 각 컬럼에 저장된 개별 데이터 값.
   - Row: 테이블의 행.
   - Record: 데이터의 행.
   - Primary Key: 테이블의 각 레코드를 고유하게 식별하는 컬럼의 값.
   - Foreign Key: 다른 테이블의 레코드를 참조하는 컬럼의 값.
   - Index: 데이터 검색 속도를 높이기 위해 사용되는 자료구조.
   - Schema: 데이터베이스의 구조와 제약 조건을 정의한 것.
   - Normalization (정규화): 데이터베이스 설계 최적화 과정.
   - Denormalization (비정규화): 성능 향상을 위한 중복 데이터 생성 과정.

1. **데이터 조작 및 관리**
   - Query: 데이터베이스에 정보를 요청하는 명령어 혹은 문장.
   - Join: 두 개 이상의 테이블에서 관련된 컬럼을 기반으로 데이터 결합.
   - View: 실제 데이터를 포함하지 않는 가상의 테이블.
   - Transaction: 하나의 논리적 작업 단위.
   - Procedure: 하나 이상의 SQL문을 포함하는 PL/SQL 블록.
   - Data Integrity (데이터 무결성): 데이터의 정확성과 안정성 유지.
   - Constraint (제약 조건): 데이터베이스 내 데이터에 적용되는 규칙이나 제한.
   - Stored Procedure (저장 프로시저): 데이터베이스에 저장된 SQL 코드 집합.
   - Trigger (트리거): 특정 조건/이벤트 발생 시 자동 실행되는 SQL 코드.
   - ACID Properties (ACID 속성): 트랜잭션의 원자성, 일관성, 고립성, 지속성.
   - Subquery (서브쿼리): 다른 쿼리 내에서 실행되는 쿼리.
   - Alias (별칭): 테이블이나 컬럼에 임시 이름 부여.
   - Aggregate Function (집계 함수): 여러 행 값을 요약하는 함수.

2. **SQL 언어와 데이터 처리**
   - SQL: 데이터베이스와 상호작용을 위한 언어.
   - DML (Data Manipulation Language): 데이터 조작에 사용되는 SQL 부분.
   - DDL (Data Definition Language): 데이터 구조 정의에 사용되는 SQL 부분.
   - DCL (Data Control Language): 데이터베이스 접근/권한 관리에 사용되는 SQL 부분.
   - TCL (Transaction Control Language): 트랜잭션 관리에 사용되는 SQL 부분.

3. **데이터 처리 시스템과 기술**
   - Data Warehouse (데이터 웨어하우스): 데이터 통합, 저장 및 분석 시스템.
   - OLTP (Online Transaction Processing): 실시간 트랜잭션 처리 시스템.
   - OLAP (Online Analytical Processing): 복잡한 쿼리 및 분석을 위한 데이터 처리 방식.