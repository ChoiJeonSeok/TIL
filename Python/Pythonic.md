# Pythonic한 코드 작성 방법.
Python의 특성을 최대한 활용하여 가독성이 좋고 효율적인 코드를 작성하자.

## [**1. 리스트 컴프리헨션**](https://github.com/ChoiJeonSeok/TIL/blob/master/Python/knowledge/list_comprehension.md)

- 리스트 컴프리헨션은 기존 리스트를 기반으로 새로운 리스트를 생성하는 간결한 방법을 제공한다. 
- Python에서는 for 루프를 사용하여 리스트를 생성하거나 리스트 컴프리헨션을 사용하여 생성할 수 있다.
- 리스트 컴프리헨션은 일반적으로 람다 함수보다 사람이 읽기 쉽다. 또한 map 함수보다 빠르다는 장점이 있다.

예시:

```python
# for 루프 사용
squares = []
for i in range(10):
    squares.append(i * i)
print(squares)

# 리스트 컴프리헨션 사용
squares = [i * i for i in range(10)]
print(squares)
```

두 경우 모두 출력: `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`


- 리스트 컴프리헨션을 사용하면 For 루프와 If 문을 간결하게 결합할 수 있다.

```python
[x for x in range(10) if x % 2 == 0]
```

## [**2. 제너레이터**](https://github.com/ChoiJeonSeok/TIL/blob/master/Python/knowledge/yield.md)

- 제너레이터는 리스트나 튜플과 같은 반복 가능한 객체이다. 
- 리스트와 달리 임의의 인덱스로 인덱싱할 수 없지만, 여전히 for 루프를 통해 반복할 수 있다. 
- 제너레이터는 함수와 yield 문을 사용하여 생성된다.
- yield 문은 호출될 때 상태를 유지한다. 

예시:

```python
def gen():
    for i in range(10):
        yield i

for number in gen():
    print(number)
```

- yield 문은 함수의 실행을 일시 중지하고 값을 생성하여 전달한다.
- return 처럼 반환하고 끝나는 것이 아니기에 0부터 9까지의 숫자를 각각 별도의 줄에 출력한다.
- return 을 사용하면 함수 gen()은 iterable 객체가 아니게 된다. 따라서 TypeError가 발생한다.

## **3. `enumerate` 사용**

- `enumerate`는 Python의 내장 함수이다. 
- 이를 사용하면 자동 카운터를 가진 이터러블 객체를 루프로 처리할 수 있다.

예시:

```python
my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list):
    print(counter, value)
```

이것은 다음을 출력한다:

```
0 apple
1 banana
2 grapes
3 pear
```

## **4. 다중 할당**

- Python에서는 한 줄에 여러 변수에 값을 할당할 수 있다:

예시:

```python
a, b = 1, 2
print(a)  # 출력: 1
print(b)  # 출력: 2
```

## **5. `in` 키워드 사용**

- Python에서는 `in` 키워드를 사용하여 항목이 리스트에 있는지 확인할 수 있다:

예시:

```python
my_list = ['apple', 'banana', 'grapes', 'pear']
if 'banana' in my_list:
    print("Yes, 'banana' is in the fruits list")
```

출력: `Yes, 'banana' is in the fruits list`

## **6. 문자열 포매팅**


### C 스타일 문자열 포매팅
- Python 초기에는 C 스타일의 문자열 포매팅을 사용했다.
- "%" 연산자는 "튜플" (고정 크기의 리스트)에 포함된 `여러 변수`와 함께 포맷 문자열을 사용하여 포맷된다.
- 이 포맷 문자열에는 "%s"와 "%d"와 같은 "인수 지정자"라는 특수 기호와 일반 텍스트가 포함된다.

예시:

```python
name = "John"
print("Hello, %s!" % name)
```

출력: `Hello, John!`

예시2:

```python
name = "John"
age = 30
print("Hello, %s! You are %d years old." % (name, age))
```
여러 변수이므로 튜플로 묶는다.
출력 : `Hello, John! You are 30 years old.`

### **`str.format()` 메소드**
- 이 방식은 Python 2.6 이상에서 사용할 수 있다. C 스타일보다 유연하고 사용하기 편하다.

    ```python
    name = "John"
    age = 30
    print("Hello, {}! You are {} years old.".format(name, age))
    ```

