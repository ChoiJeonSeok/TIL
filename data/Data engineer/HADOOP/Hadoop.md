# Hadoop

## 개요
Hadoop은 대규모 데이터 세트를 처리하고 분석하기 위한 오픈 소스 프레임워크이다. 주로 분산 컴퓨팅 환경에서 작동하며, 데이터를 여러 노드로 분산하여 처리하고 저장한다. Hadoop은 기존의 데이터 처리 방식과는 다르게 데이터를 작은 조각으로 나누어 여러 노드에서 병렬로 처리함으로써 성능과 확장성을 향상시킨다.

<br>

## 분산 컴퓨팅 환경
- 분산 컴퓨팅 환경은 여러 컴퓨터 또는 노드들이 네트워크로 연결되어 작업을 분산하여 처리하는 환경을 의미한다.

## 데이터 분산 처리 방법
- Hadoop은 데이터를 작은 조각으로 나누어 여러 노드에 분산하여 처리한다.
- 데이터를 나누는 과정은 두 가지로 나뉩니다: 분할(Divide)과 배분(Distribute).
- 분할(Divide): 대용량 데이터를 작은 블록으로 분할한다.
- 배분(Distribute): 분할된 데이터 블록을 여러 노드로 분산하여 저장한다.

## Hadoop의 핵심 구성 요소
 - HDFS
 - MapReduce

### HDFS (Hadoop Distributed File System)
- HDFS는 대규모 데이터 세트를 저장하기 위한 분산 파일 시스템이다.
- 데이터는 여러 개의 블록으로 나누어 각 노드에 나누어 저장되며, 이를 통해 데이터를 분산하여 처리할 수 있다.
- 장애 허용성과 데이터 복구 기능을 제공한다.
- Hadoop은 데이터를 작은 조각으로 나누어 여러 노드에서 병렬로 처리한다는 것은, Hadoop이 데이터를 여러 개의 작은 블록으로 나누어 각 노드에서 동시에 처리함으로써 성능과 확장성을 향상시키는 것을 의미한다.

### MapReduce
- MapReduce는 분산 데이터 처리 모델로, 데이터를 작은 작업 단위로 분할하고, 각 노드에서 병렬로 처리한 후 결과를 조합하여 최종 결과를 생성한다.
- Map 단계에서는 데이터를 분할하여 키-값 쌍으로 변환한다. 각 쌍은 병렬로 처리되며, 여러 개의 중간 결과가 생성된다.
- Reduce 단계에서는 중간 결과를 조합하여 최종 결과를 생성한다. 각 Reduce 작업은 특정 키에 대해 실행되며, 결과는 병렬로 처리된다.
- 예를 들어, Word Count 작업에서는 Map 단계에서 문서를 단어로 분할하고, 각 단어를 (단어, 1)과 같은 키-값 쌍으로 변환한다. Reduce 단계에서는 같은 단어를 가진 키-값 쌍을 합산하여 단어의 빈도를 계산한다.



<br>

## Hadoop의 장점과 단점

| 장점                            | 단점                                          |
|---------------------------------|-----------------------------------------------|
| 대용량 데이터 처리              | 설정 및 관리가 복잡할 수 있음                 |
| 다양한 도구와 프레임워크 지원 | 각 노드별 일정 수준 이상의 하드웨어를 요구함    |
| 확장성                          | 하드웨어 요구 사항이 높음                      |
| 비용 효율적인 스토리지 및 처리 | 작은 규모의 데이터 처리에는 비효율적일 수 있음 |
| 대규모 시스템에 적합            |                                               |

<br>

# 사용

### 배운내용
- hadoop HDFS 데몬을 작동할 때, 자기 자신인 ubuntu@master 계정에도 ssh로 접근을 시도한다.
- 따라서, ssh key를 자기자신(master)에게도 복사하여 인증 상태로 만들어야 한다.

### hadoop 첫 사용
- 2023.06.07 hadoop으로 파일을 공유, 생성, 삭제, 이동을 실습하였다. 
- 독립된 머신 간에 파일을 공유할 수 있는 시스템은 언제 봐도 신기하다. 
- master, worker01, worker02, worker03에 각각 20GB의 용량이 할당되어 있다. 그러면 운영체제나 다른 파일들이 차지할 용량을 생각하지 않고 용량을 계산한다면, 최대 80GB의 용량을 hadoop이 사용할 수 있는 것이다.
- 데이터를 기본 128BM의 블록으로 분할하고 여러 머신에 블록들을 분산 저장한다. 
- 또한, 동시에 replication factor라는 개념을 사용하여 각 블록을 특정 수 만큼(기본:3) 복제하여 특정 수 만큼의 머신에 저장한다.
- 이를 통해 데이터는 안정성과 가용성을 가지게 된다. 데이터가 손실되더라도 다른 복제본이 있어 데이터를 복구할 수 있고, 여러 머신에서 동시에 읽고 쓸 수 있기 때문에 데이터에 대한 동시 액세스 및 처리 성능이 향상된다. 데이터에 대한 요청이 분산되므로 전체 시스템의 처리량이 증가하고 병목 현상이 줄어든다.

## hadoop과 다른 파일 관리 시스템의 공통점과 차이점

|                   | Hadoop           | 다른 파일 관리 시스템 |
|-------------------|-----------------|----------------------|
| 데이터 처리 방식 | 분산 처리      | 단일 노드 처리       |
| 확장성                | 높음               | 제한적                 |
| 내고장성                | 높음               | 제한적                 |
| 처리 속도             | 느림               | 빠름                   |
| 대용량 데이터 처리 | 용이               | 어려움                 |
| 데이터 복제         | 높은 복제 수    | 제한된 복제 수     |
| 유연성                | 낮음               | 높음                   |
| 저장 방식             | 분산 파일 시스템 | 로컬 파일 시스템   |
| 장애 복구             | 가능               | 제한적                 |
| 비용                   | 상대적으로 저렴 | 상대적으로 비쌈   |
