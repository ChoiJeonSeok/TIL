### TIL: Java의 Interface에 대한 이해

#### 정의
- 인터페이스는 Java에서 메서드의 선언만을 포함하는 구조다. 구현은 없고, 메서드의 "시그니처"만 정의된다.
- 시그니처란, 메서드의 이름, 입력 매개변수, 반환 타입 등을 의미한다.

#### 목적
1. **유지 보수성**: 인터페이스를 통해 구현을 추상화함으로써, 구현이 변경되어도 인터페이스를 사용하는 코드는 변경할 필요가 없게 된다.
   
2. **확장성**: 인터페이스를 사용하면 새로운 기능을 추가하거나 기존 기능을 수정할 때도 기존 코드에 최소한의 변경만으로 가능하다.

3. **다형성**: 인터페이스를 구현한 다양한 클래스의 객체를 동일한 타입, 즉 인터페이스 타입으로 다룰 수 있다.

4. **낮은 결합도**: 인터페이스를 사용하면 클래스 간의 결합도가 낮아져서, 하나의 클래스 변경이 다른 클래스에 미치는 영향을 줄일 수 있다.

#### 사용 예시
```java
public interface Database {
    void save();
    void update();
}

public class MySQLDatabase implements Database {
    public void save() {
        // MySQL에 저장하는 로직
    }
    public void update() {
        // MySQL을 업데이트하는 로직
    }
}

public class MongoDBDatabase implements Database {
    public void save() {
        // MongoDB에 저장하는 로직
    }
    public void update() {
        // MongoDB를 업데이트하는 로직
    }
}

public class App {
    private Database database;

    public App(Database database) {
        this.database = database;
    }

    public void saveData() {
        database.save();
    }
}

App app1 = new App(new MySQLDatabase());
app1.saveData();  // MySQL에 저장

App app2 = new App(new MongoDBDatabase());
app2.saveData();  // MongoDB에 저장
```
- `Database` 인터페이스에는 `save`와 `update` 메서드가 선언되어 있다.
- `MySQLDatabase`나 `MongoDBDatabase`와 같은 구현체에서는 이 `save`와 `update` 메서드를 구현한다.
- `App` 클래스에서는 `Database` 인터페이스를 통해 구현체를 사용하므로, 어떤 데이터베이스를 사용하든 동일한 메서드를 호출할 수 있다.

#### 인터페이스와 `implements`
- `implements` 키워드는 클래스가 특정 인터페이스를 구현하겠다고 선언할 때 사용된다.
- 해당 클래스는 인터페이스에 정의된 모든 메서드를 구현해야 한다.

#### 주의점
- 인터페이스를 구현할 때는 인터페이스에 정의된 모든 메서드를 구현해야 한다는 점을 명심해야 한다.
- interface는 일종의 `약속`이나 `계약`이라고 볼 수 있다. 이 `약속`을 통해 어떤 클래스가 어떤 메서드를 반드시 구현해야 하는지 명시적으로 나타내는 것이다. 
- 개발자가 사용 또는 구현을 할 때 미리 알 수 있는 `틀`을 제공하며, 이 `틀`을 따르는 여러 구현체를 자유롭게 교체하거나 확장할 수 있다.
- 예를 들어, `Database` interface를 알고 있다면, `MySQLDatabase`나 `MongoDBDatabase` 등의 구현체가 어떤 메서드를 가지고 있는지 미리 알 수 있다. 따라서 `틀`을 알고 있다면 해당 `틀`을 이용한 메서드는 어떤 기능을 기대할 수 있는지 명확하게 알 수 있다.
- interface에 정의된 모든 메서드를 구현한 뒤, 추가적인 메서드를 더 구현할 수 있다. 대신, interface 타입 참조 변수를 사용하게 되면, 해당 interface에 정의된 메서드만 호출할 수 있다. 
  - 확장된 기능을 사용하고 싶다면 확장한 해당 클래스 타입으로 캐스팅해야 한다.
  - 또는 처음부터 클래스 타입의 참조 변수를 사용하면 된다.
    ```java
    Database db = new MySQLDatabase();
    db.save();  // 가능
    db.update();  // 가능
    db.connect();  // 컴파일 에러

    ((MySQLDatabase) db).connect();  // 캐스팅 => 가능

    MySQLDatabase db = new MySQLDatabase(); // 처음부터 클래스 타입으로 인스턴스 생성.
    db.save();  // 가능
    db.update();  // 가능
    db.connect();  // 가능
    ```