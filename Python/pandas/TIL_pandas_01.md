## pandas 불러오기

- import pandas as pd

# 파일 읽기 및 쓰기

- 변수명 = pd.read_csv(’csv파일 dir’)
ex) df = pd.read_csv(r”C:\WORKSPACE-PYTHON\pythonEx\python practice\gugudan.csv”)
r을 붙이면 ‘ \ ’를 ‘ / ’로 바꾸지 않아도 된다.

# 기본 정보 알아보기(index, column, info, describe)

## column

- df.columns : column 명을 조회한다.
- df.columns = [’새로운 column 이름1’, ’새로운 column 이름2’, ’새로운 column 이름3’ …]
: 앞에서부터(0번) 새로운 column명으로 갱신한다.
: 새로운 column list를 변수에 담아 df.columns = 변수명 으로 해도 된다.

## index

- df.index
실행결과 : RangeIndex(start=0, stop=15, step=1)
: 인덱스가 어떻게 짜여져있는지 조회한다.

## info & describe

- df.info()
: info 메소드는 주로 빠진 값(null)과 데이터 타입을 볼 때 유용하다.
    
    ![Untitled](https://user-images.githubusercontent.com/82266289/225621683-567588f1-9b54-4b2c-9fd8-a0821e8604c8.png)
    
- df.describe()
:다양한 통계 수치를 일목요연하게 보여준다.
    
    ![Untitled](https://user-images.githubusercontent.com/82266289/225621712-e69dbe38-d113-4f7e-bbbf-68e78f330454.png)
    

## 형태 및 자료 파악하기

- df.shape
실행결과 : (15, 8)
: shape는 tuple 형태로 반환되며, (row의 수, column의 수)를 의미한다.
- head(), tail()
: 상위, 하위 row를 출력한다. 매개변수로 양수를 전달하여 사용하며 기본값은 5이다.
<br><br>

# 데이터 다루기
- (df⇒데이터가 담긴 변수명)

## 데이터 정렬

- `df.sort_index()`
: index를 기반으로 정렬
: 오름차순 정렬(default, ascending=True)
: 내림차순 정렬(ascending=False)
- `df.sort_values(by=’column명’, ascending=)`
: ‘column명’의 column 데이터를 오름차순(default) / 내림차순(ascending=False)으로 정렬한다.
    - 복수 정렬
    `df.sort_values(by=[’column1’, ‘column2’…])`
    : 정렬기준 우선순위 : 1. column1 2. column2 
    ⇒ 우선 column1으로 정렬 그래도 동일한 데이터는 column2를 기준으로 정렬

## 데이터 선택

### 개별 선택

- `df[’column명’]` or `df.column명`
: 해당 column의 데이터가 series 타입으로 호출된다.

### 단순 index에 대한 범위 선택(행 출력)

- 리스트 슬라이싱 기능을 활용한다.
- df[행 번호 이상(default=0): 행 번호 미만]
: df[:] ⇒ 전체 행 출력.
: df[:3]
: 0행부터 3행 미만
df.head(3)과 같은 표현

### 특정 column의 행 데이터 선택

- df.loc[행 번호 이상:행 번호 미만 , ‘column명’] or df.loc[:, [‘column명1’, ‘column명2’, …]
column에 대해 단수 선택과 복수 선택이 모두 가능하다.