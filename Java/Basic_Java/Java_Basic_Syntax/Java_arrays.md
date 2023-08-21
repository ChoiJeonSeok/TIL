# 4. 배열

## 배열 선언 및 초기화
Java에서 배열은 동일한 타입의 데이터 요소들의 모임. 

```java
// 배열 선언 및 초기화
int[] numbers = new int[5]; // 크기가 5인 정수형 배열 생성
double[] grades = {85.5, 90.0, 78.3}; // 값으로 배열 초기화
```

## 배열의 길이와 인덱스
배열의 길이는 `length` 속성을 통해 얻을 수 있으며, 배열의 인덱스는 0부터 시작한다.

```java
int[] numbers = new int[5];
int length = numbers.length; // 배열의 길이

int firstNumber = numbers[0]; // 첫 번째 요소
int secondNumber = numbers[1]; // 두 번째 요소
```

## 다차원 배열
Java에서는 다차원 배열도 사용할 수 있다. 2차원 배열의 예제는 다음과 같다:

```java
int[][] matrix = new int[3][4]; // 3행 4열의 2차원 배열
matrix[0][0] = 1;
matrix[0][1] = 2;
// ...
```

## 배열의 복사
배열의 내용을 다른 배열로 복사하려면 `System.arraycopy()`나 `Arrays.copyOf()` 메서드를 사용할 수 있다:

```java
int[] sourceArray = {1, 2, 3};
int[] destinationArray = new int[sourceArray.length];
System.arraycopy(sourceArray, 0, destinationArray, 0, sourceArray.length);
```

## 가변 길이 인자 (Varargs)
메서드의 파라미터로 가변 개수의 인자를 받을 때 사용한다. 가변 길이 인자는 배열로 전달되며, `타입...` 형태로 선언한다:

```java
public void printNumbers(int... numbers) {
    for (int num : numbers) {
        System.out.println(num);
    }
}
```

## 배열과 메모리
- Java의 배열은 힙(heap) 영역에 할당된다. 배열은 연속된 메모리 공간에 저장되며, 각 요소는 인덱스를 통해 접근한다.
- 배열이 heap에 저장되는 이유는 배열의 크기가 실행 중에 동적으로 결정될 수 있기 때문이다. 실행 중에 크기가 결정되고 변경될 수 있는 동적 배열은 메모리를 동적으로 할당하고 해제해야 한다. 
- 힙은 프로그램 실행 중에 필요한 크기만큼 메모리를 할당하고 해제할 수 있는 유연한 영역이므로 동적 배열의 저장소로 적합하다.
