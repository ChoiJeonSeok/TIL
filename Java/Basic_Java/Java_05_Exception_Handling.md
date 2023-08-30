# 예외 처리 (Exception Handling) in Java

- 예외 처리는 프로그램의 안정성을 높이고 유지보수를 쉽게 하는 중요한 프로그래밍 기술. 
- Java에서는 `try`, `catch`, `finally`, `throw`, `throws` 등의 키워드를 사용하여 예외를 처리한다.

## 목차
1. **try-catch 문**
    1. 기본 구조
    2. 다중 catch 블록
    3. finally 블록
    4. 중첩 try-catch
    5. 예제

2. **사용자 정의 예외 (Custom Exceptions)**
    1. 사용자 정의 예외 만들기
    2. 사용자 정의 예외 사용하기
    3. 예제

3. **Java 표준 라이브러리의 예외 클래스**
    1. `java.lang.Exception` 클래스
    2. `java.lang.RuntimeException` 클래스
    3. 주요 예외 클래스들
    4. 예제

---

## 1. try-catch 문

### 1.1 기본 구조
- `try-catch` 블록은 예외가 발생할 가능성이 있는 코드를 `try` 블록 안에 넣고, 예외가 발생했을 때 처리할 코드를 `catch` 블록 안에 넣는다.

```java
// try-catch 기본 구조
try {
    // 예외가 발생할 가능성이 있는 코드
} catch (ExceptionType e) {
    // 예외가 발생했을 때 실행할 코드
}
```

### 1.2 다중 catch 블록
- 하나의 `try` 블록에 대해 여러 개의 `catch` 블록을 사용할 수 있다. 
- 다양한 예외 유형에 대해 다른 처리를 하려면 이 기능을 사용한다.

```java
// 다중 catch 블록
try {
    // 예외가 발생할 수 있는 코드
} catch (FileNotFoundException e) {
    // FileNotFoundException 처리
} catch (IOException e) {
    // IOException 처리
} catch (Exception e) {
    // 모든 예외 처리
}
```

### 1.3 finally 블록
- `finally` 블록은 예외 발생 여부와 관계없이 항상 실행되는 코드 블록이다.

```java
try {
    // 예외 발생 가능성이 있는 코드
} catch (Exception e) {
    // 예외 처리
} finally {
    // 항상 실행되는 코드
}
```

### 1.4 중첩 try-catch
- `try-catch` 블록은 중첩해서 사용할 수 있다.

```java
try {
    try {
        // 내부 try 블록
    } catch (Exception e) {
        // 내부 catch 블록
    }
} catch (Exception e) {
    // 외부 catch 블록
}
```

### 1.5 예제

```java
public class TryCatchExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;  // ArithmeticException 발생
        } catch (ArithmeticException e) {
            System.out.println("0으로 나눌 수 없습니다: " + e);
        } finally {
            System.out.println("항상 실행되는 부분");
        }
    }
}
```

## 2. 사용자 정의 예외 (Custom Exceptions)

### 2.1 사용자 정의 예외 만들기
- Java에서는 사용자가 직접 예외 클래스를 만들 수 있다. 
- 사용자 정의 예외 클래스는 `Exception` 클래스를 상속받아야 한다. 그 후 생성자를 통해 예외 메시지를 설정한다.

