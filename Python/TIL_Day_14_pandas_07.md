### datetime 변환

- OOOO-OO-OO 으로 되어 있는 data가 있다. type이 datetime이 아니라면 바꿔주자.
- `df[’columnName’] = pd.to_datetime(df[’columnName’])`

### apply

- apply는 Series나 DataFrame에 좀 더 구체적인 로직을 적용하고 싶은 경우 활용한다.
- apply() 함수는 함수를 인자로 받는다.
- dataframe의 행 또는 열을 이 함수에 전달한다.
- **함수의 반환값으로 새로운 데이터프레임을 생성한다. (series)**

```jsx
# 예시1
import pandas as pd

# 데이터프레임 생성
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# 열에 함수 적용
def square(x):
    return x ** 2
df['A_square'] = df['A'].apply(square)

# 행에 함수 적용
def sum_row(row):
    return row['A'] + row['B']
df['sum'] = df.apply(sum_row, axis=1)
```

- 결과
    
    ![Untitled](https://user-images.githubusercontent.com/82266289/226943828-86b8e845-28de-49c4-9fdc-372bbad34819.png)

    

```jsx
# 예시2
# '성별'컬럼의 '남자','여자'를 1,0으로 변경
df.loc[df['성별'] == '남자', '성별'] = 1
df.loc[df['성별'] == '여자', '성별'] = 0

apply와 함수를 통해 바꿀 수 있다.
def male_or_female(x):
    if x == '남자':
        return 1
    elif x == '여자':
        return 0
또는 
male_or_female = lambda x: 1 if x == '남자' else 0

사용은 이렇게 한다.
df['성별_NEW'] = df['성별'].apply(male_or_female)
```

### map (맵핑)

- 반복 가능한 객체에 대해 각 요소에 지정된 함수를 적용한 결과를 반환한다.
- 두 개의 인자를 받는데, 첫 번째 인자는 적용할 함수, 두 번째 인자는 함수를 적용할 시퀀스나 반복 가능한 객체이다. 보통 dictionary를 사용한다.
- df[’성별’].map(my_map)
my_map = {’남자’:1, ‘여자’:0}
성별 column에 있는 남자는 1로, 여자는 0으로 갱신한다.

### column간 연산 (+, -, *, /, %)

- column간 덧셈과 뺄셈은 있는 그대로 진행된다. 
a_column + b_column - c_column ⇒ 각 열마다 계산이 진행되어 열로 출력된다. (series)
- /(나눗셈)과 나머지(%)만 남기는 경우도 마찬가지이다. 값 하나하나를 가지고 하기에 사칙연산과 같다.
- `df['통계미술합계'] = df['통계'] + df['미술'] + 10` 이렇게 사용한다.
- NaN 값이 있는 경우 계산이 되지 않는다.

### DataFrame 간 연산

- df1 + df2 ⇒ 각 column data를 index에 맞게 연산한다.
- column data가 숫자인 경우에만 가능하다.
- DataFrame의 column명이 섞여있어도 가능하다. (단, 같아야 한다.)