### `Override`와 `Overload`에 대한 설명

#### Override (오버라이딩)

- **정의**: 상위 클래스에서 정의한 메소드를 하위 클래스에서 재정의하는 것
- **사용 이유**: 하위 클래스에서 상위 클래스의 메소드를 그대로 사용하지 않고 새로운 기능을 구현하거나 수정할 때 사용
- **주의사항**: 메소드 시그니처가 동일해야 하며, 리턴 타입도 동일하거나 하위 타입이어야 함
- **키워드**: Java에서는 `@Override` 어노테이션을 사용하여 명시적으로 오버라이딩을 표시한다.

##### 예시 코드
```java
// 상위 클래스 Animal
public class Animal {
    public void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

// 하위 클래스 Dog
public class Dog extends Animal { // Animal class 상속
    @Override
    public void makeSound() {
        System.out.println("Dog barks");
    }
}
```

#### Overload (오버로딩)

- **정의**: 같은 이름의 메소드를 여러 개 정의하는 것을 의미합니다. 매개변수의 타입이나 개수가 달라야 한다
- **사용 이유**: 같은 기능을 하는 메소드가 다양한 매개변수를 받을 수 있도록 설계할 때 사용한다
- **주의사항**: 리턴 타입이나 접근 지정자가 다르다고 해서 오버로딩이 되는 것은 아니다
  
##### 예시 코드
```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }
}
```

#### 차이점
- **Override**: 상위 클래스의 메소드를 하위 클래스에서 재정의한다. 메소드 시그니처는 동일해야 한다.
- **Overload**: 같은 이름의 메소드를 여러 개 정의한다. 매개변수의 타입이나 개수가 달라야 한다.

두 개념은 코드의 재사용성과 유지 보수성을 높이는 중요한 역할을 한다. `Override`는 주로 다형성을 구현할 때 사용되며, `Overload`는 유연한 메소드 설계를 가능하게 한다.