# Java 메서드 체이닝 (Method Chaining)

### 1. 정의
   - 메서드 체이닝은 객체의 메서드를 연속적으로 호출하는 프로그래밍 패턴.
   - 각 메서드가 현재 객체의 참조 (`this`)를 반환하면, 다음 메서드를 바로 호출할 수 있다.
   - 코드의 가독성과 유지보수성을 높이는 데 사용된다.

### 2. 작동 원리
   - 메서드 체이닝을 사용하려면, 체이닝할 메서드가 현재 객체의 참조를 반환해야 한다.
   - `return this;` 구문을 사용하여 현재 객체를 반환하면, 해당 반환값을 이용해 같은 객체의 다른 메서드를 호출할 수 있다.

### 3. 예제 코드
   ```java
   class Car {
     Car start() {
       System.out.println("Starting the car...");
       return this;
     }
     Car accelerate() {
       System.out.println("Accelerating...");
       return this;
     }
   }
   Car myCar = new Car();
   myCar.start().accelerate(); // 메서드 체이닝
   ```

### 4. 사용 케이스
   - **빌더 패턴**: 객체 생성을 단계별로 수행하면서 가독성을 높이는 데 사용된다.
   - **플루언트 인터페이스**: 코드를 자연어에 가깝게 만들어 읽기 쉽게 하는 데 활용된다.
   - **설정 및 구성**: 객체의 여러 속성을 설정하거나 구성하는 작업을 간결하게 만든다.

### 5. 장점
   - 코드의 가독성 향상: 연속적인 메서드 호출로 코드를 더 읽기 쉽게 만든다.
   - 중복 코드 제거: 같은 객체에 대한 연속적인 작업을 줄여 코드의 중복을 줄일 수 있다.
   - 유연한 인터페이스 제공: 메서드 체이닝을 통해 동적인 인터페이스를 제공하면서 사용자에게 다양한 옵션을 제공할 수 있다.

### 6. 주의사항
   - 메서드 체이닝은 남용하지 않도록 주의해야 한다. 과도한 체이닝은 코드의 복잡성을 증가시킬 수 있다.
   - 체이닝을 사용하는 메서드는 불변 객체와 함께 사용되는 경우가 많으므로, 객체의 상태 변화를 주의 깊게 관리해야 한다.
<details><summary>final 키워드, 불변 객체와 메서드 체이닝 예시</summary>

## final 키워드

- `final` 키워드는 변수를 상수화하므로 해당 변수에 값을 한 번만 할당할 수 있다. 클래스의 필드에 `final`을 사용하면 그 필드는 불변이 된다. 즉, 한 번 초기화된 후에는 그 값을 변경할 수 없다.

### 예시:

```java
public class Person {
  final String name; // 불변 필드

  public Person(String name) {
    this.name = name; // 초기화
  }

  // 다른 메서드에서 name 필드를 변경하려고 하면 컴파일 오류가 발생.
}
```

- `final`을 사용한 필드는 생성자에서 초기화되어야 하며, 그 이후에는 값을 변경할 수 없다.

- 그러나 주의할 점은 `final` 키워드가 참조형 변수의 불변성만 보장한다는 것이다. 만약 `final` 필드가 객체를 참조하는 경우, 해당 객체의 내부 상태는 변경될 수 있다. 불변성을 완벽하게 보장하려면 해당 객체도 불변이어야 한다.

### 예시 (참조형 변수):

```java
public class Container {
  private int value;

  public void setValue(int value) {
    this.value = value;
  }

  public int getValue() {
    return value;
  }
}

public class Holder {
  final Container container; // final 필드

  public Holder(Container container) {
    this.container = container;
  }
}

Container container = new Container();
Holder holder = new Holder(container);

container.setValue(1); // Holder의 container 필드가 참조하는 객체의 상태 변경 가능
```

위 예시에서 `Holder` 클래스의 `container` 필드는 `final`이므로 참조 자체는 변경할 수 없지만, 참조하고 있는 `Container` 객체의 내부 상태는 변경할 수 있습니다.

따라서 `final`은 필드의 불변성을 부분적으로만 보장하며, 완전한 불변성을 달성하려면 참조하고 있는 객체도 불변이어야 합니다.

## 불변 객체와 메서드 체이닝

- 메서드 체이닝과 불변 객체를 함께 사용하면, 체인 중간에서 객체의 상태가 변경되지 않음을 보장할 수 있다. 
- 그러나 의도와 다르게 메서드를 잘못 설계하면 불변성을 깨뜨릴 수도 있다.

### 불변성이 깨지지 않은 경우

