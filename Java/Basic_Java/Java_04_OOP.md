# 객체 지향 프로그래밍 OOP(Object-Oriented Programming)

## 객체 지향 프로그래밍 (OOP)의 정의

객체 지향 프로그래밍은 프로그래밍 패러다임 중 하나로, 프로그램을 객체들의 모임으로 보고 이 객체들 간의 상호작용을 통해 동작하도록 설계한다. 객체 지향 설계의 주요 원칙에는 클래스와 객체, 생성자, 상속, 캡슐화, 다형성, 추상화 등이 있다.

## OOP의 특징

### 1. **클래스와 객체** 
- 클래스(Class): 클래스는 객체의 속성과 행동을 정의하는 틀 또는 설계도. 예를 들어 '자동차' 클래스는 색상, 브랜드, 속도 등의 속성과 run, stop 등의 행동을 가질 수 있다.
- 객체(Object): 클래스를 기반으로 실제로 메모리에 할당된 것을 객체라고 한다. 클래스의 인스턴스라고도 한다.

```java
class Car {        // 클래스 정의
  String color;    // 속성
  void run() {     // 행동
    // 달리기 코드
  }
}

Car myCar = new Car(); // 객체 생성
```

### 2. **생성자** 
- 생성자(Constructor): 객체가 생성될 때 자동으로 호출되는 메서드로, 객체의 초기화 작업을 담당한다.

```java
class Car {
  String color;

  Car(String c) { // 생성자
    color = c;
  }
}

Car myCar = new Car("Red"); // "Red" 색상의 Car 객체 생성
```
<details><summary>생성자에 대한 추가 설명</summary>

## 생성자의 특징
- 생성자의 이름은 클래스 이름과 동일해야 한다.
- 생성자는 반환 값이 없으며, 'void' 키워드도 사용하지 않는다.
- 생성자는 객체가 생성될 때 자동으로 호출된다.
- 생성자는 오버로딩이 가능하여, 매개변수의 개수나 타입이 다른 여러 개의 생성자를 정의할 수 있다.

## 생성자의 종류
### 기본 생성자(Default Constructor)
- 매개변수가 없는 생성자
- 클래스에 생성자가 정의되어 있지 않으면 컴파일러가 자동으로 추가한다.

### 매개변수 있는 생성자
- 필요한 매개변수를 받아 객체의 속성을 초기화한다.

### 복사 생성자
- 다른 객체를 복사하여 새 객체를 생성할 때 사용한다.


## 오버로딩
- Overloading은 같은 이름의 메서드나 생성자를 여러 개 정의하는 프로그램밍 기법.
- 오버로딩된 메서드나 생성자는 매개변수의 타입, 개수, 순서가 달라야 한다. 반환 타입은 상관없다.

### 오버로딩의 예시
```java
void print(int a) {
  System.out.println(a);
}

void print(double a) {
  System.out.println(a);
}

void print(String str) {
  System.out.println(str);
}
```
- print 메서드는 오버로딩 되어 있으며, 호출 시 매개변수의 타입에 따라 적절한 메서드가 실행된다.

### 생성자 오버로딩
- 클래스에 여러 생성자를 정의할 수 있다. 이를 생성자 오버로딩이라고 한다.
- 매개변수의 타입과 개수를 다르게 하여 여러 생성자를 정의할 수 있다.

## 생성자 호출 시 주의할 점.
- 생성자의 매개변수와 일치하지 않는 값을 전달하면 컴파일 오류가 발생한다.
- 필요한 매개변수를 모두 전달해야 하며, 그렇지 않을 경우 오류가 발생한다.

### 생성자 오버로딩 호출 예시_1

```java
class Person {
  String name;
  int age;

  Person() { // 기본 생성자
    name = "Unknown";
    age = 0;
  }

  Person(String n, int a) { // 매개변수 있는 생성자
    name = n;
    age = a;
  }

  Person(Person p) { // 복사 생성자
    name = p.name;
    age = p.age;
  }
}

Person person1 = new Person(); // 기본 생성자 호출
Person person2 = new Person("John", 25); // 매개변수 있는 생성자 호출
Person person3 = new Person(person2); // 복사 생성자 호출
```
### 생성자 오버로딩 호출 예시_2

