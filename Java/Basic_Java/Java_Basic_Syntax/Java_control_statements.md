# 3. 제어문

## 조건문
조건문은 특정 조건을 만족할 때 코드 블록을 실행.

### if 문
특정 조건이 참일 때 코드 블록을 실행.
```java
if (조건) {
    // 조건이 참일 때 실행할 코드
}
```

### if-else 문
조건이 참이면 하나의 코드 블록을 실행하고, 거짓이면 다른 코드 블록을 실행.
```java
if (조건) {
    // 조건이 참일 때 실행할 코드
} else {
    // 조건이 거짓일 때 실행할 코드
}
```

### if-else if-else 문
여러 조건을 체크하여 각 조건에 따른 다른 코드 블록을 실행.
```java
if (조건1) {
    // 조건1이 참일 때 실행할 코드
} else if (조건2) {
    // 조건2가 참일 때 실행할 코드
} else {
    // 모든 조건이 거짓일 때 실행할 코드
}
```

### switch 문
하나의 변수를 여러 정수형 값(범위 X)과 비교하여 해당 값에 따른 코드 블록을 실행.
```java
switch (변수) {
    case 값1:
        // 변수가 값1일 때 실행할 코드
        break;
    case 값2:
        // 변수가 값2일 때 실행할 코드
        break;
    default:
        // 변수가 어떤 값과도 일치하지 않을 때 실행할 코드
}
```
만약 각 case에 break가 없다면 해당 case부터 그 아래에 있는 코드가 모두 실행됨.<br>
물론 아래 case에 break가 있다면, 그곳에서 switch 코드 실행이 중단되고 다음 코드 블럭으로 넘어감.<br>
이를 `fall-through`라고 하며 특정한 경우에 의도적으로 사용할 수 있음. 

<details>
    <summary>switch fall-through 예시</summary>

```java
int dayOfWeek = 2; // 화요일

switch (dayOfWeek) {
    case 1: // 월요일
    case 2: // 화요일
    case 3: // 수요일
    case 4: // 목요일
    case 5: // 금요일
        System.out.println("오늘은 업무일입니다.");
        break;
    case 6: // 토요일
    case 7: // 일요일
        System.out.println("오늘은 주말입니다.");
        break;
    default:
        System.out.println("유효하지 않은 요일입니다.");
}
// 출력: 오늘은 업무일입니다.
```

`fall-through`는 여러 `case`에 동일한 코드를 적용해야 할 때 코드 중복을 줄이고 가독성을 높이는 데 유용하다.

</details>


## 반복문
반복문은 특정 조건이 만족되는 동안 코드 블록을 반복하여 실행.

### for 문
지정된 횟수만큼 코드 블록을 반복.
```java
for (초기화; 조건; 증감) {
    // 반복할 코드
}
```
<details>
    <summary>for 문 사용 방식</summary>

    Java의 `for` 문은 매우 유연하며 다양한 방식으로 사용할 수 있다. 
    초기화, 조건, 증감 부분 다양한 사용 방법.

### 1. 다중 변수 초기화 및 증감
`for` 문에서는 쉼표를 사용하여 여러 변수를 동시에 초기화하고 증감시킬 수 있다.

```java
for (int i = 0, j = 10; i < 10; i++, j -= 2) {
    System.out.println("i: " + i + ", j: " + j);
}
```

### 2. 다양한 증감 연산
증감 부분에서는 단순한 증가/감소 외에도 다양한 연산을 적용할 수 있다.

```java
for (int i = 1; i < 100; i *= 2) {
    System.out.println(i); // 2의 거듭제곱 출력
}
```

### 3. 조건문 없이 무한 루프
조건 부분을 생략하면 무한 루프를 생성할 수 있다. 이 경우, 반복문 내부에서 `break`를 사용하여 루프를 종료해야 한다.

```java
for (;;) {
    // 무한 루프
    if (조건) break; // 조건을 만족하면 루프 종료
}
```

### 4. 복잡한 조건문 사용
조건 부분에서는 복잡한 논리 연산을 사용하여 정교한 제어를 할 수 있다.