### **f-문자열 (Formatted String Literals)**
- Python 3.6 이상에서 도입된 이 방식은 더욱 간결하고 직관적이다. 
- 이는 변수와 표현식을 문자열 리터럴 내부에 직접 삽입할 수 있게 해준다.

    ```python
    name = "John"
    age = 30
    print(f"Hello, {name}! You are {age} years old.")
    ```
- 모두 사용한 결과, f-문자열 포맷팅이 가장 가독성있고 사용하기 편리했다.

## **7. `zip` 사용**

`zip()`의 목적은 여러 컨테이너의 유사한 인덱스를 매핑하여 단일 엔티티로 사용할 수 있도록 하는 것이다.

예시:

```python
name = [ "Kim", "Choi", "Lee", "Cha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]

mapped = zip(name, roll_no, marks)

print(set(mapped)) 
```

출력 : {('Lee', 3, 60), ('Kim', 4, 40), ('Choi', 1, 50), ('Cha', 2, 70)}

1. `zip()`은 주어진 시퀀스들 중 가장 짧은 길이에 맞춰 작동한다. 더 긴 시퀀스의 남은 요소들이 무시되는 것을 막기 위해 `itertools.zip_longest`를 사용하여 가장 긴 시퀀스에 맞추어 묶고 빈 값에는 기본값을 설정할 수 있다.

```python
import itertools

names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30, 35]

# zip_longest를 사용하여 더 긴 리스트에 맞춤
# 여러 리스트가 있어도 하나의 fillvalue 값으로 기본값이 적용된다.
zipped = list(itertools.zip_longest(names, ages, fillvalue="No Age"))

for item in zipped:
    print(item)

# 코드 실행 시 결과
('Alice', 25)
('Bob', 30)
('Charlie', 35)
('Diana', 'No Age')    
```



2. 데이터 타입은 `zip` 객체이다. 반복 가능한 객체이며 리스트나 set, 딕셔너리와 같은 다른 데이터 타입으로 변환할 수 있다.
3. 두 리스트를 `zip()`으로 결합하여 딕셔너리를 만들 수 있다. 하나의 리스트가 키, 다른 하나가 값이 된다.

```python
# 딕셔너리 생성
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = dict(zip(names, ages))
print(people)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

4. `zip(*iterable)`을 사용하면 zip 된 리스트를 다시 원래의 리스트로 분리할 수 있다. 행렬의 전치와 같은 작업에 쓰인다.
```python
# 예시 1
# 언패킹과 재구성
matrix = [(1, 2, 3), (4, 5, 6)]
transposed = zip(*matrix)
print(list(transposed))  # [(1, 4), (2, 5), (3, 6)]


# 예시 2
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# 언패킹하여 원래 리스트로 복원
numbers, letters = zip(*pairs)

