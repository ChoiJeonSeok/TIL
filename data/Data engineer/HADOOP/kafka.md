# Apache Kafka


|             | Apache Kafka                                                        |
|-------------|---------------------------------------------------------------------|
| 장점        | - 대규모 데이터 처리에 적합한 분산 메시징 시스템이다.                 |
|             | - 고가용성과 확장성을 제공하여 대량의 데이터를 처리할 수 있다.       |
|             | - 데이터 손실 없이 안정적인 메시지 전달을 보장한다.                   |
|             | - 실시간 데이터 스트리밍을 지원하여 실시간 처리가 가능하다.           |
|             | - 다양한 생태계와의 통합을 제공하여 다른 분산 처리 프레임워크와 연동이 용이하다. |
| 단점        | - 초기 설정과 관련된 어려움이 있을 수 있다.                       |
|             | - 데이터 분산 처리에 따른 복잡성이 존재할 수 있다.                  |

### Apache Kafka 개요

- Kafka는 실시간 데이터 피드를 처리하기 위해 설계된 분산 스트리밍 플랫폼으로, 특히 대용량의 데이터 스트리밍 처리에 적합하다. Kafka는 고속으로 데이터를 수집하고, 저장하며, 처리하는 데 사용된다.

### Kafka의 핵심 구성 요소

1. **프로듀서(Producer)**: 데이터를 생성하고 Kafka 시스템으로 보내는 역할을 한다. 예를 들어, 서버 로그 데이터, 이벤트 데이터 등을 Kafka 클러스터로 전송한다.

2. **컨슈머(Consumer)**: Kafka로부터 데이터를 읽어와서 처리하는 역할을 한다. 여러 컨슈머가 동시에 데이터를 읽을 수 있다.

3. **브로커(Broker)**: Kafka 클러스터의 기본 구성 요소로, 실제로 데이터를 저장하고 처리하는 서버들이다. 여러 브로커가 함께 클러스터를 형성한다.

4. **토픽(Topic)**: 데이터의 카테고리나 피드를 의미한다. 프로듀서는 특정 토픽에 데이터를 보내고, 컨슈머는 특정 토픽의 데이터를 구독한다.

5. **파티션(Partition)**: 토픽은 여러 파티션으로 나누어져 있어, 대규모 데이터를 효율적으로 처리할 수 있다.

### Kafka의 주요 특징

1. **분산 처리**: Kafka는 분산 아키텍처를 사용하여 고가용성과 확장성을 제공한다. 이는 대량의 데이터를 효율적으로 처리할 수 있게 해준다.

2. **고신뢰성**: Kafka는 데이터를 여러 브로커에 복제하여, 서버 장애 시에도 데이터 손실을 방지한다.

3. **실시간 처리**: Kafka는 낮은 지연 시간으로 데이터를 실시간으로 처리할 수 있어, 실시간 분석이나 모니터링에 유용하다.

4. **다양한 통합 지원**: Kafka는 Hadoop, Spark와 같은 다른 데이터 처리 시스템과 쉽게 통합할 수 있다.

### Kafka 사용 사례

1. **로그 수집**: 시스템 로그, 사용자 행동 로그 등을 실시간으로 수집하여 분석한다.

2. **실시간 모니터링**: 시스템의 성능 지표나 사용자 활동을 실시간으로 모니터링한다.

3. **스트림 처리**: 실시간으로 들어오는 데이터 스트림을 처리하여, 실시간 분석이나 대시보드에 사용한다.

4. **이벤트 소싱**: 사용자의 행동이나 시스템의 상태 변경을 이벤트로 기록하고, 이를 통해 시스템의 상태를 재구성하는 데 사용한다.

### Kafka의 한계 및 고려사항

- **초기 설정 복잡성**: Kafka는 많은 설정 옵션을 제공하며, 초기 설정이 복잡할 수 있다. 적절한 환경 설정이 중요하다.
- **운영 관리**: 대규모 클러스터 관리는 운영상의 복잡성을 증가시킨다.
- **데이터 모델링 요구**: 효율적인 사용을 위해서는 데이터를 적절하게 모델링하고 파티셔닝 전략을 고려해야 한다.
- **보안 설정**: 데이터 보안과 관련된 설정이 중요하다.

