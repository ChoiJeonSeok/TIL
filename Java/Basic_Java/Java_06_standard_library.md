# Java 표준 라이브러리

## 1. 문자열 처리 (String Handling)

### 1.1. 문자열 생성과 초기화
- `String` 클래스: 불변 객체로 문자열을 표현
  - `Integer`, `Double`, `Character` 등의 Wrapper 클래스들도 불변 객체.
- `StringBuilder`, `StringBuffer`: 가변 문자열 처리

#### 예시

```java
String str1 = "Hello"; // 리터럴을 사용한 초기화
String str2 = new String("World"); // 생성자를 사용한 초기화

StringBuilder sb = new StringBuilder("Hello");
sb.append(" World");
```

### 1.2. 문자열 메소드
- `length()`: 문자열 길이
- `charAt(int index)`: 특정 인덱스의 문자 반환
- `substring(int beginIndex, int endIndex)`: 부분 문자열 추출

#### 예시

```java
String str = "Hello World";
int len = str.length(); // 문자열 길이
char ch = str.charAt(0); // 'H'
String sub = str.substring(0, 5); // "Hello"
```

### 1.3. 문자열 비교
- `equals()`: 문자열 내용 비교
- `equalsIgnoreCase()`: 대소문자 무시하고 비교
- `compareTo()`: 사전식 순서로 비교

#### 예시

```java
String str1 = "Hello";
String str2 = "hello";
boolean isEqual = str1.equals(str2); // false
boolean isIgnoreCaseEqual = str1.equalsIgnoreCase(str2); // true
```

### 1.4. 문자열 연산
- `concat()`: 문자열 합치기
- `trim()`: 공백 제거
- `split()`: 문자열 분리

#### 예시

```java
String str = " Hello ";
String trimmed = str.trim(); // "Hello"
String[] splitted = str.split(" "); // ["", "Hello", ""]
```

## 2. 컬렉션 프레임워크 (Collection Framework)

### 2.1. List 인터페이스
- `ArrayList`: 동적 배열
- `LinkedList`: 이중 연결 리스트

#### 예시

```java
List<String> arrayList = new ArrayList<>();
arrayList.add("Apple");
arrayList.add("Banana");

List<String> linkedList = new LinkedList<>();
linkedList.add("Cat");
linkedList.add("Dog");
```

### 2.2. Set 인터페이스
- `HashSet`: 해시 테이블을 이용한 집합
- `TreeSet`: 트리를 이용한 정렬된 집합

#### 예시

```java
Set<String> hashSet = new HashSet<>();
hashSet.add("Apple");
hashSet.add("Banana");

Set<String> treeSet = new TreeSet<>();
treeSet.add("Cat");
treeSet.add("Dog");
```

### 2.3. Map 인터페이스
- `HashMap`: 키-값 쌍을 해시 테이블에 저장
- `TreeMap`: 키-값 쌍을 트리에 저장

#### 예시

```java
Map<String, Integer> hashMap = new HashMap<>();
hashMap.put("Apple", 1);
hashMap.put("Banana", 2);

Map<String, Integer> treeMap = new TreeMap<>();
treeMap.put("Cat", 1);
treeMap.put("Dog", 2);
```

## 3. 날짜와 시간 (Date and Time)

### 3.1. `java.util.Date`와 `java.util.Calendar`
- `Date`: 날짜와 시간을 나타내는 클래스
- `Calendar`: 날짜와 시간을 조작하는 클래스

#### 예시

```java
Date date = new Date();
Calendar cal = Calendar.getInstance();
cal.setTime(date);
```

### 3.2. `java.time` 패키지
- `LocalDate`: 날짜만 처리
- `LocalTime`: 시간만 처리
- `LocalDateTime`: 날짜와 시간 처리

#### 예시

```java
LocalDate today = LocalDate.now();
LocalTime time = LocalTime.now();
LocalDateTime dateTime = LocalDateTime.now();
```