print("Numbers:", numbers)
print("Letters:", letters)
```

## **8. `*args`와 `**kwargs` 사용**

- `*args`와 `**kwargs`는 Python의 특수 문법으로, 메서드 시그니처에서 함수에 변수 개수의 인수를 전달하는 데 사용된다.
- 매서드 시그니처란
- *args는 임의의 개수의 위치 인수를 함수에 전달하는 데 사용된다. 이는 튜플 형태로 처리된다.<br> 아래의 예시에서 adder 함수는 임의의 개수의 숫자를 받아서 그 합계를 출력한다. <br>*args를 사용하면, 함수 호출 시 얼마나 많은 인수를 전달하든 상관없이 함수가 이를 처리할 수 있다. (C의 가변인자?)
- **kwargs는 임의의 개수의 키워드 인수를 함수에 전달하는 데 사용된다. 이는 딕셔너리 형태로 처리된다.<br>각 인수는 `key=value`의 형태로 전달되어야 한다.

예시:

```python
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)
```

출력:

```
Sum: 8
Sum: 22
Sum: 17
```

예시2:
```python
def print_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_data(name="John", age=30, country="USA")
```

출력2:
```
name: John
age: 30
country: USA
```

예시3: 둘 다 사용.
```python
def func(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

func(1, 2, 3, a=4, b=5)
```

출력3: <br>`*args`는 위치 인자 1,2,3을 받고 `**kwargs`는 키워드 인자 a=4, b=5를 받아들인다.
<br>함수 내부에서는 `args`가 튜플로, `kwargs`가 딕셔너리로 처리된다.
```
1
2
3
a = 4
b = 5
```

## **9. `getattr`와 `setattr` 사용**

- 둘 다 Python의 내장 함수로, 객체의 속성에 동적으로 접근하는데 사용된다.
- 객체의 구조를 미리 알 수 없는 상황이나 복잡한 데이터 구조와 상호 작용할 때 특히 유용하다.

### `getattr(object, name[, default])`

- **용도**: 객체의 특정 속성 값을 가져온다.
- **매개변수**:
  - `object`: 속성 값을 조회할 객체
  - `name`: 문자열 형태로 제공되는 속성 이름
  - `default`: (선택적) 해당 속성이 객체에 없을 때 반환되는 기본값
- **반환값**: 지정된 속성의 값이 반환된다. 속성이 존재하지 않고 `default` 값이 제공된 경우, `default` 값이 반환된다. `default` 값이 없을 경우 `AttributeError`가 발생한다.
- **사용 사례**: `getattr`은 런타임에 속성 이름을 결정할 때. 예를 들어, 사용자 입력에 따라 다른 속성 값을 읽어야 할 때 사용할 수 있다.

### `setattr(object, name, value)`

- **용도**: 객체의 특정 속성에 값을 설정한다.
- **매개변수**:
  - `object`: 속성 값을 설정할 객체
  - `name`: 문자열 형태로 제공되는 속성 이름
  - `value`: 해당 속성에 할당할 값
- **반환값**: `None`. 이 함수는 값을 설정하고 끝나며 별도의 반환값을 제공하지 않는다.
- **사용 사례**: `setattr`은 객체의 속성 값을 동적으로 변경하거나 새로운 속성을 추가할 때 사용된다. 속성이 존재하지 않는 경우, 새로운 속성이 생성되고 제공된 값이 할당된다.

### `.` 연산자와 `hasattr` 함수
- `.` 연산자를 사용해 객체의 속성에 접근할 수도 있으나, 이 방법은 속성 이름이 런타임에 결정되는 동적 접근을 지원하지 않는다. 
- 대신 `hasattr` 함수를 사용하면 객체가 특정 속성을 가지고 있는지 확인할 수 있으며, 이는 `True` 또는 `False`를 반환한다. 
- 하지만 `hasattr`는 속성의 존재 여부만 확인할 수 있고, 해당 속성의 값을 검색하지는 못한다.


예시: 일반적인 사용 예시

```python
class Person:
    age = 23
    name = "Adam"

person = Person()
attr_name = "age"
print('The age is:', getattr(person, attr_name))
print('The age is:', person.age)
attr_name = "name"
print('The name is:', getattr(person, attr_name))
```

출력:

```
The age is: 23
The age is: 23
The name is : Adam
```

예시2: `getattr` 함수를 사용하여 기존 속성과 존재하지 않는 속성에 접근하는 예시.
```python
class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))  # 존재하는 속성
print('The salary is:', getattr(person, "salary", 50000))  # 존재하지 않은 속성과 default 값 설정
# 이미 속성이 있는 경우 default 값이 아닌 해당 값 출력
```

출력2: `getattr(person, "salary")`를 호출하면 에러 발생, 하지만 default 값을 호출하면 기본값 반환.
```
The age is: 23
The salary is: 50000
```

예시3: `setattr` 함수를 사용하여 새로운 속성을 생성하고 값을 설정하는 예시.
```python
setattr(person, "salary", 60000)  # Set a new attribute
print('The salary is:', getattr(person, "salary"))  # Now the attribute exists
```

출력3: `Person` 클래스의 인스턴스인 `person` 객체에 `salary`라는 새로운 속성을 추가하고, 속성의 값을 `60000`으로 설정한다. 
<br> `setattr(person, "salary", 60000)`은 `person.salary = 60000`과 같다.
```
The salary is: 60000
```

예시4: Runtime에 `getattr`을 사용하여 어떤 속성에 접근할지 결정하는 예시.
```python
person = Person()
attr_name = input("어떤 속성에 접근하실건가요? ")
print(getattr(person, attr_name))
```

출력4: input 입력칸에 해당 속성의 이름을 입력하면 된다. age, name, salary 중 하나를 입력하면 해당 값을 출력한다.
```
어떤 속성에 접근하실건가요? name
Adam
```

## **10. `@property` 사용** 
- @property는 데코레이터로
- 데코레이터란 Python의 기능 중 하나로, 기존 함수나 메서드의 동작을 수정하거나 확장할 때 사용된다.<br>`@` 기호와 함께 사용되며, 보통 함수나 메서드 정의 바로 위에 위치한다. 
<br>데코레이터는 함수를 매개변수로 받는 함수이다. 데코레이터는 입력으로 받은 함수를 `감싸는` 새로운 함수를 반환하며, 이 `감싸는` 함수는 원래의 함수를 호출하기 전후에 추가적인 동작을 수행할 수 있다.
- 이를 통해 원래의 함수는 그대로 두면서, 그 함수의 동작을 확장하거나 수정하는 것이 가능하다.
- 이러한 기능은 코드의 재사용성을 높이고, 코드의 가독성을 향상시킨다.

기본적인 형태: 

```python
def my_decorator(func):
    def wrapper():
        # 원래 함수 호출 전에 수행할 동작
        result = func()  # 원래 함수 호출
        # 원래 함수 호출 후에 수행할 동작
        return result
    return wrapper

