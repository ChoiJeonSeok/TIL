## tqdm
<br>

- 진행상황을 출력할 수 있게하는 함수
![image](https://user-images.githubusercontent.com/82266289/224945482-f6b3f6ea-bf0f-48fb-939f-a8cf9df8e835.png)

# 함수 정리

- type(변수) ⇒ 해당 변수의 자료형을 조회한다.
- python에서 범위는 보통 ~이상 ~미만이다.

## list comprehension

- [표현식 for 항목 in 반복 가능 객체 if 조건]
    - 표현식은 반복적으로 계산되는 식을 의미한다.
    - 항목은 반복 가능 객체에서 가져온 요소이다.
    - 반복 가능 객체란 리스트, 튜플, 문자열 등이 될 수 있다.
    - 조건은 필요시 사용하는 if 문이다.
- 할당
    - 변수 = [i for i in myList (이곳에 조건문)]
- 변수 = [(내부값 처리) for i in myList]
    
    ![Untitled](https://user-images.githubusercontent.com/82266289/225345198-6a947a04-cd87-4894-a2aa-6fa916f7fee9.png)
- 예를 들어, 
1부터 10까지의 정수 중에서 짝수만을 담은 리스트를 생성하는 코드를 리스트 컴프리헨션을 사용하여 작성하면 다음과 같습니다.

even_numbers = [x for x in range(1, 11) if x % 2 == 0]

위의 코드에서, range(1, 11)은 1부터 10까지의 정수를 나타내는 range 객체입니다. x % 2 == 0은 x가 짝수인지 확인하는 조건입니다. 따라서 even_numbers 리스트에는 [2, 4, 6, 8, 10]이 담기게 됩니다.

## 자료구조 관련 함수

![튜플은 생성할 때 초기화를 해야 하며, 
수정 및 내용 삭제가 불가하다.](https://user-images.githubusercontent.com/82266289/225344961-f778daac-0f2b-4a13-b843-5543d11fc9ae.png)

튜플은 생성할 때 초기화를 해야 하며, 
수정 및 내용 삭제가 불가하다.

```
# 'apple'은 key
# 123456은 value
mydict['apple'] = 123456
```

```
# 리스트에 데이터를 추가(삽입)
# append는 기존 리스트 목록 맨 뒤에 삽입이 된다.
mylist.append(1)

# insert로 리스트 추가하기
# insert는 내가 원하는 위치에 index를 지정해서 추가할 수 있다.
mylist.insert(0,4)

# 리스트에서 저장된 값을 참조하는데,
# 참조된 값은 더이상 사용하지 않는 경우
# 맨 뒤 값을 꺼내 할당하거나 조회한 뒤 삭제한다.
# [4, 1, 2, 3] => pop => 3 => [4, 1, 2]
temp = mylist.pop()

# remove함수는 mylist에서 첫번째 해당 값을 삭제
mylist.remove(1)

a = [1,2,3,4,5,6,7,8]
# 데이터 7의 index번호를 확인할 때
a.index(7)

# 데이터의 길이
len(mylist)

# update는 한꺼번에 여러 개의 요소를 추가 가능
s1.update([5,6,7])
```

## python 연산자

- 산술연산자. 값을 계산하기 위해 사용한다.
    
    ![Untitled 2](https://user-images.githubusercontent.com/82266289/225344980-09f51582-0aad-40f7-b26a-c47b75ff3223.png)
    
- 비교연산자. 값을 비교하기 위해 사용한다.
    
    ![Untitled 3](https://user-images.githubusercontent.com/82266289/225344984-e7821b0b-e579-495b-a8dd-d49146acf701.png)
- 할당연산자. 변수에 값을 할당하기 위해 사용한다.
    
    ![Untitled 4](https://user-images.githubusercontent.com/82266289/225344996-7f20a44f-9cbb-491a-bb7d-6414ed05f226.png)
    
- 논리연산자. 조건을 확인하기 위해 사용한다.
    
    ![Untitled 5](https://user-images.githubusercontent.com/82266289/225345005-2bc30ea8-0599-4a72-adab-5416612634ef.png)
    
- Bitwise 연산자. 비트단위의 연산을 하는데 사용된다.
    
    ![Untitled 6](https://user-images.githubusercontent.com/82266289/225345015-b65b1b95-9a65-4fec-9bd5-eb00b3b48448.png)
    
- 멤버쉽 연산자. 문자열, 리스트 또는 튜플과 같은 시퀀스 멤버십을 테스트하는데 사용된다.
    
    ![Untitled 7](https://user-images.githubusercontent.com/82266289/225345120-7ca201f8-daea-4697-af64-149e68c8b140.png)
    
- identity 연산자
    
    ![Untitled 8](https://user-images.githubusercontent.com/82266289/225345128-1c0f94f5-014d-4c43-9426-6f43522bd9e5.png)
    
- 파이썬 연산자 우선 순위
    
    ![Untitled 9](https://user-images.githubusercontent.com/82266289/225345139-f4576760-44dd-4b01-bfdc-dacab57591aa.png)
    

## 문자열

- len(변수) ⇒ 문자열의 길이를 잰다.
- split(구분자) ⇒ 구분자로 문장을 나눈다.
split(’ ‘) ⇒ 공백으로 나눔.
aa = a.split(’ ‘) ⇒ list에 단어 단위로 나눠서 들어온다.
- enumerate()
    
    - [파이썬의 enumerate() 내장 함수로 for 루프 돌리기](https://www.daleseo.com/python-enumerate/)
    
    - python의 내장함수로 index와 값(원소)를 동시에 접근하며 for 문을 돌릴 수 있게 한다.
    - 기본적으로 인덱스와 원소로 이루어진 tuple을 만든다. 
    인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 unpacking을 해줘야 한다.
        
        ![Untitled 10](https://user-images.githubusercontent.com/82266289/225345184-8de0d31c-6a29-46db-9955-33f6db75f8eb.png)
        
        ![Untitled 11](https://user-images.githubusercontent.com/82266289/225345150-c8c702af-d71c-44f9-b434-40899b3b3d5f.png)
        
    - 인덱스 시작이 0이 아니어야 한다면, 
    `for i, letter in enumerate(['A', 'B', 'C'], start=1):`
    이렇게 start 인자에 시작하고 싶은 숫자를 작성한다.
    - `enumerate()` 함수는 파이썬 내장 함수 중 하나로, 반복 가능한 객체(리스트, 튜플, 문자열 등)를 입력 받아 인덱스와 값을 동시에 반환하는 객체를 생성합니다.
        
        아래는 enumerate() 함수를 사용한 예시입니다.
        
        ```
        fruits = ['apple', 'banana', 'cherry']
        for idx, fruit in enumerate(fruits):
            print(idx, fruit)
        
        ```
        
        위 코드의 실행 결과는 다음과 같습니다.
        
        ```
        0 apple
        1 banana
        2 cherry
        
        ```
        
        `enumerate()` 함수는 기본적으로 인덱스와 원소로 이루어진 튜플을 만듭니다. 따라서, 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 unpacking을 해줘야 합니다. unpacking 예시는 아래와 같습니다.
        
        ```
        for idx, fruit in enumerate(fruits):
            print(f"index: {idx}, fruit: {fruit}")
        
        ```
        
        위 코드의 실행 결과는 다음과 같습니다.
        
        ```
        index: 0, fruit: apple
        index: 1, fruit: banana
        index: 2, fruit: cherry
        
        ```
        
        `enumerate()` 함수의 start 인자를 이용하면 인덱스 시작값을 지정할 수도 있습니다. 아래는 start 인자를 이용한 예시입니다.
        
        ```
        for idx, fruit in enumerate(fruits, start=1):
            print(f"index: {idx}, fruit: {fruit}")
        
        ```
        
        위 코드의 실행 결과는 다음과 같습니다.
        
        ```
        index: 1, fruit: apple
        index: 2, fruit: banana
        index: 3, fruit: cherry
        
        ```
        
- lower(), upper() ⇒ 알파벳 문자들을 소문자, 대문자로 변환.
- startswith(), endswith() ⇒ ~로 시작하는, ~로 끝나는 파일
- replace(해당글자,바꿀글자) ⇒ 파일명을 바꾼다. 
확장자 바꿀때 유용하다.
- strip() ⇒ 문자열의 양 끝 불필요한 공백을 제거한다.

## print 사용법

1. f-string 사용
f-string은 파이썬 3.6 버전 이후부터 지원하는 문자열 포맷팅 방법입니다. 문자열 앞에 f 또는 F를 붙이고, 중괄호({}) 안에 변수 또는 표현식을 넣으면 됩니다. 예를 들어, 다음과 같이 사용할 수 있습니다.
    1. name = "Alice"
    age = 25
    print(f"My name is {name}, and I'm {age} years old.")
2. r-string 사용
r-string은 raw string을 의미하며, 이스케이프 시퀀스(Escape sequence)를 무시하고 문자 그대로 출력하는 방법입니다. 문자열 앞에 r 또는 R을 붙이면 됩니다. 예를 들어, 다음과 같이 사용할 수 있습니다.
    1. path = r"C:\Users\username\Documents"
    print(path)
3. format() 메소드 사용
format() 메소드를 사용하면, 중괄호({}) 안에 변수나 값을 넣어서 문자열을 포맷팅할 수 있습니다. 예를 들어, 다음과 같이 사용할 수 있습니다.
    1. name = "Bob"
    age = 30
    print("My name is {}, and I'm {} years old.".format(name, age))

## 함수 간단 정리

- **`split()`**
문자열.split(’구분자’) 
문자열을 특정 구분자를 기준으로 나누어 리스트로 만드는 함수
- **`remove()`**
리스트.remove(값) 
리스트에서 특정 값을 제거하는 함수
- **`enumerate()`**
enumerate(리스트) 
ex) **`enumerate(['apple', 'banana', 'orange'])`** 
결과: **`(0, 'apple'), (1, 'banana'), (2, 'orange')`**
리스트의 각 요소에 대해 인덱스와 함께 반복문을 수행하는 함수
- **`insert()`**
리스트.insert(삽입하려는 위치의 index, 추가할 요소)
리스트의 특정 위치에 요소를 추가하는 함수.
- **`lower(), upper()`**
문자열.lower() // 문자열.upper()
****문자열의 영문자들을 소문자, 대문자로 변환하는 함수
- `**startswith()**` 
문자열.startswith(검사할 문자열, 시작 인덱스, 끝 인덱스)
문자열이 특정 문자열로 시작하는지 검사하는 함수
- **`endswith()`**
문자열.endswith(검사할 문자열, 시작 인덱스, 끝 인덱스)
문자열이 특정 문자열로 끝나는지 검사하는 함수
- **`replace()`**
문자열.replace(교체할 문자열_old, 대체할 문자열_new)
문자열에서 특정 문자열을 다른 문자열로 교체하는 함수
- **`strip()`**
문자열.strip()
문자열의 양쪽 끝에서 특정 문자를 제거하는 함수
-