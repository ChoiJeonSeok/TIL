
| 접근 제어자 | 같은 클래스 | 같은 패키지 | 하위 클래스 (같은 패키지) | 하위 클래스 (다른 패키지) | 그 외 패키지 |
|--------------|-------------|--------------|---------------------------|---------------------------|--------------|
| public       | 가능        | 가능         | 가능                       | 가능                       | 가능         |
| protected    | 가능        | 가능         | 가능                       | 가능                       | 불가능        |
| default      | 가능        | 가능         | 가능                       | 불가능                      | 불가능        |
| private      | 가능        | 불가능        | 불가능                      | 불가능                      | 불가능        |

- **같은 클래스**: 동일한 클래스 내에서의 접근
- **같은 패키지**: 동일한 패키지 내의 다른 클래스에서의 접근
- **하위 클래스 (같은 패키지)**: 동일한 패키지 내에서 해당 클래스를 상속받은 클래스에서의 접근
- **하위 클래스 (다른 패키지)**: 다른 패키지에서 해당 클래스를 상속받은 클래스에서의 접근
- **그 외 패키지**: 동일한 패키지도, 상속 관계도 아닌 외부 패키지에서의 접근

이 표는 클래스, 변수, 메서드 등에 적용되는 접근 제어자의 작동 방식을 요약한 것. <br>
클래스 설계 시 적절한 접근 제어를 선택함으로써 코드의 안정성과 유지보수성을 높일 수 있다.


```java
public class MyClass {
  private int privateVar; // private 변수
  public int publicVar;  // public 변수

  private void privateMethod() { // private 메서드
    System.out.println("Private Method");
  }

  public void publicMethod() { // public 메서드
    System.out.println("Public Method");
  }

  private class InnerClass { // private 내부 클래스
    public void innerMethod() {
      System.out.println("Inner Class Method");
    }
  }
}

class Test {
  public static void main(String[] args) {
    MyClass obj = new MyClass();

    // obj.privateVar; // 오류! private 변수에 접근 불가능
    obj.publicVar = 10; // public 변수에 접근 가능

    // obj.privateMethod(); // 오류! private 메서드에 접근 불가능
    obj.publicMethod(); // public 메서드에 접근 가능

    // MyClass.InnerClass inner = obj.new InnerClass(); // 오류! private 내부 클래스에 접근 불가능
  }
}

```

<details>
    <summary>각 접근 제어자에 대한 예시</summary>

### 1. public

`public`으로 선언된 변수나 메서드는 어떤 클래스에서든 접근이 가능.

```java
public class PublicClass {
  public int publicVar = 10;
}

class Test {
  public static void main(String[] args) {
    PublicClass obj = new PublicClass();
    System.out.println(obj.publicVar); // 10
  }
}
```

### 2. private

`private`으로 선언된 변수나 메서드는 해당 클래스 내에서만 접근이 가능.

```java
class PrivateClass {
  private int privateVar = 20;

  public int getPrivateVar() {
    return privateVar; // 같은 클래스 내에서 접근 가능
  }
}

class Test {
  public static void main(String[] args) {
    PrivateClass obj = new PrivateClass();
    // System.out.println(obj.privateVar); // 오류! 외부 클래스에서 접근 불가능
    System.out.println(obj.getPrivateVar()); // 20
  }
}
```

### 3. protected

`protected`로 선언된 변수나 메서드는 같은 패키지 내의 클래스나 해당 클래스를 상속받은 외부 패키지의 클래스에서 접근이 가능.

```java
class ProtectedClass {
  protected int protectedVar = 30;
}

class Test extends ProtectedClass {
  public static void main(String[] args) {
    Test obj = new Test();
    System.out.println(obj.protectedVar); // 30
  }
}
```

### 4. default

접근 제어자를 지정하지 않으면, 해당 요소는 같은 패키지 내의 클래스에서만 접근이 가능.

```java
class DefaultClass {
  int defaultVar = 40;
}

class Test {
  public static void main(String[] args) {
    DefaultClass obj = new DefaultClass();
    System.out.println(obj.defaultVar); // 40
  }
}
```

이러한 접근 제어자는 클래스의 특정 부분을 외부로부터 보호하거나 특정 부분만을 외부에 노출하는 데 사용되며, 코드의 안정성과 유지보수성을 높이는 데 중요한 역할을 함.

</details>
