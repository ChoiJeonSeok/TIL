# Java 표준 라이브러리 목차

## 1. 자료형과 자료구조

### 1.1 기본 타입 (Primitive Types)
- `byte`, `short`, `int`, `long`
- `float`, `double`
- `char`, `boolean`

### 1.2 래퍼 클래스 (Wrapper Classes)
- `Integer`, `Long`, `Double`, `Character`, `Boolean`

### 1.3 문자열 (String)
- 문자열 생성, 수정, 비교

### 1.4 배열 (Arrays)
- 1차원, 다차원 배열

### 1.5 컬렉션 프레임워크 (Collections Framework)
- `List`, `Set`, `Map`, `Queue`

## 2. 입출력 (I/O)

### 2.1 콘솔 I/O
- `System.out`, `System.in`

### 2.2 파일 I/O
- `File`, `FileInputStream`, `FileOutputStream`

### 2.3 버퍼 I/O
- `BufferedReader`, `BufferedWriter`

### 2.4 객체 직렬화 (Serialization)
- `ObjectInputStream`, `ObjectOutputStream`

## 3. 네트워킹 (Networking)

### 3.1 소켓 (Sockets)
- `Socket`, `ServerSocket`

### 3.2 URL과 URI
- `URL`, `URI`

### 3.3 HTTP 통신
- `HttpURLConnection`

## 4. 날짜와 시간 (Date and Time)

### 4.1 기존 API
- `Date`, `Calendar`

### 4.2 새로운 API
- `LocalDate`, `LocalTime`, `LocalDateTime`

## 5. 유틸리티 클래스 (Utility Classes)

### 5.1 수학 관련
- `Math`, `BigInteger`, `BigDecimal`

### 5.2 정규표현식 (Regular Expression)
- `Pattern`, `Matcher`

### 5.3 랜덤 수 생성
- `Random`

### 5.4 타이머와 스케줄링
- `Timer`, `TimerTask`

## 6. 동시성 (Concurrency)

### 6.1 기본 스레딩
- `Thread`, `Runnable`

### 6.2 고급 스레딩
- `ExecutorService`, `ForkJoinPool`

### 6.3 동기화 유틸리티
- `CountDownLatch`, `CyclicBarrier`, `Semaphore`

### 6.4 락 (Locks)
- `ReentrantLock`, `ReadWriteLock`

## 7. GUI 개발

### 7.1 AWT
- `Component`, `Container`

### 7.2 Swing
- `JFrame`, `JPanel`, `JButton`

### 7.3 JavaFX
- `Stage`, `Scene`, `Control`

## 8. 데이터베이스 연동

### 8.1 JDBC
- `DriverManager`, `Connection`, `PreparedStatement`, `ResultSet`

### 8.2 JPA
- `EntityManager`, `Entity`

## 9. 암호화와 보안

### 9.1 기본 암호화
- `MessageDigest`

### 9.2 고급 암호화
- `Cipher`

### 9.3 키 관리
- `KeyStore`

## 10. 국제화 (Internationalization)

### 10.1 로케일 (Locale)
- `Locale`

### 10.2 리소스 번들 (Resource Bundle)
- `ResourceBundle`

물론, 제가 작성한 목차는 주요한 부분들을 포함하고 있지만, Java 표준 라이브러리는 아주 방대하므로 모든 것을 나열하기는 어렵습니다. 다음은 몇 가지 추가적인 섹션과 주제입니다:

## 11. 리플렉션 (Reflection)

### 11.1 클래스 정보 접근
- `Class`, `Field`, `Method`

### 11.2 동적 객체 생성
- `Constructor`

## 12. 애노테이션 (Annotations)

### 12.1 기본 애노테이션
- `@Override`, `@Deprecated`

### 12.2 사용자 정의 애노테이션
- `@interface`

## 13. 스트림 API (Stream API)

### 13.1 기본 스트림 연산
- `filter`, `map`, `reduce`

### 13.2 병렬 스트림
- `parallelStream`

## 14. 옵셔널 (Optional)

### 14.1 기본 사용법
- `Optional.of`, `Optional.empty`

### 14.2 옵셔널 연산
- `isPresent`, `ifPresent`, `orElse`

## 15. 함수형 인터페이스 (Functional Interfaces)

### 15.1 기본 함수형 인터페이스
- `Function`, `Consumer`, `Supplier`, `Predicate`

### 15.2 람다 표현식
- 람다 표현식의 기초와 활용

## 16. NIO (New I/O)

### 16.1 채널 (Channel)
- `FileChannel`, `SocketChannel`

### 16.2 버퍼 (Buffer)
- `ByteBuffer`, `CharBuffer`

## 17. 로깅 (Logging)

### 17.1 기본 로깅
- `java.util.logging.Logger`

### 17.2 로깅 레벨 설정
- `Level.FINE`, `Level.INFO`, `Level.WARNING`