```java
class Book {
  String title;
  String author;
  int pages;

  // 기본 생성자
  Book() {
    title = "Unknown";
    author = "Unknown";
    pages = 0;
  }

  // 제목과 저자만 받는 생성자
  Book(String t, String a) {
    title = t;
    author = a;
    pages = 0;
  }

  // 제목, 저자, 페이지 수를 받는 생성자
  Book(String t, String a, int p) {
    title = t;
    author = a;
    pages = p;
  }
}

Book book1 = new Book(); // 기본 생성자 호출
Book book2 = new Book("Java Programming", "Author Name"); // 제목과 저자만 받는 생성자 호출
Book book3 = new Book("Python Programming", "Author Name", 500); // 모든 정보를 받는 생성자 호출
```

</details>


### 3. **상속** 
- 상속(Inheritance): 기존 클래스의 속성과 메서드를 새로운 클래스에서 재사용할 수 있게 하는 기능.


```java
class Vehicle { // 부모 클래스
  void run() {
    // 달리기 코드
  }
}

class Car extends Vehicle { // 자식 클래스, Vehicle 클래스를 상속
  // 추가 속성 및 메서드
}
```


### 4. **캡슐화** 
- 캡슐화(Encapsulation): 객체의 속성과 행동을 하나로 묶고, 실제 구현 내용을 외부에 감추는 기능.

```java
class Car {
  private String color; // private으로 외부 접근 제한

  public String getColor() { // 외부에서 color에 접근하기 위한 메서드
    return color;
  }
}
```


### 5. **다형성** 
- 다형성(Polymorphism): 동일한 메서드명이나 연산자가 다양한 형태로 동작하는 기능.

```java
class Animal {
  void sound() {
    System.out.println("동물이 소리를 냅니다.");
  }
  
  void eat() {
    System.out.println("동물이 먹이를 먹습니다."); // 공통 기능
  }
}

class Dog extends Animal {
  // 부모 클래스의 sound() 메서드 오버라이딩
  void sound() {
    System.out.println("개가 멍멍 짖습니다.");
  }
}

class Cat extends Animal {
  // 부모 클래스의 sound() 메서드 오버라이딩
  void sound() {
    System.out.println("고양이가 야옹 소리를 냅니다.");
  }
}

Animal myAnimal = new Dog();
myAnimal.sound(); // "개가 멍멍 짖습니다." 출력
myAnimal.eat();   // "동물이 먹이를 먹습니다." 출력

myAnimal = new Cat();
myAnimal.sound(); // "고양이가 야옹 소리를 냅니다." 출력
myAnimal.eat();   // "동물이 먹이를 먹습니다." 출력
```
- 오버라이딩은 상속받은 부모 클래스의 특정 메서드만 자식 클래스에서 재정의하고 싶을 때 사용된다. 나머지 메서드들은 부모 클래스에서 정의된 대로 동작하므로, 중복 코드를 줄이고 유지보수가 용이하다.

### 6. **추상화** 
- 추상화(Abstraction): 필요한 속성과 기능만을 강조하고 불필요한 세부사항은 생략하여 복잡도를 줄이는 기법.

```java
abstract class Vehicle { // 추상 클래스
  abstract void run();   // 추상 메서드
}

class Car extends Vehicle {
  void run() {
    System.out.println("자동차가 달립니다."); // 추상 메서드 구현
  }
}
```

### OOP의 장점

- **재사용성:** 클래스와 상속을 통해 코드 재사용이 쉽다.
- **확장성:** 기존 코드를 변경하지 않고 기능을 확장할 수 있어 유지보수와 확장이 용이하다.
- **유지보수성:** 각 객체가 독립적으로 동작하므로 문제가 발생해도 해당 객체만 수정하면 된다.

### OOP의 단점

- **설계 복잡성:** 올바른 객체 지향 설계는 시간과 노력이 필요하다.
- **성능 이슈:** 객체 간의 메시지 전달, 상속 등은 실행 시간과 메모리를 소모할 수 있다.

### OOP의 적용 예

자바, C++, 파이썬 등 대부분의 현대 프로그래밍 언어는 객체 지향 패러다임을 지원하며, 시스템 설계, 웹 개발, 모바일 앱 개발 등 다양한 분야에서 활용된다.

