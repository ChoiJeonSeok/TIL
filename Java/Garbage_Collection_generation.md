### 1. 세대별 구분

Java의 힙 메모리는 크게 세 부분으로 나뉜다: <br>
Young 세대, Old 세대, 그리고 Permanent 세대 (Java 8 이후에는 Metaspace).

- **Young 세대**: 새로 생성된 객체가 배치되는 영역이다. Young 세대는 다시 Eden 영역과 두 개의 Survivor 영역으로 나뉜다.
- **Old 세대**: Young 세대에서 살아남은 객체가 이동되는 영역.

### 2. Young 세대에서의 가비지 컬렉션

1. **객체 생성**: 새로운 객체는 Eden 영역에 생성된다.
2. **Minor GC**: Eden 영역이 꽉 차면 Minor GC가 발생한다. 살아있는 객체는 Survivor 영역 중 하나로 이동된다.
3. **Survivor 영역 이동**: 객체가 살아남을 때마다 다른 Survivor 영역으로 이동된다.
4. **Old 세대로 이동**: 객체가 일정 횟수 이상 Survivor 영역에서 살아남으면 Old 세대로 프로모션된다.

### 3. Old 세대에서의 가비지 컬렉션

1. **Major GC**: Old 세대가 꽉 차면 Major GC가 발생한다. 이 과정은 통상적으로 Young 세대의 Minor GC보다 더 오래 걸린다.
2. **Full GC**: 전체 힙 영역을 대상으로 하는 가비지 컬렉션. Full GC는 성능에 큰 영향을 미칠 수 있으므로, 가능한 피해야 한다.

### 4. 세대별 구분의 기준

- **나이**: 객체가 Minor GC를 몇 번 살아남았는지에 따라 Old 세대로 프로모션될 수 있다.
- **프로모션 임계값**: 객체의 프로모션 여부를 결정하는 임계값을 설정할 수 있으며, 이 임계값을 넘으면 Old 세대로 이동한다.

### 결론

세대별 가비지 컬렉션은 객체의 생명 주기와 애플리케이션의 동작 특성을 반영하여 메모리 관리를 최적화한다. Young 세대에서 빈번하게 수행되는 가비지 컬렉션과 Old 세대에서 더 드물게 수행되는 가비지 컬렉션의 조합은 전체 시스템의 성능과 효율성을 높이는 데 기여한다.

<details>
    <summary><h2>Java 가비지 컬렉션에서 사용되는 힙 메모리의 영역들</h2></summary>

### 1. Eden 영역

- **역할**: 새로 생성된 객체가 처음으로 할당되는 영역.
- **특성**: Eden 영역이 꽉 차면 Minor GC가 발생하며, 살아남은 객체는 Survivor 영역으로 이동.

### 2. Survivor 영역

- **역할**: Minor GC에서 살아남은 객체가 이동하는 영역.
- **특성**: 두 개의 Survivor 영역이 있으며 (S0, S1), 객체가 살아남을 때마다 두 영역 사이를 이동.

### 3. Old 영역

- **역할**: Young 세대에서 일정 횟수 이상 살아남은 객체가 프로모션되는 영역.
- **특성**: Old 영역이 꽉 차면 Major GC가 발생합니다. 이 영역의 가비지 컬렉션은 일반적으로 Young 세대보다 더 오래 걸린다.

### 4. Permanent 영역 (Java 8 이전) / Metaspace (Java 8 이후)

- **역할**: 클래스 메타데이터, 메서드 데이터, 상수 풀 등이 저장되는 영역.
- **특성**: Java 8 이후에는 Metaspace라는 이름으로 변경되었으며, 네이티브 메모리를 사용.

### 결론

- **Eden 영역**: 새로운 객체가 생성되는 영역
- **Survivor 영역**: Minor GC에서 살아남은 객체가 이동하는 영역
- **Old 영역**: 오랫동안 살아남은 객체가 이동하는 영역
- **Permanent 영역 / Metaspace**: 클래스와 메서드 관련 정보가 저장되는 영역


</details>