```java
// 사용자 정의 예외 클래스
public class MyException extends Exception {
    public MyException(String message) {
        super(message);
    }
}

// 메인 클래스와 메서드
public class CustomExceptionExample {
    public static void main(String[] args) {
        try {
            validateAge(15);  // 나이가 18세 미만이므로 MyException 발생
        } catch (MyException e) { // runtime에 자동으로 e 변수에 extends Exception한 클래스로부터 인스턴스 할당. 예외가 발생하면 그 시점에서 해당 예외 객체가 생성된다.(Java의 동적 예외 처리)
            System.out.println("예외 발생: " + e.getMessage());  // '나이가 미성년입니다.' 출력
        }
    }

    public static void validateAge(int age) throws MyException {
        if (age < 18) {
            throw new MyException("나이가 미성년입니다.");  // 여기에서 message를 "나이가 미성년입니다."로 설정
        }
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            doSomethingRisky();  // 이 메서드 내에서 MyException이 발생할 수 있음
        } catch (MyException e) {
            System.out.println("Caught an exception: " + e.getMessage());
            // 여기에서 추가 처리를 할 수 있음. 예를 들어, 로그를 남기거나, 사용자에게 메시지를 표시 등
        }
    }

    public static void doSomethingRisky() throws MyException {
        // ... 어떤 로직 ...
        if (/* 어떤 조건 */) {
            throw new MyException("Something went wrong");
        }
        // ... 어떤 로직 ...
    }
}
```

### 2.2 사용자 정의 예외 사용하기
- 사용자 정의 예외를 발생시키려면 `throw` 키워드를 사용한다.

```java
public class MyException extends Exception {
    public MyException(String message) {
        super(message);
    }
}

public class CustomExceptionExample {
    public static void main(String[] args) {
        try {
            raiseCustomException();  // 사용자 정의 예외 발생
        } catch (MyException e) {
            System.out.println("Caught an exception: " + e.getMessage());
        }
    }

    public static void raiseCustomException() throws MyException { // 사용자 정의 예외 발생 시
        throw new MyException("This is a custom exception");
    }
} // e.getMessage() 를 통해 "This is a custom exception"이라는 메시지가 출력될 것임.
```

## 3. Java 표준 라이브러리의 예외 클래스

### 3.1 `java.lang.Exception` 클래스
- `java.lang.Exception` 클래스는 Java에서 모든 검사 예외(checked exceptions)의 부모 클래스.
- 검사 예외란 컴파일러가 명시적으로 처리를 요구하는 예외. 
- 이 클래스를 상속받아 사용자 정의 예외를 만들 수 있다.

#### 주요 메서드
- `getMessage()`: 예외에 대한 상세 메시지를 반환한다.
- `printStackTrace()`: 예외 발생 당시의 스택 트레이스를 출력한다.

### 3.2 `java.lang.RuntimeException` 클래스
- `RuntimeException` 클래스는 모든 비검사 예외(unchecked exceptions)의 부모 클래스.
- 비검사 예외는 명시적인 예외 처리를 강제하지 않는다.
- 이 클래스를 상속받아 사용자 정의 런타임 예외를 만들 수 있다.

#### 주요 메서드
- `getMessage()`, `printStackTrace()` 등 `Exception` 클래스와 동일한 메서드를 가진다.

### 3.3 주요 예외 클래스들
- `NullPointerException`: 객체 참조가 `null`인 상태에서 객체의 메서드를 호출할 때 발생한다.
- `IndexOutOfBoundsException`: 배열이나 리스트에서 유효하지 않은 인덱스를 사용할 때 발생한다.
- `NumberFormatException`: 숫자 형식이 아닌 문자열을 숫자로 변환하려고 할 때 발생한다.
- `ArithmeticException`: 수학적으로 불가능한 연산을 수행할 때 발생한다.

### 3.4 예제
- `NullPointerException`을 처리하는 방법. 
- `String str = null`에서 `str`은 `null`이므로 `str.length()`는 `NullPointerException`을 발생시킨다.


```java
public class StandardExceptionExample {
    public static void main(String[] args) {
        String str = null;
        try {
            System.out.println(str.length());  // NullPointerException 발생
        } catch (NullPointerException e) {
            System.out.println("Null 값을 참조하고 있습니다: " + e.getMessage());
        }
    }
}
```
- `catch` 블록이 `NullPointerException`을 잡아 "Nuill 값을 참조하고 있습니다: null"이라는 메시지를 출력한다.
- `e.getMessage()`는 `null`을 반환하는데, 이는 `NullPointerException`이 생성자에 메시지를 전달받지 않았기 때문이다. 