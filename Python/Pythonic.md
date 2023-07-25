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

**9. `getattr`와 `setattr` 사용**

- `getattr(object, name[, default])` : 객체의 속성에 접근하는 데 사용된다.

- `setattr(object, name, value)` : `getattr()`과 유사하지만 값을 얻는 대신 속성의 값을 설정한다.

예시:

```python
class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)
```

출력:

```
The age is: 23
The age is: 23
```

**10. `@property` 사용**

- Python에는 프로퍼티라는 개념이 있어 객체 지향 프로그래머의 생활을 훨씬 간단하게 만든다.

예시:

```python
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value