```java
for (int i = 0, j = 10; i < 10 && j > 0; i++, j -= 2) {
    // i가 10 미만이고 j가 0보다 클 때 실행
}
```

### 5. 초기화 및 증감 부분에서의 메서드 호출
초기화 및 증감 부분에서 메서드 호출을 통해 복잡한 로직을 적용할 수 있다.

```java
for (int i = customInit(); checkCondition(i); i = customIncrement(i)) {
    // 사용자 정의 초기화, 조건 검사, 증감 로직 적용
}
```
이때, checkCondition(i) 메서드는 `boolean` 타입의 값을 반환해야 한다.<br>
값이 `true`일 경우 반복문이 계속 실행되고, `false`일 경우 반복문이 중단된다.<br>

예시
```java
public static boolean checkCondition(int i) {
    return i < 10; // i가 10 미만인 경우 true 반환, 그렇지 않으면 false 반환
}
```

### 6. Enhanced for loop (for-each)
Java 5 이상에서는 배열이나 컬렉션을 순회하는 간결한 방법으로 for-each 루프를 사용할 수 있다고 한다.

```java
for (int value : array) {
    System.out.println(value); // 배열의 모든 요소 출력
}
```

- 일반적인 for 루프로 배열을 순회하려면, 인덱스를 직접 관리하며 배열의 각 요소에 접근해야 한다.
```java
int[] array = {10, 20, 30, 40, 50};
for (int i = 0; i < array.length; i++) {
    int value = array[i];
    System.out.println(value);
}
```
- 그런데, for-each 루프를 사용하면 인덱스를 직접 관리하지 않아도 되며, 코드도 간결해진다.

```java
int[] array = {10, 20, 30, 40, 50};
for (int value : array) {
    System.out.println(value);
}
```

#### 동작 원리.
1. `array`의 첫 번째 요소부터 마지막 요소까지 순서대로 `value` 변수에 할당된다.
2. 루프의 본문에서는 `value` 변수를 사용하여 각 요소에 대한 작업을 수행할 수 있다.
3. 모든 요소를 순회하면 루프가 종료된다.

### for-each for 루프 외 사용.
- for-each 루프는 배열뿐만 아니라 ArrayList, HaseSet 등 `Iterable` 인터페이스를 구현하는 컬렉션 클래스에도 사용할 수 있다.
 
### ArrayList 예시
```java
import java.util.ArrayList;

ArrayList<Integer> numbers = new ArrayList<>();
numbers.add(10);
numbers.add(20);
numbers.add(30);

for (int value : numbers) {
    System.out.println(value); // 10, 20, 30 순서대로 출력
}
```

### HashSet 예시
```java
import java.util.HashSet;

HashSet<String> names = new HashSet<>();
names.add("Alice");
names.add("Bob");
names.add("Charlie");

for (String name : names) {
    System.out.println(name); // Alice, Bob, Charlie 출력 (순서는 보장되지 않음)
}
```

</details>


### while 문
조건이 참인 동안 코드 블록을 반복.
```java
while (조건) {
    // 반복할 코드
}
```

### do-while 문
조건이 참인 동안 코드 블록을 반복하며, 최소 한 번은 실행.
```java
do {
    // 반복할 코드
} while (조건);
```

### for-each 문 (enhanced for loop)
배열이나 컬렉션의 모든 요소를 순회.
```java
for (타입 변수명 : 배열/컬렉션) {
    // 반복할 코드
}
```

## 제어문 중첩
하나의 제어문 안에 다른 제어문을 중첩하여 사용할 수 있다.

## break와 continue
- `break`: 현재 반복문을 종료합니다.
- `continue`: 현재 반복을 건너뛰고 다음 반복을 진행.

## 레이블 (label)
레이블을 사용하여 중첩된 반복문에서 특정 반복문을 제어할 수 있다.

```java
outer: for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
        if (조건) {
            break outer; // outer 레이블의 반복문을 종료
        }
    }
}
```