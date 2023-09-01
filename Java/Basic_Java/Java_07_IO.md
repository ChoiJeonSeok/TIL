# Java의 파일 입출력 (I/O)

- 파일 입출력은 데이터를 파일로부터 읽거나 파일에 쓰는 작업을 의미한다. 

## FileReader와 BufferedReader

- **개념**
  - `FileReader`는 텍스트 파일을 문자 단위로 읽어오는 클래스
  - `BufferedReader`는 버퍼를 사용하여 입출력을 빠르게 처리하는 클래스
  
- **주의점** 
  - 예외 처리는 필수. 
  - 파일을 찾을 수 없거나 읽기 권한이 없는 경우에 `IOException`이 발생할 수 있다.

- **사용방법**
  -  `FileReader`로 파일을 열고, `BufferedReader`로 해당 파일을 읽는다.

- **사용하는 곳**
  -  텍스트 파일을 읽어서 데이터를 처리해야 하는 경우에 사용된다.

### 예제 코드 및 실행 방법

```java
// FileReader와 BufferedReader import.
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFileExample {
    public static void main(String[] args) {
        try {
            // FileReader로 'example.txt' 파일을 연다.
            FileReader reader = new FileReader("example.txt");
            // BufferedReader로 파일을 읽어온다.
            BufferedReader bufferedReader = new BufferedReader(reader);
            
            String line;
            // readLine() 메서드로 한 줄씩 읽어온다.
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }
            // 리소스를 반납한다.
            bufferedReader.close();
        } catch (IOException e) {
            // 예외가 발생하면 스택 트레이스를 출력한다.
            e.printStackTrace();
        }
    }
}
```

**실행 방법**

1. 위 코드를 `ReadFileExample.java` 파일에 저장한다.
2. 터미널에서 `javac ReadFileExample.java` 명령으로 컴파일한다.
3. `java ReadFileExample` 명령으로 실행한다.

**java ReadFileExample 실행시 일어나는 일**

1. **컴파일 단계**: `javac ReadFileExample.java` 명령을 실행하면 Java 컴파일러는 `ReadFileExample.java` 소스 파일을 바이트코드로 변환한다. 이 때 `ReadFileExample.class`라는 새로운 파일이 생성된다.

2. **실행 단계**: `java ReadFileExample` 명령을 실행하면 Java 가상 머신(JVM)은 `ReadFileExample.class` 파일을 로드하여 프로그램을 실행한다.

3. **파일 읽기**: 프로그램이 실행되면 `example.txt`라는 파일을 찾아 내용을 읽기 시작한다. 이 파일이 현재 디렉토리에 없거나 읽을 수 없다면 `IOException`이 발생하고 에러 메시지가 출력된다.

4. **출력**: 파일이 정상적으로 열리면, 프로그램은 파일의 내용을 한 줄씩 읽어 콘솔에 출력한다. 파일의 끝에 도달하면 `BufferedReader.readLine()` 메서드는 `null`을 반환하고 `while` 루프가 종료된다.

5. **리소스 해제**: 모든 작업이 끝나면 `BufferedReader` 객체를 `close()` 메서드로 닫아 리소스를 해제한다.

6. **결과**: `example.txt` 파일의 내용이 콘솔에 출력된다.


## FileWriter와 BufferedWriter

- **개념**
  - `FileWriter`는 텍스트 파일에 문자 단위로 쓰는 클래스
  - `BufferedWriter`는 버퍼를 사용하여 입출력을 빠르게 처리하는 클래스

- **주의점**
  -  예외 처리와 파일 클로징 잘 해야한다.

- **사용방법**
  - `FileWriter`로 파일을 열고, `BufferedWriter`로 해당 파일에 쓴다.

- **사용하는 곳**
  - 텍스트 데이터를 파일에 저장해야 하는 경우에 사용된다.

### 예제 코드 및 실행 방법

```java
// FileWriter와 BufferedWriter import
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class WriteFileExample {
    public static void main(String[] args) {
        try {
            // FileWriter로 'example.txt' 파일을 연다.
            FileWriter writer = new FileWriter("example.txt");
            // BufferedWriter로 파일에 쓴다.
            BufferedWriter bufferedWriter = new BufferedWriter(writer);
            
            // write 메서드로 문자열을 쓴다.
            bufferedWriter.write("Hello World");
            // newLine 메서드로 줄 바꿈을 한다.
            bufferedWriter.newLine();
            bufferedWriter.write("See You Again");
            
            // 리소스를 반납합니다.
            bufferedWriter.close();
        } catch (IOException e) {
            // 예외가 발생하면 스택 트레이스를 출력.
            e.printStackTrace();
        }
    }
}
```

**실행 방법**

1. 위 코드를 `WriteFileExample.java` 파일에 저장한다.
2. 터미널에서 `javac WriteFileExample.java` 명령으로 컴파일한다.
3. `java WriteFileExample` 명령으로 실행한다.

**java ReadFileExample 실행시 일어나는 일**

1. **컴파일 단계**: 터미널에서 `javac WriteFileExample.java` 명령을 실행하면, Java 컴파일러가 `WriteFileExample.java` 소스 파일을 컴파일하여 바이트코드로 변환한다. 이 과정에서 `WriteFileExample.class`라는 파일이 생성된다.

2. **실행 단계**: `java WriteFileExample` 명령을 터미널에서 실행하면, Java 가상 머신(JVM)은 `WriteFileExample.class` 바이트코드 파일을 로드하여 프로그램을 시작한다.

3. **파일 쓰기**: 프로그램이 실행되면, `FileWriter`를 통해 `example.txt`라는 이름의 파일을 생성하거나 덮어씁니다. 그 다음 `BufferedWriter`를 통해 해당 파일에 문자열을 쓴다.

4. **내용 기록**: `bufferedWriter.write("Hello World");`와 같은 코드 라인을 통해 "Hello World"라는 문자열이 파일에 기록된다. `bufferedWriter.newLine();`은 줄 바꿈을 의미하므로, 다음 문자열 "See You Again"은 새로운 줄에 기록된다.

5. **리소스 해제**: 모든 내용이 파일에 기록된 후에는 `bufferedWriter.close();`를 통해 열려있는 파일과 연결된 리소스를 해제한다.

6. **예외 처리**: 파일 쓰기 과정에서 문제가 발생하면 (예: 디스크 공간이 부족하거나 파일에 쓰기 권한이 없는 경우), `catch` 블록이 실행되어 에러 메시지를 콘솔에 출력한다.

7. **결과**: `example.txt` 파일은 프로그램이 작성한 내용인 "Hello World"와 "See You Again"을 포함하게 된다. 


#### 이렇게 Java에서는 `FileReader`, `BufferedReader`, `FileWriter`, `BufferedWriter` 등을 사용하여 파일 입출력을 처리할 수 있다. 이 클래스들은 텍스트 파일의 입출력을 문자 단위로 처리하며, 버퍼를 사용하여 효율적인 입출력을 지원한다.