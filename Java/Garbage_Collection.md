
## 1. 가비지 컬렉션의 개념

가비지 컬렉션은 프로그램이 동적으로 할당한 메모리 중 더 이상 사용되지 않는 부분을 자동으로 회수하는 과정이다. 이로써 개발자는 메모리 관리에 신경 쓸 필요가 없으며, 메모리 누수와 같은 문제를 방지할 수 있다.

## 2. 가비지 컬렉션의 동작 원리

### **Marking 단계**: 
- 이 단계에서는 어떤 객체가 "Garbage"인지를 판단한다. 즉, 더 이상 참조되지 않는 객체를 식별하는 과정이다. 가비지 컬렉터는 루트 객체(root objects)부터 시작하여 참조되는 모든 객체를 추적하고, 이를 통해 도달할 수 없는 객체를 가비지로 표시한다. 
- 루트 객체 탐색 : 루트 객체는 스택, 전역 변수, 레지스터 등에서 직접 참조되는 객체이다. 가비지 컬렉터는 루트 객체부터 시작하여 참조되는 모든 객체를 추적한다.
- 가비지 식별 : 루트 객체에서 도달할 수 없는 객체는 가비지로 판단된다. 이러한 객체는 더이상 프로그램에서 사용되지 않으므로 메모리에서 제거될 수 있다.
### **Sweeping 단계**: 
- 메모리 해제 : Marking 단계에서 식별된 가비지 객체를 메모리에서 제거한다. 이 단계에서 메모리는 해제되며, 해당 영역은 다시 사용될 수 있게 된다.
### **Compaction 단계 (선택적)**: 
- 메모리 조각 정리 : 가비지 컬렉션 후에는 사용되지 않는 메모리 영역이 흩어져 있을 수 있다. 압축 단계에서는 이러한 메모리 조각을 정리하여 연속된 공간을 만든다.

## 3. 세대별 가비지 컬렉션

Java에서는 객체를 새로운(Young) 세대와 오래된(Old) 세대로 분류하여, 세대별로 가비지 컬렉션을 수행한다. 이는 효율성을 높이는 데 도움이 된다. 대부분의 객체는 사용되지 않게 되는 경우가 많으므로 Young 세대에서 먼저 가비지 컬렉션을 수행한다. 

[Young 세대와 Old 세대, Permanent(Metaspace_Java8~) 세대](https://github.com/ChoiJeonSeok/TIL/blob/master/Java/Garbage_Collection_generation.md)

## 4. 다양한 가비지 컬렉션 알고리즘

여러 가지 가비지 컬렉션 알고리즘이 있다.

1. Serial GC: 단일 스레드에서 작동하며, 주로 단일 코어의 CPU에서 사용된다.
2. Parallel GC: 여러 스레드를 사용하여 가비지 컬렉션을 병렬로 수행한다.
3. Concurrent mark-Sweep(CMS) GC: 애플리케이션 스레드와 동시에 작동하여 응답 시간을 줄인다.
4. G1 Garbage Collector: Heap을 여러 영역으로 나누고, 각 영역을 독립적으로 관리한다.

## 5. 가비지 컬렉션 튜닝

JVM 옵션을 사용하여 가비지 컬렉션을 튜닝할 수 있으며, 성능 최적화를 위해 적절한 가비지 컬렉터와 튜닝 옵션을 선택해야 할 수도 있다.
<br><br>예시(Parallel GC 활성화)
```java
# Parallel GC 사용
java -XX:+UseParallelGC -jar application.jar
```

## 6. 가비지 컬렉션의 장단점




### 결론

가비지 컬렉션은 Java의 중요한 부분으로, 메모리 관리의 복잡성을 줄이고 프로그램의 안정성을 높이는 역할을 합니다. 기본 원리부터 다양한 알고리즘, 튜닝 방법에 이르기까지 깊은 이해가 필요하며, 이는 개발 뿐만 아니라 취업 면접에서도 중요한 주제로 다뤄집니다.