```java
// 불변 객체를 사용한 메서드 체이닝
public class ImmutablePerson {
  private final String name;
  private final int age;

  // 생성자
  public ImmutablePerson(String name, int age) {
    this.name = name;
    this.age = age;
  }

  public ImmutablePerson setName(String name) {
    return new ImmutablePerson(name, this.age); // 새 객체 반환
  }

  public ImmutablePerson setAge(int age) {
    return new ImmutablePerson(this.name, age); // 새 객체 반환
  }
}

ImmutablePerson person = new ImmutablePerson("John", 30);
person = person.setName("Mike").setAge(25); // 체이닝
```
1. **초기 객체 생성**: `ImmutablePerson person = new ImmutablePerson("John", 30);`를 통해 "John", 30을 가진 `ImmutablePerson` 객체를 생성하고 `person` 변수에 참조를 할당한다.
2. **setName 호출**: `person.setName("Mike")`를 호출하면, 새로운 `ImmutablePerson` 객체가 "Mike", 30을 가진 상태로 생성된다. 이 새 객체는 `setName` 메서드가 반환하는 값이다. 원래 "John", 30을 가진 객체는 변경되지 않고 그대로 남아 있다.
3. **setAge 호출**: `setName` 메서드가 반환한 새로운 객체에 대해 `setAge(25)`를 호출하면, 또 다른 새로운 `ImmutablePerson` 객체가 "Mike", 25를 가진 상태로 생성된다.
4. **참조 갱신**: `person = person.setName("Mike").setAge(25);` 부분에서, `person` 변수의 참조가 마지막으로 생성된 "Mike", 25를 가진 객체로 갱신된다.
5. **기존 객체 참조 해제**: "John", 30을 가진 원래 객체는 이제 `person` 변수에 의해 참조되지 않으므로, 가비지 컬렉션의 대상이 될 수 있다.

- 결과적으로, `person` 변수는 "Mike", 25를 가진 새로운 `ImmutablePerson` 객체를 참조하게 된다. 불변 객체와 메서드 체이닝을 이런 방식으로 사용하면, 객체의 상태를 변경하는 대신 새로운 객체를 생성하게 되므로 원래 객체는 불변성을 유지하게 된다.
- 새로운 객체에 값을 할당하고 싶다면 코드 맨 아래 두 줄을 이렇게 바꾸면 된다. 그러면 person과 person2라는 변수에 의해 각각이 참조받게 된다.

```java
ImmutablePerson person = new ImmutablePerson("John", 30);
ImmutablePerson person2 = person.setName("Mike").setAge(25); // 체이닝
```
</details>

<details><summary>메서드에 의해 불변성이 깨지는 경우</summary>

### 1. 내부 상태를 변경하는 메서드 제공

- 불변 객체는 생성 후에 상태가 변하지 않아야 하지만, 내부 상태를 변경하는 메서드를 제공하면 불변성이 깨진다.

#### 예시:

```java
public class BrokenImmutablePerson {
  private String name; // final이 없음
  private int age;

  public BrokenImmutablePerson(String name, int age) {
    this.name = name;
    this.age = age;
  }

  // 내부 상태를 변경하는 메서드
  public void setName(String name) {
    this.name = name; // 불변성 깨짐
  }
}
```

### 2. 내부 상태를 직접 변경할 수 있는 참조 노출

- 불변 객체가 참조 타입의 필드를 가지고 있을 때, 그 참조를 외부로 노출하면 불변성이 깨질 수 있다.

#### 예시:

```java
import java.util.Date;

public class BrokenImmutableCalendar {
  private final Date date;

  public BrokenImmutableCalendar(Date date) {
    this.date = date;
  }

  // 내부 참조를 직접 반환
  public Date getDate() {
    return date; // 불변성 깨짐
  }
}

Date date = new Date();
BrokenImmutableCalendar calendar = new BrokenImmutableCalendar(date);
date.setTime(0); // calendar 객체의 내부 상태 변경 가능
```
#### 불변성을 유지하려면?
- 불변 클래스가 아닌 Date 객체의 참조를 외부에 노출하고 있어 클래스 외부에서 date 참조를 통해 내부 상태를 변경할 수 있다.
- 불변성을 유지하려면, 내부 참조를 외부에 노출하지 않도록 주의해야 한다. 내부 Date 객체의 복사본을 반환하면 문제를 해결할 수 있다.

```java
public Date getDate() {
  return (Date) date.clone(); // 복사본 반환
}
```

### 3. 하위 클래스에서 불변성 깨뜨리기

상속을 허용하고, 하위 클래스에서 불변성을 깨뜨릴 수 있는 메서드를 추가하면 문제가 발생할 수 있다.

#### 예시:

```java
public class ImmutableBase {
  private final int value;

  public ImmutableBase(int value) {
    this.value = value;
  }
}

public class MutableSubclass extends ImmutableBase {
  private int anotherValue;

  public MutableSubclass(int value, int anotherValue) {
    super(value);
    this.anotherValue = anotherValue;
  }

  // 내부 상태를 변경하는 메서드
  public void setAnotherValue(int anotherValue) {
    this.anotherValue = anotherValue; // 불변성 깨짐
  }
}
```

이러한 경우들은 불변 객체를 설계하고 구현할 때 주의해야 할 부분들로, 객체의 불변성을 유지하려면 이러한 실수를 피해야 한다.


</details>