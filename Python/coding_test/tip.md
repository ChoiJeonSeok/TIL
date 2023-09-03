# Python 코딩 테스트 팁

## 1. I/O 최적화

### input() 대신 sys.stdin.readline()

- **정의**: `input()`은 Python의 내장 함수로 사용자로부터 입력을 받는다. `sys.stdin.readline()`은 `sys` 모듈의 함수로, 라인 단위로 입력을 받는다.
- **예시**: 
  ```python
  # input() 사용 예시
  n = int(input())
  
  # sys.stdin.readline() 사용 예시
  import sys
  n = int(sys.stdin.readline())
  ```
- **이유**: `input()`보다 `sys.stdin.readline()`이 더 빠른 이유는 내부 버퍼링 때문이다.
- **사용 케이스**: 대량의 데이터를 빠르게 입력받아야 할 때 유용하다.

### print() 대신 sys.stdout.write()

- **정의**: `print()`는 Python의 내장 함수로 출력을 한다. `sys.stdout.write()`는 `sys` 모듈의 함수로, 문자열을 콘솔에 출력한다.
- **예시**: 
  ```python
  # print() 사용 예시
  print("Hello, world!")
  
  # sys.stdout.write() 사용 예시
  import sys
  sys.stdout.write("Hello, world!\n")
  ```
- **이유**: 마찬가지로 내부 버퍼링 때문에 `sys.stdout.write()`가 `print()`보다 빠르다.
- **사용 케이스**: 대량의 데이터를 빠르게 출력해야 할 때 유용하다.

## 2. 알고리즘 최적화

### list 대신 deque 사용하기

- **정의**: `list`는 Python의 기본적인 배열 자료형이다. `deque`는 `collections` 모듈에서 제공하는 덱 자료형이다.
- **예시**: 
  ```python
  # list 사용 예시
  my_list = []
  my_list.append(1)
  my_list.pop(0)
  
  # deque 사용 예시
  from collections import deque
  my_deque = deque()
  my_deque.append(1)
  my_deque.popleft()
  ```
- **이유**: `list`의 앞쪽에 요소를 추가하거나 삭제하는 작업은 \(O(N)\) 시간이 걸린다. 반면에 `deque`는 \(O(1)\) 시간이 걸린다.
- **사용 케이스**: 스택, 큐 등의 자료 구조가 필요할 때 유용하다.

## 3. 코드 구조화

### 함수나 클래스 사용하기

- **정의**: 코드를 재사용하고 구조화하기 위해 함수나 클래스를 사용할 수 있다.
- **예시**: 
  ```python
  def factorial(n):
      if n == 0:
          return 1
      return n * factorial(n-1)
  ```
- **이유**: 코드의 재사용성을 높이고 가독성을 개선하기 위함.
- **사용 케이스**: 유사한 로직이 반복되거나, 복잡한 로직을 분리해야 할 때 유용하다.


물론입니다. 코딩 테스트에 유용한 추가 팁들을 아래에 나열하겠습니다.

## 4. 모듈 활용

### math 모듈

- **정의**: 수학 함수와 상수를 제공하는 내장 모듈
- **예시**:
  ```python
  import math
  
  # 제곱근 계산
  math.sqrt(4)  # 결과: 2.0
  ```
- **이유**: 복잡한 수학 연산을 간단하게 처리할 수 있다.
- **사용 케이스**: 제곱근, 로그 등의 수학 연산이 필요한 경우에 유용하다.

### itertools 모듈

- **정의**: 효율적인 반복 작업을 위한 여러 가지 함수를 제공하는 모듈
- **예시**: 
  ```python
  import itertools
  
  # 순열
  list(itertools.permutations([1, 2, 3], 2))
  ```
- **이유**: 반복문을 사용하여 만드는 것보다 더 빠르고 간결하게 반복 작업을 수행할 수 있다.
- **사용 케이스**: 순열, 조합 등의 반복 작업이 필요한 경우에 유용하다.

## 5. 재귀 함수의 깊이 제한 늘리기

- **정의**: Python에서 재귀 함수의 깊이는 기본적으로 제한되어 있지만 이를 늘릴 수 있다.
- **예시**:
  ```python
  import sys
  sys.setrecursionlimit(10**6)
  ```
- **이유**: 재귀 함수의 호출 깊이가 기본값보다 클 필요가 있을 때 이를 조정한다.
- **사용 케이스**: DFS 등 재귀를 사용하는 알고리즘에서 깊이 제한에 걸리는 것을 피하고 싶을 때 사용한다.

## 6. 문자열 처리 팁

### 문자열 불변성을 이용하기

- **정의**: Python에서 문자열은 불변(immutable)이다. 즉, 문자열을 변경할 수 없고, 새로운 문자열을 만들어야 한다.
- **예시**: 
  ```python
  # 불가능
  s = "hello"
  s[0] = "H"
  
  # 가능
  s = "H" + s[1:]
  ```
- **이유**: 문자열을 빈번하게 변경해야 하는 경우, 이를 리스트로 변환하여 처리하고 마지막에 다시 문자열로 변환하는 것이 더 효율적이다.
- **사용 케이스**: 문자열을 빈번하게 변경해야 하는 경우에 유용하다.