@my_decorator
def my_funciton():
    print("hello")
```

설명: <br>`my_decorator`는 데코레이터이며, `func`는 데코레이터가 적용되는 함수.
<br>`wrapper`는 감싸는 함수로, 원래 함수를 호출하기 전후에 추가적인 동작을 수행한다.
<br>`my_decorator`는 `wrapper`를 반환하므로, `my_decorator`를 적용한 함수는 `wrapper`로 대체된다.
<br>따라서 `my_function` 함수는 `hello`를 출력하기 전에 `wrapper`에서 설정한 동작을 수행되길 기다린 후 `hello`를 출력하고 이후 `wrapper`에 설정된 동작을 수행하게 한다.

예시:

```python
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property # getter
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter # setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

# 객체 생성
c = Celsius()

# 온도 설정
c.temperature = 25

# 온도 가져오기
print(c.temperature)  # "Getting value..."를 출력하고, 25를 반환합니다.

# 화씨로 변환
print(c.to_fahrenheit())  # 77.0를 반환합니다.

# 온도를 절대영도 이하로 설정하려고 하면 ValueError가 발생합니다.
c.temperature = -274  # ValueError: Temperature below -273.15 is not possible.
```

출력:
```
Setting value...
Getting value...
25
77.0
Setting value...
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[10], line 14
     11 print(c.to_fahrenheit())  # 77.0를 반환합니다.
     13 # 온도를 절대영도 이하로 설정하려고 하면 ValueError가 발생합니다.
---> 14 c.temperature = -274

Cell In[3], line 17, in Celsius.temperature(self, value)
     15 print("Setting value...")
     16 if value < -273.15:
---> 17     raise ValueError("Temperature below -273.15 is not possible.")
     18 self._temperature = value

