# 라우팅

## 라우팅이란?
- 라우팅은 패킷이 출발지에서 목적지로 전달되는 경로를 결정하는 과정이다. 
- 라우터가 패킷의 목적지를 기반으로 최적의 경로를 선택하여 패킷을 전달한다.

### 라우팅 프로토콜

- 라우팅 프로토콜은 네트워크 간에 라우팅 정보를 교환하고 최적의 경로를 결정하기 위해 사용된다. 
- 주요 라우팅 프로토콜로는 RIP(Routing Information Protocol), OSPF(Open Shortest Path First), BGP(Border Gateway Protocol) 등이 있다.

### 라우팅 테이블

- 라우팅 테이블은 라우터가 가지고 있는 목적지 네트워크와 해당 네트워크로의 경로 정보를 포함하는 데이터베이스이다.
- 라우팅 테이블을 기반으로 라우터는 패킷을 적절한 경로로 전달한다.

### 내부 라우팅과 외부 라우팅

- 내부 라우팅: 동일한 자체 네트워크 내에서 라우팅을 수행하는 것.
  - 라우터는 내부 네트워크에 대한 경로를 파악하여 패킷을 전달한다.

- 외부 라우팅: 다른 네트워크 간에 라우팅을 수행하는 것.
  - 외부 라우팅은 대개 게이트웨이(Gateway) 또는 외부 라우터를 통해 이룬다.

### 정적 라우팅

- 정적 라우팅은 수동으로 라우팅 테이블을 구성하는 방식.
- 네트워크 관리자가 수동으로 경로를 설정하여 패킷을 전달한다.

### 동적 라우팅

- 적 라우팅은 라우터들이 라우팅 정보를 자동으로 교환하여 최적의 경로를 결정하는 방식. 
- 라우팅 프로토콜을 사용하여 라우팅 테이블을 동적으로 업데이트한다.