# Pythonic한 코드 작성 방법.
Python의 특성을 최대한 활용하여 가독성이 좋고 효율적인 코드를 작성하자.

**1. 리스트 컴프리헨션**

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

**2. 제너레이터**

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

**3. `enumerate` 사용**

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

**4. 다중 할당**

- Python에서는 한 줄에 여러 변수에 값을 할당할 수 있다:

예시:

```python
a, b = 1, 2
print(a)  # 출력: 1
print(b)  # 출력: 2
```

**5. `in` 키워드 사용**

- Python에서는 `in` 키워드를 사용하여 항목이 리스트에 있는지 확인할 수 있다:

예시:

```python
my_list = ['apple', 'banana', 'grapes', 'pear']
if 'banana' in my_list:
    print("Yes, 'banana' is in the fruits list")
```

출력: `Yes, 'banana' is in the fruits list`

**6. 문자열 포매팅**

- Python은 새로운 포맷된 문자열을 생성하기 위해 C 스타일의 문자열 포매팅을 사용한다. 
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

**7. `zip` 사용**

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

>만약 인덱스가 서로 다르다면?
>묶을 수 있는 데까지 순차대로 묶고 나머지는 무시된다.

**8. `*args`와 `**kwargs` 사용**

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

**9. `getattr`와 `setattr` 사용**

- 둘 다 Python의 내장 함수로, 객체의 속성에 동적으로 접근하는데 사용된다.
- `getattr(object, name[, default])` : `object`라는 객체의 `name`이라는 속성의 값을 반환한다.<br>이때, `name`은 문자열로 주어져야 한다. 만약 해당 속성이 존재하지 않으면 `default`값을 반환한다.<br>getattr을 사용하면 속성 이름을 런타임에 결정하거나, 속성이 실제로 존재하는지 확인하지 않고도 속성에 접근할 수 있다.
- `setattr(object, name, value)` : `getattr()`과 유사하지만 값을 얻는 대신 속성의 값을 설정한다.<br>`object`라는 객체의 `name`이라는 속성에 `value`값을 할당한다. <br>만약 해당 속성이 존재하지 않으면, 새로운 속성을 생성하고 `value`값을 할당한다.

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
print('The name is:', getattr(person, attr_name)
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

**10. `@property` 사용** 
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

### 11. 긴 여러 줄의 문자열 생성
- `"""` 또는 `'''` 삼중 따옴표를 사용하면 감싸인 문자열 내에서는 줄 바꿈을 자유롭게 사용할 수 있다.

```python
long_string = """아주 긴 문자열도
언제든지 줄바꿈을 할
수 있다."""
```

### 12. 리스트 정렬 확인
- `all()` 함수와 `zip()` 함수를 사용하여 리스트 정렬을 확인할 수 있다.

```python
def is_sorted(lst):
  return all(a <= b for a, b in zip(lst, lst[1:]))
```

### 12. assert : 개발용 간이 테스트 시험지.
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


### 13. 컨텍스트 매니저 (Context Managers): 리소스의 효율적 관리
- 컨텍스트 매니저는 `with` 문과 함께 사용되어 파일, 네트워크 연결 등의 리소스를 안전하게 사용하고 해제하는 데 사용된다.
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