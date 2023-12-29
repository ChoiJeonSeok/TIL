# 2. 데이터 스토리지 및 관리

## 2.1 Amazon S3: 확장 가능한 객체 스토리지
- **개요**: Amazon Simple Storage Service (S3)는 확장 가능한 객체 스토리지 서비스로, 데이터 백업, 아카이빙, 빅데이터 분석 등 다양한 용도로 사용된다.
- **특징**: 높은 내구성, 보안, 간편한 데이터 액세스, 웹에서 직접 액세스할 수 있는 저장소 제공.
- **사용 사례**: 웹사이트의 정적 파일 호스팅, 데이터 레이크 구축, 백업 및 재해 복구 솔루션.
- **URL 구조**: `[버킷 이름].s3.[region].amazonaws.com` (객체 이름이 뒤에 붙을 수 있다.)

<details>
<summary>Amazon S3의 사용사례</summary>
1. 정적 웹사이트 호스팅: 웹 서버 없이 웹사이트를 구축하고 운영할 수 있게 해줌.
2. 데이터 레이크 구축: 다양한 형식의 데이터를 저장할 수 있음.
3. 백업 및 재해 복구
4. 미디어 파일 저장 및 전송
5. 데이터 아키이빙: S3 Glacier를 통한 데이터 장기 보존
6. 모바일 및 웹 애플리케이션 데이터 스토리지: 사용자 데이터, 설정, 상태 정보 등 저장
7. 분산 애플리케이션의 데이터 공유 및 동기화
</details>

### 객체 스토리지 서비스
-  데이터를 객체로 관리하는 서비스. `객체`란 데이터와 그 데이터에 대한 메타데이터, 그리고 데이터를 구별하는 고유 식별자를 포함한다. 데이터를 더 유연하게 관리할 수 있으며, 대규모 데이터를 효율적으로 처리하는 데 적합하다. 각 객체는 HTTP 기반 API를 통해 접근할 수 있다.

- **객체 구성 요소**: 객체는 세 가지 주요 구성 요소로 이루어져 있다: 
    <br>(1) 데이터 자체
    <br>(2) 데이터에 대한 추가 정보나 설명을 포함하는 메타데이터
    <br>(3) 데이터에 접근하기 위한 고유 식별자 또는 키.

- **플랫 네임스페이스**: 이는 계층적인 폴더 구조가 없는 저장소 구조를 의미한다. 모든 데이터 객체는 단일 수준의 저장소 공간에 위치하며, 각 객체는 고유한 식별자나 이름을 통해 직접 접근된다. 이러한 구조는 대규모 데이터를 보다 효율적으로 관리하고, 검색 속도를 향상시키는 데 도움이 된다.

## 2.2 Amazon RDS: 관계형 데이터베이스 서비스

### 개요
- Amazon Relational Database Service (RDS)는 관리가 용이한 관계형 데이터베이스 서비스로, 다양한 데이터베이스 엔진을 지원한다. 
- MySQL, PostgreSQL, Oracle 등이 포함된다.

### Amazon RDS의 주요 특징
#### 1. **스케일링**
   - **수직적 스케일링**: 데이터베이스의 컴퓨팅 리소스(예: CPU, RAM)을 필요에 따라 증감시켜 성능을 조절한다.
   - **수평적 스케일링**: 읽기 부하를 분산하기 위해 읽기 전용 복제본을 추가할 수 있다.

#### 2. **백업**
   - **자동 백업**: 정해진 일정에 따라 데이터베이스를 자동으로 백업한다.
   - **스냅샷 백업**: 데이터베이스의 현재 상태를 스냅샷으로 캡처하여, 필요시 복원할 수 있다.

#### 3. **패치 관리 자동화**
   - 데이터베이스 소프트웨어의 보안 패치 및 업데이트를 자동으로 관리한다.

#### 4. **고가용성**
   - **다중 AZ 배포**: 여러 가용 영역에 데이터베이스 인스턴스를 분산 배치하여, 한 영역에서 장애가 발생해도 서비스가 계속 운영된다.
   - **자동 장애 감지 및 복구**: 장애 발생 시 자동으로 트래픽을 안정적인 영역으로 전환한다.

#### 5. **재해 복구**
   - 백업과 다중 AZ 배포를 통해 데이터 보호 및 빠른 복구를 지원하여 비즈니스 연속성을 보장한다.

### 사용 사례
- **웹 애플리케이션**: 안정적이고 확장 가능한 데이터베이스 환경을 제공한다.
- **ERP 시스템 (Enterprise Resource Planning)**: 여러 부서의 데이터와 프로세스를 통합하여 효율성과 의사결정을 개선한다.
- **CRM 시스템 (Customer Relationship Management)**: 고객 관련 데이터를 중앙화하여 관리 및 분석한다.


## 2.3 Amazon DynamoDB: NoSQL 데이터베이스 서비스
- **개요**: DynamoDB는 빠른 성능을 제공하는 완전 관리형 NoSQL 데이터베이스 서비스이다.
- **특징**: 단일 자릿수 밀리초의 응답 시간, 자동 스케일링, 보안 및 내구성.
- **사용 사례**: IoT, 모바일 애플리케이션, 실시간 분석, 게임 개발 등.

## 2.4 Amazon Redshift: 데이터 웨어하우스 서비스
- **개요**: Amazon Redshift는 대량의 데이터를 분석하고 보고하는 데 최적화된 데이터 웨어하우스 서비스이다.
- **특징**: 페타바이트 규모의 데이터 처리, 고성능 쿼리 실행, 데이터 암호화, SQL 기반.
- **사용 사례**: 비즈니스 인텔리전스, 대규모 데이터 분석, 보고서 생성.

## 2.5 데이터 레이크 및 S3 활용
- **개요**: 데이터 레이크는 다양한 형식의 대규모 데이터를 저장하고 분석하기 위한 시스템입니다. AWS에서는 S3를 중심으로 데이터 레이크를 구축한다.
- **특징**: 다양한 데이터 소스 통합, 대규모 데이터 저장 및 분석, 유연한 데이터 접근.
- **사용 사례**: 빅데이터 분석, 기계 학습, 실시간 분석, 다양한 데이터 소스의 통합.

### 데이터 레이크
- 구조화된 데이터 및 텍스트, 이미지, 로그 파일 등의 비구조화된 데이터도 저장할 수 있는 시스템이다.
- 원시 형태의 데이터를 그대로 저장하며 필요에 따라 데이터를 변환하고 처리할 수 있다.

