# 파이썬 리스트 컴프리헨션 사용하기

- 리스트 컴프리헨션은 코드를 더 간결하고 효율적으로 만들어주는 강력한 기능.
- 복잡한 반복문과 조건문을 한 줄의 코드로 간단히 표현하여 코드의 가독성과 성능을 동시에 챙길 수 있다.

## 리스트 컴프리헨션의 기본

- **형태**: `[표현식 for 항목 in 반복가능객체]`
- **조건 추가**: `[표현식 for 항목 in 반복가능객체 if 조건문]`

## 실제 사용 예시

### 기본 형태의 리스트 컴프리헨션

- **예시**: 0부터 9까지 숫자의 제곱을 계산
- **코드**: 
    ```python
    squares = [i ** 2 for i in range(10)]
    print(squares)  # 출력: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```

### 조건문을 포함한 리스트 컴프리헨션

- **예시**: 0부터 9까지 숫자 중 짝수만의 제곱을 계산
- **코드**: 
    ```python
    even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
    print(even_squares)  # 출력: [0, 4, 16, 36, 64]
    ```

### 중첩된 루프를 사용한 리스트 컴프리헨션

- **예시**: 두 리스트의 모든 조합에 대해 곱셈 수행
- **코드**: 
    ```python
    product = [x*y for x in [1, 2, 3] for y in [3, 4, 5]]
    print(product)  # 출력: [3, 4, 5, 6, 8, 10, 9, 12, 15]
    ```

### 복잡한 조건문

- **예시**: 조건문을 여러 개 사용하여 복잡한 필터링
- **코드**: 
    ```python
    complex_list = [i for i in range(30) if i % 2 == 0 if i % 3 == 0]
    print(complex_list)  # 출력: [0, 6, 12, 18, 24]
    ```

### if-else 구문

- **예시**: 각 숫자가 짝수면 'even', 홀수면 'odd'
- **코드**: 
    ```python
    even_odd = ['even' if i % 2 == 0 else 'odd' for i in range(10)]
    print(even_odd)  # 출력: ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']
    ```

### 문자열 리스트 처리

- **예시**: 문자열 리스트에서 길이가 5 이상인 문자열만 추출
- **코드**: 
    ```python
    words = ['apple', 'banana', 'cherry', 'date']
    long_words = [word for word in words if len(word) >= 5]
    print(long_words)  # 출력: ['apple', 'banana', 'cherry']
    ```

### 중첩 리스트 컴프리헨션

- **예시**: 2차원 리스트 평탄화
- **코드**: 
    ```python
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten_matrix = [num for row in matrix for num in row]
    print(flatten_matrix)  # 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```


## 데이터 처리를 위한 리스트 컴프리헨션 예시

### 1. 데이터 필터링

- **상황**: 어떤 데이터셋에서 특정 조건을 만족하는 요소만 추출하고 싶을 때.
- **예시**: 온도 데이터 리스트에서 25도 이상의 데이터만 추출하기.
- **코드**:
    ```python
    temperatures = [20, 22, 24, 27, 30, 18, 25]
    high_temperatures = [temp for temp in temperatures if temp >= 25]
    print(high_temperatures)  # 출력: [27, 30, 25]
    ```

### 2. 데이터 변환

- **상황**: 데이터셋의 각 요소에 대해 특정 변환을 적용하고 싶을 때.
- **예시**: 각 숫자의 제곱 값을 계산하기.
- **코드**:
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [number ** 2 for number in numbers]
    print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]
    ```

### 3. 데이터 정규화

- **상황**: 데이터셋의 모든 항목을 특정 범위 내로 스케일링하고 싶을 때.
- **예시**: 점수를 0과 1 사이로 정규화하기.
- **코드**:
    ```python
    scores = [234, 456, 678, 123]
    max_score = max(scores)
    normalized_scores = [score / max_score for score in scores]
    print(normalized_scores)  # 출력: [0.34513274336283184, 0.6725663716814159, 1.0, 0.18141592920353982]
    ```

### 4. 문자열 처리

- **상황**: 문자열로 이루어진 데이터셋에서 특정 패턴이나 조건에 부합하는 항목만 추출하고 싶을 때.
- **예시**: 이메일 주소 리스트에서 도메인이 'gmail.com'인 이메일만 추출하기.
- **코드**:
    ```python
    emails = ['user1@gmail.com', 'user2@yahoo.com', 'user3@gmail.com', 'user4@hotmail.com']
    gmail_users = [email for email in emails if '@gmail.com' in email]
    print(gmail_users)  # 출력: ['user1@gmail.com', 'user3@gmail.com']
    ```
- **예시**: 이메일 주소 리스트에서 도메인이 'gmail.com'인 이메일을 찾고, 도메인을 제외한 사용자 이름만 추출하기. 필터링과 변환을 한 줄로 할 수 있다.
- **코드**:
    ```python
    emails = ['user1@gmail.com', 'user2@yahoo.com', 'user3@gmail.com', 'user4@hotmail.com']
    gmail_usernames = [email.split('@')[0] for email in emails if '@gmail.com' in email]
    print(gmail_usernames)  # 출력: ['user1', 'user3']
    ```


### 5. 다차원 리스트 평탄화

- **상황**: 다차원 리스트를 단일 차원 리스트로 변환하고 싶을 때.
- **예시**: 2차원 리스트를 1차원 리스트로 평탄화하기.
- **코드**:
    ```python
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten = [num for row in matrix for num in row]
    print(flatten)  # 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

### 6. 복잡한 데이터 구조 변환

- **상황**: 복잡한 데이터 구조를 보다 단순하거나 다른 형태로 변환하고 싶을 때.
- **예시**: 사전의 리스트를 특정 키의 값으로만 이루어진 리스트로 변환하기.
- **코드**:
    ```python
    students = [
        {'name': 'Alice', 'grade': 90},
        {'name': 'Bob', 'grade': 85},
        {'name': 'Cindy', 'grade': 88}
    ]
    names = [student['name'] for student in students]
    print(names)  # 출력: ['Alice', 'Bob', 'Cindy']
    ```

### 7. 데이터 필터링과 변환-로그 데이터

- **상황**: 대규모 데이터셋에서 특정 조건을 만족하는 데이터만 추출하고, 동시에 특정 형식으로 변환해야 할 때.
- **예시**: 로그 데이터에서 특정 에러 코드를 포함하는 항목만 추출하고, 각 로그의 타임스탬프를 특정 형식으로 변환하는 경우
- **코드**:
    ```python
    log_data = [
    {"timestamp": "2024-01-01 10:00:00", "level": "error", "code": "E001"},
    {"timestamp": "2024-01-01 10:05:00", "level": "info", "code": "I001"},
    {"timestamp": "2024-01-01 10:10:00", "level": "error", "code": "E002"},
    # ... 기타 로그 데이터 ...
    ]

    # 에러 로그만 추출하고, 타임스탬프를 ISO 형식으로 변환
    error_logs = [
        {"timestamp": log["timestamp"].replace(" ", "T"), "code": log["code"]}
        for log in log_data if log["level"] == "error"
    ]
    print(error_logs)
    # 출력:
    # [
    #   {"timestamp": "2024-01-01T10:00:00", "code": "E001"},
    #   {"timestamp": "2024-01-01T10:10:00", "code": "E002"}
    # ]
    ```