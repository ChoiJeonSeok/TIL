# `yield`

- Python의 `yield` 키워드는 제너레이터를 구현할 때 사용된다. 
- 이 키워드는 코드의 복잡성을 줄이고, 메모리 효율성을 높이는 데 도움이 된다.

## `yield`의 기본 개념과 역할

### 값 생성 및 반환
- `yield`는 함수 내에서 값을 반환하고 함수의 실행을 일시 중지한다. 
- 이는 제너레이터 함수가 다음 번 호출될 때까지의 상태(지역 변수, 실행 위치 등)를 유지한다. 
- `yield` 다음에 나오는 값이 호출자에게 반환되며, 다음 호출 시 `yield` 다음 줄부터 실행이 재개된다.
- 아래 코드의 `simple_counter` 함수는 최대값 `max`까지 증가하는 숫자를 순차적으로 생성한다. 

```python
def simple_counter(max):
    n = 0
    while n < max:
        yield n
        n += 1

# 제너레이터 사용
counter = simple_counter(3)
print(next(counter)) # 첫 번째 호출 0
print(next(counter)) # 두 번째 호출 1
print(next(counter)) # 세 번째 호출 2
```

### `yield`의 작동 방식 설명

1. **첫 번째 호출 (`next(counter)`)**:
   - `n`은 0에서 시작한다.
   - `while` 루프 조건이 참이므로 루프 내부로 진입한다.
   - `yield n`은 0을 반환하고 함수의 실행을 일시 중지한다.
   - 이 시점에서 함수의 상태 (여기서는 `n`의 값)는 유지된다.

2. **두 번째 호출**:
   - 함수는 `yield` 다음 줄인 `n += 1`에서 실행을 재개한다.
   - `n`은 1이 되고, 다시 `while` 루프의 시작으로 돌아간다.
   - `yield n`은 이번에는 1을 반환하고 다시 실행을 중지한다.

3. **세 번째 호출**:
   - 함수는 `n += 1`에서 실행을 재개하여 `n`을 2로 만든다.
   - 다시 루프를 실행하여 `yield n`은 2를 반환한다.

### 메모리 효율성
- 제너레이터는 필요할 때마다 값을 생성하고 반환한다. 
- 이는 모든 데이터를 메모리에 저장하지 않기 때문에, 특히 대규모 데이터셋을 처리할 때 메모리 사용량을 크게 줄일 수 있다.

### 상태 유지
- `yield`를 사용하는 제너레이터 함수는 호출 사이에 상태를 유지한다. 
- 이는 함수가 다음 호출 시 이전 상태에서 계속 실행될 수 있도록 한다.

## `yield` 활용 예시

- 피보나치 수열 생성기

```python
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 제너레이터 사용
for value in fibonacci_generator(5):
    print(value)
```

- `fibonacci_generator` 함수는 피보나치 수열의 첫 `n` 항을 생성한다. 
- 각 `yield`는 현재 항을 반환하고, 함수의 상태를 일시 중지한다.

## `yield`의 활용 및 장점

### 간결한 코드 작성
- 복잡한 데이터 처리 로직을 간결하고 이해하기 쉬운 코드로 작성할 수 있다. 
- `yield`는 복잡한 반복자를 간단하게 구현하는 데 유용하다.

### 데이터 스트리밍
- 파일 읽기, 네트워크 요청 등에서 데이터를 청크 단위로 효율적으로 처리할 수 있다.

### 커스텀 반복자 생성
- 사용자 정의 반복자를 쉽게 만들 수 있으며, 복잡한 반복 로직을 캡슐화할 수 있다.

## 제너레이터의 반복 종료와 관련된 추가 정보 제공
- 제너레이터가 더 이상 생성할 값이 없을 때, 호출자에게 유용한 정보나 상태를 알려주기 위해 추가 정보를 제공하는 경우가 있다. 
- 제너레이터의 반복이 정상적으로 완료되었는지, 아니면 특정 조건으로 인해 조기에 종료되었는지를 나타내는 데 사용된다.

### yiled와 return을 함께 사용하는 경우
- `yiled`는 제너레이터 함수에서 값을 순차적으로 생성하고 반환하는 데 사용된다.
- `return`은 제너레이터의 반복이 종료될 때 추가적인 정보를 제공하는 데 사용된다. 
  - `return`으로 반환된 값은 `StopIteration` 예외의 인자로 전달되어, 제너레이터 사용자가 이를 활용할 수 있다.

```python
def my_generator():
    yield "Hello"
    yield "World"
    return "No more elements"

gen = my_generator()
print(next(gen))  # "Hello"
print(next(gen))  # "World"
try:
    print(next(gen))
except StopIteration as e:
    print(e.value)  # "No more elements"
```

1. my_generator `함수는 두 개의` yield` 문을 사용해 "Hello"와 "World"를 차례로 생성한다. 
2. 마지막 `return`은 "No more elements"라는 값을 `StopIteration` 예외와 함께 반환하며, 제너레이터의 종료를 나타낸다.
3. 만약 `StopIteration` 예외를 처리하지 않는다면, 제너레이터가 반환할 값이 없을 때 예외가 발생하고 프로그램은 그 지점에서 중단된다.
4. 프로그램의 비정상적 종료를 막기 위해 try except 문으로 예외를 처리하였다.
5. `return`문에 지정된 값이 `StopIteration` 예외의 `value` 속성으로 설정되므로, `e.value`를 통해 `return`에 의해 반환된 값을 출력할 수 있다.