ValueError: Temperature below -273.15 is not possible.
```

- `setter`란 객체 지향 프로그래밍에서 사용되는 용어. 특정 속성의 값을 설정(set)하는 데 사용되는 메서드를 가리킨다. 객체의 내부 상태를 캡슐화하고, 속성에 대한 유효성 검사나 추가적인 처리를 수행할 수 있다.
- 위 코드에서 `temperature` 속성의 `setter`는 입력받은 온도 값이 실제로 가능한 값인지 확인하는 역할을 한다. 입력 값이 `-273.15`보다 작으면 `ValuError`를 발생시킨다. 
- `temperature`에 값이 실제로 입력되기 전에 `setter`가 먼저 실행된다고 봐도 좋다.
- `@property`가 붙은 `temperature` 메서드는 `getter`이다.
  <br>호출되면 `_temperature` 인스턴스 변수의 값을 반환한다.

## 11. 긴 여러 줄의 문자열 생성
- `"""` 또는 `'''` 삼중 따옴표를 사용하면 감싸인 문자열 내에서는 줄 바꿈을 자유롭게 사용할 수 있다.

```python
long_string = """아주 긴 문자열도
언제든지 줄바꿈을 할
수 있다."""
```

## 12. 리스트 정렬 확인
- `all()` 함수와 `zip()` 함수를 사용하여 리스트 정렬을 확인할 수 있다.

```python
def is_sorted(lst):
  return all(a <= b for a, b in zip(lst, lst[1:]))
```

## [13. assert : 개발용 간이 테스트 시험지.](https://github.com/ChoiJeonSeok/TIL/blob/master/Python/knowledge/assert.md)
- 조건이 참인지 확인하는 데 사용된다.
- 개발 과정에서 오류를 빠르게 발견하고, 디버깅을 돕는데 사용된다.
- 또한 코드를 작성함에 있어 그 작동 과정을 개발자가 정확하게 이해하고 있는지 스스로 점검하는 용도로도 사용될 수 있다. assert를 어디에 어떤 조건으로 작성해야 하는지 알아야 적절한 테스트가 가능하기 때문이다.
- 조건이 거짓이면 'AssertionError'를 발생시키고 개발자가 정한 메시지와 함께 프로그램을 중단시킨다.
- 리스트가 정렬되었는지 확인하는 함수에 `assert`를 추가하는 것은, 해당 함수가 올바른 결과를 반환하는지 검증하는 데 사용된다. 
 
- 예를 들어, `is_sorted` 함수를 기준으로 `assert`를 추가한다면, 특정한 리스트에 대해 함수가 `True` 또는 `False`를 올바르게 반환하는지 확인할 수 있다.

```python
def is_sorted(lst):
    return all(a <= b for a, b in zip(lst, lst[1:]))

# 정렬된 리스트 테스트
sorted_list = [1, 2, 3, 4, 5]
assert is_sorted(sorted_list), "리스트가 정렬되어 있어야 합니다."

# 정렬되지 않은 리스트 테스트
unsorted_list = [5, 3, 4, 1, 2]
assert not is_sorted(unsorted_list), "리스트가 정렬되지 않았어야 합니다."
```

- 첫 번째 `assert`는 `sorted_list`가 정렬되었는지 확인한다. 만약 리스트가 정렬되어 있다면 `is_sorted` 함수는 `True`를 반환하고, 그렇지 않다면 `AssertionError`가 발생한다.

- 두 번째 `assert`는 `unsorted_list`가 정렬되지 않았음을 확인한다. 이 리스트가 정렬되지 않았다면 `is_sorted` 함수는 `False`를 반환하고, `assert not` 구문은 성공한다. 그러나 만약 리스트가 실제로 정렬되어 있다면 `AssertionError`가 발생한다.

- 이러한 방식으로 `assert`는 코드가 의도한 대로 작동하는지 검증하는 데 사용될 수 있다.


## [14. 컨텍스트 매니저 (Context Managers): 리소스의 효율적 관리](https://github.com/ChoiJeonSeok/TIL/blob/master/Python/knowledge/Context_Managers.md)
- 컨텍스트 매니저 `with` 문은 파일, 네트워크 연결 등의 리소스를 안전하게 사용하고 해제하는 데 사용된다.
- 리소스의 할당과 해제를 자동화하여 코드를 더 깔끔하고 안전하게 만든다.
- 컨텍스트 매니저는 `__enter__`와 `__exit__` 두 가지 매직 메소드(magic methods)를 구현함으로써 정의된다. `__enter__` 메소드는 리소스가 생성되거나 할당될 때 호출되며, `__exit__` 메소드는 리소스가 더 이상 필요하지 않을 때 호출되어 리소스를 정리한다.
- 이를 통해 리소스 누수(resource leaks)를 방지하고, 예외가 발생해도 리소스가 안전하게 해제된다.


```python
with open('file.txt', 'r') as file:
    contents = file.read()
```

- 위 코드에서 `open` 함수는 파일을 열고, 파일 객체를 반환한다. `with` 문은 `open`이 반환한 파일 객체를 컨텍스트 매니저로 사용한다.
- `with` 블록 내에서 파일 내용을 읽는다. 이 블록을 벗어나면, 컨텍스트 매니저는 자동으로 파일을 닫아준다.
- 이 방식은 파일을 명시적으로 닫을 필요 없이, 예외 발생 여부에 관계없이 파일을 안전하게 닫는 것을 보장한다.

#### 컨텍스트 매니저의 확장된 사용
- 컨텍스트 매니저는 파일 처리뿐만 아니라 데이터베이스 연결, 네트워크 세션 관리 등 다양한 리소스 관리에 활용될 수 있다.
- 예를 들어, 데이터베이스 세션을 관리하는 컨텍스트 매니저는 세션이 시작될 때 데이터베이스 연결을 생성하고, 세션이 종료될 때 연결을 안전하게 닫는다.

```python
class DatabaseConnection:
    def __enter__(self):
        # 데이터베이스 연결을 생성
        self.connection = create_connection()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 연결을 해제
        self.connection.close()

with DatabaseConnection() as conn:
    # 데이터베이스 작업 수행
    ...
```

- 위 예시에서 `DatabaseConnection` 클래스는 컨텍스트 매니저로 작동한다. `with` 문을 사용하여 데이터베이스 연결을 생성하고 작업 후 자동으로 닫는다.

- 컨텍스트 매니저는 자원 관리를 위한 코드의 중복을 줄이고, 리소스 사용의 신뢰성을 높이는 효과적인 방법이다. 
- 이를 통해 코드의 안정성과 가독성이 향상되며, 예외 발생 시에도 리소스가 안전하게 해제되는 것을 보장할 수 있다.

## 15. **hasattr**

### 함수
- `hasattr` 함수는 객체가 특정 속성을 가지고 있는지 여부를 확인하는 데 사용되며, `print` 함수와 함께 사용하여 결과를 출력할 수 있다.
- 두 개의 매개변수를 받는다. 첫 번째는 속성을 확인할 객체, 두 번째는 확인할 속성의 이름이다.
- 해당 속성이 객체에 존재하면 `True`를, 존재하지 않으면 `False`를 반환한다.

### 사용 예시


#### 1번 예시 : 객체에 속성이 존재하는지 확인하기.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "멍멍!"

# 객체 생성
my_dog = Dog("바둑이", 3)

# hasattr을 사용하여 속성이 존재하는지 확인
print(hasattr(my_dog, 'name'))  # True (name 속성이 존재함)
print(hasattr(my_dog, 'height'))  # False (height 속성이 존재하지 않음)
```
- `my_dog` 객체에 `name`이라는 속성과 `height`라는 속성이 존재하는지 확인하였다.

#### 2번 예시 : 동적으로 속성 다루기
- 런타임에 속성의 존재 여부에 따라 다른 동작을 수행하거나 속성에 안전하게 접근하고 싶을 때 사용한다.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 객체 생성
my_dog = Dog("바둑이", 3)

# 사용자 입력을 받아 속성 이름 결정
property_name = input("확인하고 싶은 속성을 입력하세요: ")

# hasattr을 사용하여 속성 존재 여부 확인
if hasattr(my_dog, property_name):
    print(f"{property_name} 속성이 존재합니다.")
else:
    print(f"{property_name} 속성이 존재하지 않습니다.")
```

#### 3번 예시 : 속성의 존재 여부에 따른 다른 동작 수행
- 속성이 존재할 때는 값을 업데이트하고, 존재하지 않으면 새로운 속성을 추가하는 등에도 사용 가능하다.

```python
# 객체에 새로운 속성 추가 또는 업데이트 함수
def update_or_add_attribute(obj, attr, value):
    if hasattr(obj, attr):
        print(f"{attr} 속성이 존재하여 값을 업데이트합니다.")
        setattr(obj, attr, value)
    else:
        print(f"{attr} 속성이 존재하지 않아 새로운 속성을 추가합니다.")
        setattr(obj, attr, value)

# 사용 예시
update_or_add_attribute(my_dog, 'height', 50)
update_or_add_attribute(my_dog, 'age', 4)
```

- 특정 속성이 이미 존재하는지를 확인한 후, 존재하면 해당 속성의 값을 업데이트하고, 존재하지 않으면 새로운 속성을 추가한다.


## 16. [map](https://github.com/ChoiJeonSeok/TIL/blob/master/etc/Coming_Soon.md)

- `map` 함수는 주어진 함수를 반복 가능한(iterable) 데이터의 각 요소에 적용한다.
- 이 함수는 데이터 변환, 데이터 전처리 등에서 유용하게 사용된다.
- `map`은 함수와 반복 가능한 데이터를 인자로 받아, 각 요소에 함수를 적용한 결과를 map 객체로 반환한다.
- 반환된 map 객체는 `list()`, `set()` 등을 사용하여 다른 형태로 변환할 수 있다.
- `map`은 리스트 컴프리헨션과 유사한 기능을 수행하지만, 더 함수적인 접근을 제공한다.

예를 들어, 모든 숫자의 제곱을 계산하는 경우 `map`을 사용할 수 있다:

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # 출력: [1, 4, 9, 16, 25]
```

- 여기서 `lambda x: x ** 2`는 각 숫자를 제곱하는 익명 함수이며, `numbers` 리스트의 각 요소에 적용된다.
- `map` 함수는 이 연산의 결과를 map 객체로 반환한다.
- `list(squared)`를 통해 결과를 리스트 형태로 변환하여 출력한다.

### `map` 함수 여러 데이터 타입에 적용하기
- 문자열 리스트와 같은 다른 데이터 타입에도 적용할 수 있다. 
- 예를 들어, 모든 문자열을 대문자로 변환하는 경우:

```python
words = ["apple", "banana", "cherry"]
uppercased = map(str.upper, words)
print(list(uppercased))  # 출력: ['APPLE', 'BANANA', 'CHERRY']
```

- `str.upper` 함수는 문자열을 대문자로 변환한다.
- 이 함수를 `words` 리스트의 각 요소에 적용하여, 모든 문자열을 대문자로 변환한 결과를 반환한다.

### `map` 함수 lambda 함수와 사용하기
- 예를 들어, 두 리스트의 요소를 더하는 경우:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # 출력: [5, 7, 9]
```

- 여기서 `lambda x, y: x + y`는 두 숫자를 더하는 함수이며, `list1`과 `list2`의 각 요소에 대해 적용된다.
- `map`은 두 리스트의 각 요소를 순서대로 취하여 함수에 전달하고, 그 결과를 map 객체로 반환한다.



## 17 **슬라이싱**

### 문법 `시퀀스[시작:끝:스텝]` 형태.

- `시작`: 슬라이스가 시작되는 인덱스. 생략하면 0(시작점)으로 간주된다.
- `끝`: 슬라이스가 끝나는 인덱스. 생략하면 시퀀스의 끝으로 간주된다. 중요한 점은 이 인덱스의 요소는 포함되지 않는다는 것이다.
- `스텝`: 인덱스 간의 거리. 생략하면 1로 간주된다. 음수일 경우 역방향으로 슬라이싱한다.

### **예시와 설명**

1. **기본 슬라이싱**:
   ```python
   my_list = [0, 1, 2, 3, 4, 5]
   slice1 = my_list[1:4]  # 결과: [1, 2, 3]
   ```
   여기서 `my_list[1:4]`는 인덱스 1부터 3까지의 요소를 추출한다.

2. **음수 인덱스 사용**:
   ```python
   slice2 = my_list[-3:-1]  # 결과: [3, 4]
   ```
   여기서 `-3`은 뒤에서 세 번째 요소를 나타내고, `-1`은 마지막 요소 바로 앞을 나타낸다.

3. **시작 또는 끝 생략**:
   ```python
   slice3 = my_list[2:]  # 결과: [2, 3, 4, 5]
   slice4 = my_list[:3]  # 결과: [0, 1, 2]
   ```
   `my_list[2:]`는 인덱스 2부터 끝까지, `my_list[:3]`는 시작부터 인덱스 2까지를 의미한다.

4. **스텝 사용**:
   ```python
   slice5 = my_list[::2]  # 결과: [0, 2, 4]
   ```
   `my_list[::2]`는 전체 리스트에서 한 요소씩 건너뛰며 추출한다.

5. **역순 슬라이싱**:
   ```python
   slice6 = my_list[::-1]  # 결과: [5, 4, 3, 2, 1, 0]
   ```
   `my_list[::-1]`은 리스트를 역순으로 뒤집어준다.

6. **문자열에서의 슬라이싱**:
   ```python
   text = "Hello World"
   hello = text[:5]  # 'Hello'
   world = text[6:]  # 'World'
   reversed_text = text[::-1]  # 'dlroW olleH'
   ```
   문자열에도 리스트와 동일한 방법으로 슬라이싱을 적용할 수 있다.

### **슬라이싱의 장점**

- **간결성**: 복잡한 루프나 조건문 없이 한 줄로 간단하게 요소를 추출할 수 있다.
- **효율성**: 내부적으로 최적화되어 있어 대용량 데이터를 처리할 때도 빠르다.
- **유연성**: 시작점, 끝점, 간격을 다양하게 조절하여 다양한 작업을 손쉽게 할 수 있다.
